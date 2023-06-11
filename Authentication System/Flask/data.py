import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
import flask_login


engine = sqlalchemy.create_engine('sqlite:///users.db')
Session = sessionmaker(engine)
Base = declarative_base()


class User(Base, flask_login.UserMixin):
    __tablename__ = 'user'
    
    id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key = True)
    email = sqlalchemy.Column(sqlalchemy.String(100), unique = True)
    password = sqlalchemy.Column(sqlalchemy.String(100))
    name = sqlalchemy.Column(sqlalchemy.String(100))
    
    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name
        
    
Base.metadata.create_all(engine)

