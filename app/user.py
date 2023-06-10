from dataclasses import dataclass

@dataclass
class User:
    uid: int
    name: str
    contact_info: str = None
    location_info: str = None
