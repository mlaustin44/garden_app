from sqlalchemy import Column, String, Integer, Float

from models.database import Base

class User(Base):
    __tablename__ = 'user'
    id = Column('user_id', Integer, primary_key=True)
    name = Column('user_name', String, nullable=False)
    email = Column('user_email', String, nullable=False)