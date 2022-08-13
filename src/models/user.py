from sqlmodel import Field, SQLModel
import uuid as uuid_pkg


class UserBase(SQLModel):
    id: str = Field(default=None, index=True, primary_key=True)
    bdate: str
    photo_200: str
    photo_max_orig: str
    photo_100: str
    first_name: str
    last_name: str


class User(UserBase, table=True):
    pass


class UserCreate(UserBase):
    pass


class UserToken(SQLModel, table=True):
    token: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    user_id: str = Field(foreign_key="user.id")
