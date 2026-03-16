from pydantic import BaseModel

class UserSchema(BaseModel):
    id: str
    email: str
    last_name: str
    first_name: str
    middle_name: str


user = User(id=1, name="222", email="")
print(user)
