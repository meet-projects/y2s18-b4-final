from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Place your database schema code here

# Example code:
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    user_name = Column(String)
    password = Column(String)


    def __repr__(self):
        return ("User Name: {}, Password: {}".format(self.user_name, self.password))