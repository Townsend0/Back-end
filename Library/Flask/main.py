import flask
from forms import *
from mysql import connector
from database import *
from sqlalchemy.exc import ProgrammingError


mysql = connector.connect(host = 'localhost', user = 'root', password = 'Ksfaq137')

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'eldorjebfoenf;wekjlefjiop'

all_books = []


@app.route('/')
def home():
    forms = AddBooks()
    try:
        return flask.render_template('index.html', all_books = database_data(), forms = forms)
    except ProgrammingError:
        return flask.render_template('index.html', all_books = [], forms = forms)
        

@app.route("/add", methods = ['GET', 'POST'])
def add():
    forms = AddBooks()
    if forms.validate_on_submit():
        add_to_database(forms.name.data, forms.author.data, forms.rating.data)
        return flask.redirect(flask.url_for('home'))
    return flask.render_template('add.html', forms = forms)


if __name__ == "__main__":
    app.run(debug=True)

