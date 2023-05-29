import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

def add_to_database(name, author, rating):
    engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:Ksfaq137@localhost/Books')
    Session = sessionmaker(engine)

    class BooksData(Base):
        __tablename__ = 'booksdata'
        number = sqlalchemy.Column('id', sqlalchemy.Integer(), primary_key = True)
        name = sqlalchemy.Column('name', sqlalchemy.String(25))
        author = sqlalchemy.Column('author', sqlalchemy.String(50))
        rating = sqlalchemy.Column('rating', sqlalchemy.Integer)
        
        def __init__(self, name, author, rating):
            self.name = name
            self.author = author
            self.rating = rating
        
    Base.metadata.create_all(engine)
    new_user = BooksData(name, author, rating)
    session = Session()
    session.add(new_user)
    session.commit()
    session.close()

def database_data():
    engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:Ksfaq137@localhost/Books')
    Session = sessionmaker(engine)
    session = Session()
    return session.execute(sqlalchemy.text("SELECT * FROM books.booksdata"))