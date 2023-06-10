from dataclasses import dataclass

@dataclass
class Group:
    uid: int
    name: str
    informations: str
    access_code: str
    is_public: bool
    users: [] = None