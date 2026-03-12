from sqlalchemy import Column, Integer, String, Boolean,text , ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, nullable= False)
    username = Column(String, nullable = False, unique = True)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable=False )
    created_at = Column(TIMESTAMP(timezone= True), nullable= False, server_default=text('now()'))

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key = True, nullable= False)
    title = Column(String, nullable = False)
    body = Column(String, nullable = False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"),nullable = False)
    published = Column(Boolean, server_default= text("true"), nullable=False)
    created_at = Column(TIMESTAMP(timezone= True), nullable= False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True, onupdate=text('now()'))

    owner = relationship("User")