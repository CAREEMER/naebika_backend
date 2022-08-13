from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    vk_id: str


class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)


class UserCreate(UserBase):
    pass
