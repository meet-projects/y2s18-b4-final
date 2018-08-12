# Database related imports
# Make sure to import your tables!
from model import Base, Users

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)

# Example of adding a student:
def add_user(user_name, password):
    account = Users(user_name=user_name, password=password)
    session.add(account)
    session.commit()

def get_all_users():
    users = session.query(Users).all()
    return users
def check_password(user_name, entered_password):
	account = session.query(Users).filter_by(user_name = user_name).first()
	if account.password == entered_password:
		return True
	else:
		return False
def add_message(name, msg):
	msg = Posts(user_name = name, message = msg)
	session.add(msg)
	session.commit()
def get_all_msgs():
	messages = session.query(Posts).all()
	return messages
print(get_all_users())