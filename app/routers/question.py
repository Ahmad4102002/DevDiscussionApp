from fastapi import APIRouter,status,Depends
from app import schemas 
from app.database import get_db
from app.core.security import get_current_user
from sqlalchemy.orm import Session
from app import models

router = APIRouter(
    prefix="/questions",
    tags=['QUESTIONS']
)

# create model 
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.QuestionOut)
def create_questions(post: schemas.QuestionCreate, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):

    new_post = models.Question(owner_id=current_user.id,**post.model_dump())
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post