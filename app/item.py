from dataclasses import dataclass

from user import User

@dataclass
class Item:
    uid: int
    name: str
    information: str
    category: str
    constraint: str = None
    shared_with: list = None
    owner: User = None
