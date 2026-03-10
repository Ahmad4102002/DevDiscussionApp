from fastapi import APIRouter,status,Depends
from .. import utils,schemas
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix = "/users",
    tags = ['USERS']
)


# Endpoint for creating the user
    # cretae response model 
    # create util for hashing passwor 
    # Create db session dependency
@router.post("/",status_code=status.HTTP_201_CREATED)
def create_user(user:schemas.UserCreate,db:Session = Depends(get_db)):