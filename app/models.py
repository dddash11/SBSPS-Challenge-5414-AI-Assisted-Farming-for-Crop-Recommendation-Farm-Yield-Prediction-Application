from flask_login import UserMixin
from typing import Dict, Optional
users: Dict[str, "User"] = {}

class User(UserMixin):
    def __init__(self, id: str, name: str, email: str, password: str, typeofuser:str):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.typeofuser= typeofuser

    @staticmethod
    def get(user_id: str) -> Optional["User"]:
        return users.get(int(user_id))
