from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    """
    Описание структуры пользователя
    """
    id: str
    email: EmailStr
    lastName: str
    firstName: str
    middleName: str

class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: EmailStr
    password: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseDict(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema