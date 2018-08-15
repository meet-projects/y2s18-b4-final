# Database related imports
# Make sure to import your tables!
from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db', connect_args={'check_same_thread':False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)

# Example of adding a student:
def add_user(user_name, password, email):
    account = Users(user_name=user_name, password=password, email = email)
    session.add(account)
    session.commit()
def get_user_by_name(name):
	account = session.query(Users).filter_by(user_name = name).first()
	return account
def get_all_users():
    users = session.query(Users).all()
    return users
def check_password(user_name, entered_password):
	account = session.query(Users).filter_by(user_name = user_name).first()
	if account.password == entered_password:
		return True
	else:
		return False
def add_message(name, msg, img):
	msg = Posts(user_name = name, message = msg, image = img)
	session.add(msg)
	session.commit()
def get_all_msgs():
	messages = session.query(Posts).all()
	return messages
def delete_all_msgs():
	session.query(Posts).delete()
	session.commit()
def delete_all_users():
	session.query(Users).delete()
	session.commit()
def add_contact(first_name, second_name, city, subject, message):
	contact = Contacts(first_name = first_name, second_name = second_name, city = city, subject = subject, message = message)
	session.add(contact)
	session.commit()
def query_contacts():
	contacts = session.query(Contacts).all()
	return contacts
def add_pos(name, longi, lat):
	pos = Position(name = name, longitude = longi, latitude = lat)
	session.add(pos)
	session.commit()
def query_pos():
	return session.query(Position).all()
def delete_all_pos():
	session.query(Position).delete()
	session.commit()
