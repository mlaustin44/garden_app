from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
import sys

#DB_LOCATION = os.getenv('DB_LOCATION')
DB_LOCATION = 'sqlite:///test.db'

#create database engine
db_engine = create_engine(DB_LOCATION)

#create session registry (passing factory method for new sessions)
db_session = scoped_session( sessionmaker( autocommit=False,
                                            autoflush=False,
                                            bind=db_engine))

Base = declarative_base()
Base.query = db_session.query_property()

