from pydantic import BaseModel,EmailStr,ConfigDict
from datetime import datetime
from typing import Optional



#-------------------------------------------------
# USER Request and Response Models
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


class UserOut(BaseModel):
    
    model_config = ConfigDict(from_attributes=True)

    id: int
    username:str
    email:EmailStr
    created_at: datetime

#-------------QUESTIONS-------------------------------
class QuestionCreate(BaseModel):

    title:str
    body:str

class QuestionOut(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id:int
    title: str 
    body:str
    owner_id:int
    owner: UserOut
    published:bool
    created_at: datetime
    updated_at: Optional[datetime]


#-----------------------------------------------------
class Token(BaseModel):
    access_token:str
    token_type:str


class TokenData(BaseModel):
    id: int

