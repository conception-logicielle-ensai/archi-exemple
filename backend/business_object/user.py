from typing import Optional


class User:
    def __init__(self, id: Optional[str], username: str, roles: Optional[list[str]]):
        self.id = id
        self.username = username
        self.roles = roles

    def __str__(self):
        return f"User(username={self.username},roles={self.roles})"

    def __repr__(self):
        return f"User(username={self.username}, roles={self.roles})"

    def is_admin(self):
        return "admin" in self.roles
