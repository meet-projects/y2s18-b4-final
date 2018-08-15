from sqlalchemy import Column, Integer, String, Boolean, Float
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
    email = Column(String)


    def __repr__(self):
        return ("User Name: {}, Password: {}, Email: {}".format(self.user_name, self.password, self.email))
class Posts(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key = True)
    user_name = Column(String)
    message = Column(String)
    image = Column(String)
    def __repr__(self):
        return ("Name: {}, message: {}".format(self.user_name, self.message))
           
class Contacts(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    second_name = Column(String)
    city = Column(String)
    subject = Column(String)
    message = Column(String)


    def __repr__(self):
        return ("First Name: {}, Last name: {}, City: {}, Subject: {}, Message: {}".format(self.first_name, self.second_name, self.city, self.subject, self.message))

class Position(Base):
    __tablename__ = "positions"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    longitude = Column(Float)
    latitude = Column(Float)

    def __repr__(self):
        return ("name: {}\n, longi: {}\n, lati: {}\n\n".format(self.name, self.longitude, self.latitude))

