from bottle import run, template, route, static_file, error, request, response, redirect
from os import  getcwd
from pathlib import Path
from database_manager import get_db_user, get_db_personal_items, get_db_groups, get_db_available_items, get_db_authenticated_user, \
    db_check_login, NotFoundException, get_group_details, db_join_group, get_instance_categories, db_create_group, db_create_item, get_db_item, db_share_item, get_db_group_containing_user, db_put_user_in_group

from user import User
from item import Item

COOKIE_SECRET = 'aM11dnfi2Ofp8wKql86fUv9jE'
COOKIE_NAME = 'nadaq_session'


@route('/')
def get_home(message=None):
    current_user = _get_logged_user()
    if current_user is not None:
        redirect('/my_inventory')

    return template('home.tpl', {'message': message})

@route('/create_account')
def create_account():
    return get_home(message='Account creation is not active')

@route('/login', method='POST')
def login():
    login = request.forms.get('login')
    password = request.forms.get('password')

    if db_check_login(login=login, password=password):
        response.set_cookie(COOKIE_NAME, login, secret=COOKIE_SECRET)
        redirect('/my_inventory')

    return get_home('Authentication failed')


@route('/user/<user_uid:int>')
def get_user(user_uid):
    user = get_db_user(user_uid=user_uid)
    user_data = {'name': user.name, 'contact': user.contact_info, 'location': user.location_info}
    groups = get_db_group_containing_user(user_uid=user_uid)
    return template(
        'registered_user_page.tpl', 
        {'user': user, 'groups': groups})

@route('/my_inventory')
def get_personal_inventory():
    current_user = _get_logged_user()
    if current_user is not None:
        items = get_db_personal_items(current_user=current_user)
        return template('my_inventory.tpl', {'item_list': items})
    redirect('/')

@route('/create_item', method='GET')
def item_form():
    current_user = _get_logged_user()
    if current_user is not None:
        categories = get_instance_categories()
        return template('create_item.tpl', {'categories': categories})
    redirect('/')

@route('/create_item', method='POST')
def create_item():
    current_user = _get_logged_user()
    if current_user is not None:
        item = Item(
            uid=-1,
            name=request.forms.get('name'),
            information=request.forms.get('information'),
            category=request.forms.get('category'),
            constraint=request.forms.get('constraint'),
        )
        db_create_item(current_user, item)
        redirect('/my_inventory')

@route('/import_item', method='GET')
def import_item_form():
    return "Import by CSV is not implemented for now"

@route('/item/<item_uid>')
def item_detail(item_uid):
    item = get_db_item(item_uid, include_shared_groups=True, include_owner=True)
    # Doesn't display contact if we own this object
    current_user = _get_logged_user()
    if current_user is not None:
        item_owner = item.owner if item.owner.uid != current_user.uid else None

    return template(
        'item_details.tpl', 
        {'item': item, 'shared_groups': item.shared_with, 'item_owner': item_owner}
    )

@route('/item/<item_uid>/share', method='GET')
def share_form(item_uid):
    current_user = _get_logged_user()
    if current_user is not None:
        groups = get_db_groups(current_user=current_user, include_public=True)
        item = get_db_item(item_uid)
        return template('share_item.tpl', {'groups': groups, 'item': item})

@route('/item/<item_uid>/share', method='POST')
def share(item_uid):
    group_uid = request.forms.get('group')
    constraint = request.forms.get('constraint')
    db_share_item(item_uid=item_uid, group_uid=group_uid, constraint=constraint)
    redirect('/item/'+item_uid)
    
@route('/my_groups')
def get_personal_groups():
    current_user = _get_logged_user()
    if current_user is not None:
        groups = get_db_groups(current_user=current_user, include_public=True)
        member_groups = get_db_group_containing_user(user_uid=current_user.uid)
        return template('my_groups.tpl', {'groups': groups, 'member_groups': member_groups})
    get_home()

@route('/create_group', method='GET')
def group_form():
    return template('create_group.tpl')

@route('/create_group', method='POST')
def create_group():
    current_user = _get_logged_user()
    if current_user is not None:
        group_name = request.forms.get('name')
        group_info = request.forms.get('informations')
        db_create_group(current_user, group_name, group_info)
        redirect('/my_groups')

@route('/group/<group_uid>')
def group_details(group_uid):
    group = get_group_details(group_uid, include_users=True)
    return template('group_details.tpl', {'group': group, 'users': group.users})

@route('/group/<group_uid>/join')
def join_group(group_uid):
    current_user = _get_logged_user()
    if current_user is not None:
        db_join_group(user=current_user, group_uid=group_uid)
        redirect('/my_groups')

@route('/create_relation/<user_uid:int>', method='GET')
def relation_form(user_uid):  # put user in group
    current_user = _get_logged_user()
    if current_user is not None:
        user = get_db_user(user_uid=user_uid)
        groups = get_db_groups(current_user=current_user, include_public=False)
        return template('create_relation.tpl', {'groups': groups, 'user': user})

@route('/create_relation', method='POST')
def create_relation():
    group_uid = request.forms.get('group')
    user_uid = request.forms.get('user')
    create_new_group = request.forms.get('new_group')
    if create_new_group:
        return "Create a new group during add is not implemented" 

    db_put_user_in_group(user_uid, group_uid)
    redirect('/user/'+user_uid)

@route('/available_items')
def get_global_inventory():
    current_user = _get_logged_user()
    if current_user is not None:
        items = get_db_available_items(current_user=current_user)
        categories = get_instance_categories()
        return template('inventory.tpl', {'item_list': items, 'categories': categories})
    redirect('/')

@route('/available_items/filter/<category_name>')
def filtered_inventory():
    return "Filter by category is not implemented" 

@route('/settings')
def my_settings():
    current_user = _get_logged_user()
    if current_user is not None:
        return template('settings.tpl', {'user': current_user})
    get_home()

@route('/logoff')
def logoff():
    response.delete_cookie(COOKIE_NAME, secret=COOKIE_SECRET)
    redirect('/')

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root=Path(getcwd(), 'static'))

@error(404)
@error(500)
def error(error):
    return "<html><body>This page does not exists - Functionnality not implemented</body></html>"


def _get_logged_user():
    login = request.get_cookie(COOKIE_NAME, secret=COOKIE_SECRET)
    try:
        return get_db_authenticated_user(login=login, from_cookie=True)
    except NotFoundException:
        return None

run(host='localhost', port=8080, debug=True, reloader=True)