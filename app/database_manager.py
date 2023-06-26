#! /bin/python3

from pathlib import Path
import sqlite3
import re
import bcrypt

from user import User
from item import Item
from group import Group

application_path = Path.cwd()
if str(application_path).endswith('app'):
    application_path = application_path.parent
DATABASE_PATH = application_path / 'db' / 'database'

class NotFoundException(Exception):
    pass

class DatabaseError(Exception):
    pass


def get_hashed_password(password): #TODO: use this when you insert/update user password before storing to db
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def check_password(password, hash):
    return bcrypt.checkpw(password.encode('utf-8'), hash.encode('utf-8'))


def db_check_login(login:str, password:str):
    try:
        get_db_authenticated_user(login=login)
        return True
    except NotFoundException:
        return False


def get_db_user(user_uid:str) -> User:
    if not DATABASE_PATH.is_file():
        raise DatabaseError

    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            'SELECT uid, name, contact_informations, location_information FROM user WHERE uid =:user_uid AND is_active = 1', 
            {'user_uid': user_uid}
        )
        db_user = cursor.fetchone()

    if db_user is None:
        raise NotFoundException

    return User(
        uid=db_user[0],
        name=db_user[1],
        contact_info=db_user[2] or '',
        location_info=db_user[3] or '',
    )

def get_db_authenticated_user(login:str) -> User:
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            'SELECT uid, name, contact_informations, location_information, is_active FROM user WHERE login =:login', 
            {'login': login}
        )
        db_user = cursor.fetchone()

    if db_user is None:
        raise NotFoundException

    if bool(db_user[4]) == False:  # is_active field
        raise NotFoundException

    return User(
        uid=db_user[0],
        name=db_user[1],
        contact_info=db_user[2] or '',
        location_info=db_user[3] or '',
    )

def _read_field(instance_information_field:str, attribute:str):
    if instance_information_field is None or attribute is None:
        return None
    found = re.search(attribute+r':([a-zA-Z\-_]*)', instance_information_field)
    if found:
        return found.group(1)
    return None

def get_db_item(item_uid:int, include_shared_groups=False, include_owner=False) -> Item:
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            'SELECT uid, name, informations, instance_information, owner_uid FROM item WHERE uid = :uid',
            {'uid': item_uid}
        )
        db_items = cursor.fetchall()

    row_item = db_items[0]
    item = Item(
        uid=row_item[0],
        name=row_item[1],
        information=row_item[2],
        category=_read_field(row_item[3], 'category')
    )

    owner_uid = row_item[4]
    if include_owner:
        item.owner = get_db_user(user_uid=owner_uid)

    if include_shared_groups:
        groups = []
        with sqlite3.connect(DATABASE_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'SELECT user_group.uid, user_group.name FROM offer INNER JOIN user_group ON user_group.uid = offer.user_group_uid WHERE offer.item_uid = :item_uid',
                {'item_uid': item_uid}
            )
            db_groups = cursor.fetchall()
        
        for row_group in db_groups:
            group = Group(
                uid=row_group[0],
                name=row_group[1],
                informations='',
                access_code='',
                is_public=False,
            )
            groups.append(group)
        item.shared_with = groups

    return item
    

def get_db_personal_items(current_user:User) -> [Item]:
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            'SELECT uid, name, informations, instance_information FROM item WHERE owner_uid = :owner_uid ORDER BY name',
            {'owner_uid': current_user.uid}
        )
        db_items = cursor.fetchall()

    personal_items = []
    if db_items is None:
        return personal_items

    for row_item in db_items:
        item = Item(
            uid=row_item[0],
            name=row_item[1],
            information=row_item[2],
            category=_read_field(row_item[3], 'category'),
            shared_with='Not implemented',
            owner=current_user,
        )
        personal_items.append(item)

    return personal_items


def get_group_details(group_uid, include_users=False):
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            'SELECT uid, name, informations, access_code, is_public FROM user_group WHERE uid = :group_uid',
            {'group_uid': group_uid}
        )
        db_group = cursor.fetchall()

    row_group = db_group[0]
    group = Group(
        uid=row_group[0],
        name=row_group[1],
        informations=row_group[2] or '',
        access_code=row_group[3] or '',
        is_public=bool(row_group[4]) ,
    )

    if include_users:
        group_users = []
        with sqlite3.connect(DATABASE_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'SELECT user.uid, user.name FROM user INNER JOIN user_group_relation ON user_group_relation.user_uid = user.uid WHERE user_group_uid = :group_uid',
                {'group_uid': group_uid}
            )
            db_users = cursor.fetchall()
        for row_user in db_users:
            u = User(uid=row_user[0], name=row_user[1])
            group_users.append(u)
        group.users = group_users
    
    return group

def get_db_group_containing_user(user_uid) -> [Group]:
    groups_for_this_user = []
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            'SELECT user_group.uid, user_group.name FROM user_group_relation INNER JOIN user_group ON user_group_relation.user_group_uid = user_group.uid WHERE user_group_relation.user_uid = :user_uid',
            {'user_uid': user_uid}
        )
        db_groups = cursor.fetchall()

    for row_group in db_groups:
        group = Group(
            uid=row_group[0],
            name=row_group[1],
            informations='',
            access_code='',
            is_public=False,
        )
        groups_for_this_user.append(group)

    return groups_for_this_user
    

def db_create_group(current_user, group_name, group_info):
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO user_group("name", "informations", "is_public", "group_owner") VALUES (?, ?, ?, ?)', (group_name, group_info, False, current_user.uid))
        connection.commit()

def db_join_group(user, group_uid):
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO user_group_relation VALUES (?, ?)', (user.uid, group_uid))
        connection.commit()

def db_put_user_in_group(user_uid, group_uid):
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO user_group_relation VALUES (?, ?)', (user_uid, group_uid))
        connection.commit()

def get_instance_categories() -> [str]:
    return ['Art', 'Computer', 'Cooking', 'DIY', 'Other']


def get_db_groups(current_user:User, include_public:bool=False) -> [Group]:

    query_private_only = 'SELECT uid, name, informations, access_code, is_public FROM user_group WHERE group_owner = :owner_uid ORDER BY name ASC'
    query_with_public = 'SELECT uid, name, informations, access_code, is_public FROM user_group WHERE is_public = 1 OR group_owner = :owner_uid ORDER BY is_public DESC, name ASC'

    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            query_with_public if include_public else query_private_only,
            {'owner_uid': current_user.uid}
        )
        db_groups = cursor.fetchall()

    groups = [] 
    if db_groups is None:
        return groups

    for row_group in db_groups:
        group = Group(
            uid=row_group[0],
            name=row_group[1],
            informations=row_group[2] or '',
            access_code=row_group[3] or '',
            is_public=bool(row_group[4]) ,
        )
        groups.append(group)

    return groups

def db_create_item(current_user:User, item: Item):
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO item("name","informations","instance_information","owner_uid") VALUES (?, ?, ?, ?)',
            (item.name, item.information, 'category:'+item.category, current_user.uid)
        )
        connection.commit()

def db_share_item(item_uid, group_uid, constraint):
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO offer("item_uid","user_group_uid","informations", "timestamp") VALUES (?, ?, ?, ?)',
            (item_uid, group_uid, constraint, 42)
        )
        connection.commit()

def get_db_available_items(current_user:User) -> [Item]:
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()

        cursor.execute(
            'SELECT item.uid, item.name, item.informations, item.instance_information FROM item INNER JOIN offer ON offer.item_uid = item.uid WHERE offer.user_group_uid = :public_group_id',
            {'public_group_id': 1}
        )
        db_public_items = cursor.fetchall()

        cursor.execute(
            'SELECT item.uid, item.name, item.informations, item.instance_information FROM item INNER JOIN offer ON offer.item_uid = item.uid INNER JOIN user_group_relation ON user_group_relation.user_group_uid = offer.user_group_uid WHERE user_group_relation.user_uid = :user_uid',
            {'user_uid': current_user.uid}
        )
        db_community_items = cursor.fetchall()

    available_items = []

    for row_item in db_public_items:
        item = Item(
            uid=row_item[0],
            name=row_item[1],
            information=row_item[2],
            category=_read_field(row_item[3], 'category'),
            shared_with=None,
            owner=None,
        )
        available_items.append(item)

    for row_item in db_community_items:
        item = Item(
            uid=row_item[0],
            name=row_item[1],
            information=row_item[2],
            category=_read_field(row_item[3], 'category'),
            shared_with=None,
            owner=None,
        )
        available_items.append(item)

    return available_items
