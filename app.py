# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import *
from model import *
# Starting the flask app
app = Flask(__name__)

# App routing code here
@app.route('/home')
def home():
    if request.method == 'GET':

        return render_template('home.html', posts = get_all_msgs())
    else:
        name = request.form['name']
        msg = request.form['message']
        add_message(name,msg)
        return(render_template(

            "home.html",
            posts = get_all_msgs()


            )



        )
#register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        add_user(request.form['user_name'],
            request.form['password'])
        return redirect(url_for('login'))
#login route
@app.route('/', methods=(['GET' , 'POST']))
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['user_name']
        password = request.form['password']
        if check_password(username,password) == True:
            redirect(url_for('home'))
        else:
            redirect(url_for('login'))
@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
