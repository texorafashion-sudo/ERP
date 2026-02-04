from pydantic import BaseModel


class RoleBase(BaseModel):
    name: str
    description: str | None = None


class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    full_name: str
    email: str
    role_id: int


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
