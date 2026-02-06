from typing import Optional

from pydantic import BaseModel, Field

from business_object.user import User


class UserConnectDTO(BaseModel):
    username: str = Field(examples=["adm", "pasadm"])

    def to_user(self):
        """Convert DTO to a plain User object."""
        return User(id=None, username=self.username, roles=None)


class UserCreateDTO(BaseModel):
    username: str
    roles: Optional[list[str]] = []
