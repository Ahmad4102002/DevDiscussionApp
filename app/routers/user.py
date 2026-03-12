from fastapi import APIRouter,status,Depends,HTTPException
from .. import utils,schemas,models
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix = "/users",
    tags = ['USERS']
)


# Endpoint for creating the user
    # cretae response model 
    # create util for hashing passwor 

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate,db:Session = Depends(get_db)):

    existing_user = db.query(models.User).filter(models.User.username == user.username).first()
    existing_email = db.query(models.User).filter(models.User.email == user.email).first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={"data": "username already taken"}
    )
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={"data": "email already taken"}
    )




    hashed_password = utils.hash(user.password)
    

    new_user = models.User(**user.model_dump())
    new_user.password = hashed_password
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
