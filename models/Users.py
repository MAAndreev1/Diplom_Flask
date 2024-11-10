from backend.db import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models import *


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)

    posts = relationship('Posts')
