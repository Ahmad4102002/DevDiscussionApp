from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):

    # Actual database

    # id
    # username
    # email
    # hashed_password
    # created_at

    username : str 
    email : EmailStr
    password : str

