import flask
from sqlalchemy.orm import declarative_base, sessionmaker
import sqlalchemy
from random import randint


app = flask.Flask(__name__)

engine = sqlalchemy.create_engine('sqlite:///cafes.db')
Base = declarative_base()
Session = sessionmaker(engine)

class Cafe(Base):
    __tablename__ = 'Cafe'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(250), unique=True, nullable=False)
    map_url = sqlalchemy.Column(sqlalchemy.String(500), nullable=False)
    img_url = sqlalchemy.Column(sqlalchemy.String(500), nullable=False)
    location = sqlalchemy.Column(sqlalchemy.String(250), nullable=False)
    seats = sqlalchemy.Column(sqlalchemy.String(250), nullable=False)
    has_toilet = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)
    has_wifi = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)
    has_sockets = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)
    can_take_calls = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)
    coffee_price = sqlalchemy.Column(sqlalchemy.String(250), nullable=True)
    
    def __init__(self, name, map_url, img_url, location, seats, has_toilets, has_wifi, has_sockets, can_take_calls, coffee_price):
        self.name = name
        self.map_url = map_url
        self.img_url = img_url
        self.location = location
        self.seats = seats
        self.has_toilet = has_toilets
        self.has_wifi = has_wifi
        self.has_sockets = has_sockets
        self.can_take_calls = can_take_calls
        self.coffee_price = coffee_price
    

Base.metadata.create_all(engine)

def todict(a):
    c = dict()
    
    for b in range(len(a)):
        c[b + 1] = { 'name': a[b].name, 'map_url': a[b].map_url, 'img_url': a[b].img_url, 'location': a[b].location,
        'seats': a[b].seats, 'has_toilet': a[b].has_toilet, 'haswifi': a[b].has_wifi, 'has_sockets': a[b].has_sockets,
        'can_take_call': a[b].can_take_calls, 'coffe_price': a[b].coffee_price}
    
    return c


@app.route("/")
def home():
    return flask.render_template("index.html")
    
@app.route('/random')
def get_random():
    session = Session()
    cafe = session.query(Cafe).filter_by(id = randint(1,21)).all()
    session.close()
    return flask.jsonify(todict(cafe))
        
        
@app.route('/all')
def get_all():
    session = Session()
    a = session.query(Cafe).all()
    session.close()
    return flask.jsonify(todict(a))


@app.route('/search')
def search():
    location = flask.request.args.get('location')
    session = Session()
    a = session.query(Cafe).filter_by(location = location).all()
    session.close()
    if a:
        return flask.jsonify(Cafe = todict(a))
    return flask.jsonify(error = {'Not Found': 'Sorry, we dont have a cafe at that location'})
    
    
@app.route('/add', methods = ['GET', 'POST'])
def add():
    session = Session()
    session.add(Cafe(flask.request.form.get('name'), flask.request.form.get('map_url'),
    flask.request.form.get('img_url'), flask.request.form.get('location'),
    flask.request.form.get('seats'), bool(flask.request.form.get('has_toilet')), 
    bool(flask.request.form.get('has_wifi')), bool(flask.request.form.get('has_sockets')), 
    bool(flask.request.form.get('can_take_calls')), flask.request.form.get('coffee_prices')))
    session.commit()
    session.close()
    return flask.jsonify(response = {'success': 'Successfully added the new cafe'})


@app.route('/edit_price/<int:cafe_id>', methods = ['PATCH', 'GET'])
def edit_price(cafe_id):
    session = Session()
    a = session.query(Cafe).filter_by(id = cafe_id).first()
    if a:
        a.coffee_price = flask.request.args.get('updated_price')
        session.commit()
        session.close()
        return flask.jsonify(response = { 'success': 'Successfully changed the price'})
    return flask.jsonify(error = {'Not Found': 'Sorry a cafe with that id wasn\'t found in the data base'})


@app.route('/delete-cafe/<int:cafe_id>', methods = ['DELETE'])
def delete_cafe(cafe_id):
    if flask.request.args.get('api_key') == 'pass123$':
        session = Session()
        a = session.query(Cafe).filter_by(id = cafe_id).first()
        if a:
            session.delete(a)
            session.commit()
            session.close()
            return flask.jsonify(response = {'succes': 'Successfully delete the cafe'})
        return flask.jsonify(error = {'Not Found': 'Sorry a cafe with that id wasn\'t found in the data base'})    
    return flask.jsonify(error = {'error': 'Sorry you are not authorized to delete cafes'})


if __name__ == '__main__':
    app.run(debug=True)
