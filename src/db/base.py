# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_CONN = "mysql+pymysql://root:root@localhost/mecatoldb?charset=utf8"

#  Create an engine
engine = create_engine(DB_CONN, encoding='utf8')

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Create a declarative base
Base = declarative_base()
metadata = Base.metadata
