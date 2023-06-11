import flask
from data import *
from forms import *
from werkzeug.security import generate_password_hash, check_password_hash


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'dsljfkldjboisdjlkdsjfophgsdgodhoud'
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    session = Session()
    user = session.query(User).get(user_id)
    session.close()
    return user


@app.route('/')
def home():
    if flask_login.current_user.is_authenticated:
        return flask.render_template("index.html", logged_in = True)
    
    return flask.render_template('index.html', logged_in = False)


@app.route('/register', methods = ['GET', 'POST'])
def register():
    session = Session()
    form = SignIn()
    if flask.request.method == 'POST':
        email = flask.request.form.get('email')
        password = generate_password_hash(flask.request.form.get('password'), salt_length = 8)
        
        if session.query(User).filter_by(email = email).first():
            error = 'You have already signed up with that email log in instead'
            return flask.render_template('register.html', error = error, form = form)
        
        new_user = User(email, password, flask.request.form.get('name'))
        session.add(new_user)
        session.commit()
        new_user = session.query(User).filter_by(email = email).first()
        flask_login.login_user(new_user)
        session.close()
        
        return flask.redirect(flask.url_for('secrets'))
        
    return flask.render_template("register.html", form = form)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LogIn()

    if flask.request.method == 'POST':
        session = Session()
        user = session.query(User).filter_by(email = flask.request.form.get('email')).first()
        if not user:
            error = 'This email doesn\'t exist please try again'
            
        elif check_password_hash(user.password, flask.request.form.get('password')):
            session.close()
            flask_login.login_user(user)
            return flask.redirect(flask.url_for('secrets'))
        
        else:
            error = 'Password isn\'t correct'
            
        return flask.render_template('login.html', error = error, form = form)

    return flask.render_template("login.html", form = form)


@app.route('/secrets')
@flask_login.login_required
def secrets():
    return flask.render_template("secrets.html", name = flask_login.current_user.name)


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for('home'))


@app.route('/download', methods = ['GET', 'POST'])
@flask_login.login_required
def download():
    if flask.request.method == 'GET':
        return flask.send_file('./static/files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug = True)
