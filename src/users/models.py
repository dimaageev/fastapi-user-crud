from enum import Enum

from sqlmodel import Field, SQLModel


class Employed(Enum):
    yes = 1
    no = 0


class UserBase(SQLModel):
    name: str
    age: int
    employed: Employed


class UserBaseUpdate(SQLModel):
    name: str | None = None
    age: int | None = None
    employed: Employed | None = None


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
