from sqlalchemy import create_engine
from sqlalchemy.ext import declarative
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.dialects.mssql import pyodbc

engine = create_engine('postgresql://user:password@server:port/database_name')
_SessionFactory = sessionmaker(bind=engine)
Base = declarative.declarative_base()

def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()