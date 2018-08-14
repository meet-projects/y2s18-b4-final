# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session
# Add functions you need from databases.py to the next line!
from databases import add_user, get_all_msgs, get_user_by_name, check_password, add_message, get_all_users, add_contact, add_pos
from model import *
# Starting the flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf movies'

# App routing code here
@app.route('/home', methods=['GET','POST'])
def home():
    if 'user_name' in session:
        username = session['user_name']
        print ("hello "+username)
        if request.method == 'GET':

            return render_template('home.html', posts = get_all_msgs(), username = username)
        else:
            name = username
            msg = request.form['message']
            img = request.form['image']
            if msg == "" and img == "":
                return render_template(

                    "home.html",
                    posts = reversed(get_all_msgs()),
                    username = username


                    )
            else:
                add_message(name,msg,img)
                return render_template(

                    "home.html",
                    posts = reversed(get_all_msgs()),
                    username = username


                    )
    else:
        return redirect(url_for('login'))

#register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        accounts = get_all_users()
        is_open = True
        for account in accounts:
            if request.form['user_name'] == account.user_name:
                is_open = False
        if is_open == True:
            password = request.form['password']
            confirm = request.form['password-confirm']
            if password == confirm:
                add_user(request.form['user_name'],
                    request.form['password'])
                return redirect(url_for('login'))
            else:
                return redirect(url_for('register'))
        else:
            return  redirect(url_for('register'))

#login route
@app.route('/', methods=(['GET' , 'POST']))
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        render_template('login.html')

        print("trying to login")

        username = request.form['user_name']
        password = request.form['password']
        accounts = get_all_users()
        is_here = False
        for account in accounts:
            if account.user_name == username:
                is_here = True
        if is_here == True:
            if check_password(username,password) == True:
                print("good password")
                session['user_name'] = username
                return(redirect(url_for('home')))
            else:
                return(redirect(url_for('login')))
        else:
            return redirect(url_for('login'))
@app.route('/about_us')
def about_us():
    if 'user_name' in session:
        username = session['user_name']
        if request.method == 'GET':
            return render_template('about_us.html', username = username)
        else:
            first_name = request.form['firstname']
            second_name = request.form['lastname']
            city = request.form['city']
            subject = request.form['subject']
            message = request.form['message']
            add_contact(first_name,second_name,city,subject,message)
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_name', None)
    return redirect(url_for('login'))

@app.route('/contact', methods=['GET','POST'])
def contact_us():
    if 'user_name' in session:
        username = session['user_name']
        return render_template('contact.html', username = username)
    else:
        return render_template('login.html')
@app.route('/map')
def map():
    if 'user_name' in session:
        username = session['user_name']
        return render_template('map.html', username = username)
    else:
        return render_template('login.html')
@app.route('/report', methods=['GET','POST'])
def report():
    if 'user_name' in session:
        username = session['user_name']

        if request.method == 'GET':
            return render_template('report.html', username = username)
        else:
            name = request.form['location_name']
            longi = request.form['longitude']
            lat = request.form['latitude']
            add_pos(name,longi,lat)
            return render_template('report.html', username = username)
    else:
        return render_template('login.html')
@app.route('/profile/<string:username>')
def index(username): 
	return render_template('profile.html',username=username)


# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)

