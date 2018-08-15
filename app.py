# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session as login_session
from flask_mail import Mail, Message
# Add functions you need from databases.py to the next line!
from databases import add_user, get_all_msgs, get_user_by_name, check_password, add_message, get_all_users, add_contact, add_pos, session, get_all_msgs_name
from model import *
# Starting the flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf movies'

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'recycledtrash.meet@gmail.com',
    MAIL_PASSWORD = 'xzaq1234',
))

mail = Mail(app)


# App routing code here
@app.route('/home', methods=['GET','POST'])
def home():
    if 'user_name' in login_session:
        username = login_session['user_name']
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
            email = request.form['email']
            username = request.form['user_name']
            msg = Message("Hello " + request.form['user_name'],
                  sender="recycledtrash.meet@gmail.com",
                  recipients=[email])
            msg.body = "hello " + username +", \n your password is: " + password

            if password == confirm:
                mail.send(msg)
                add_user(request.form['user_name'],
                    request.form['password'],
                    request.form['email'])
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
                login_session['user_name'] = username
                return(redirect(url_for('map')))
            else:
                return(redirect(url_for('login')))
        else:
            return redirect(url_for('login'))
@app.route('/about_us')
def about_us():
    if 'user_name' in login_session:
        username = login_session['user_name']
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
    login_session.pop('user_name', None)
    return redirect(url_for('login'))

@app.route('/contact', methods=['GET','POST'])
def contact_us():
    if 'user_name' in login_session:
        username = login_session['user_name']
        return render_template('contact.html', username = username)
    else:
        return render_template('login.html')
@app.route('/map')
def map():
    if 'user_name' in login_session:
        username = login_session['user_name']
        points = session.query(Position).all()
        marker_list = []
        name_list = []
        for point in points:
            marker_list.append([point.latitude, point.longitude])
            name_list.append(point.name)

        return render_template('map.html', username = username, marker_list=marker_list, name_list=name_list)
    else:
        return render_template('login.html')
@app.route('/report', methods=['GET','POST'])
def report():
    if 'user_name' in login_session:
        username = login_session['user_name']

        if request.method == 'GET':
            return render_template('report.html', username = username)
        else:
            name = request.form['location_name']
            longi = float(request.form['longitude'])
            lat = float(request.form['latitude'])
            add_pos(name,longi,lat)
            return redirect(url_for('map'))
    else:
        return render_template('login.html')


@app.route('/profile')
def profile():
    if 'user_name' in login_session:
        username = login_session['user_name']
        posts = get_all_msgs_name(username)
        print(posts)
        return render_template("profile.html",
            username=username,
            posts = posts
            )
    else:
        return redirect(url_for('login'))



# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)

