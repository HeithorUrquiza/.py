#Lidando com Banco de Dados
#import sqlite3

#db = sqlite3.connect("Revision/SQLite/book-collection.db")
#cursor = db.cursor()
#cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

#cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
#db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\Users\\heith\\Documents\\GitHub\\.py\\Revision\\SQLite\\new-books-collection.db"
# initialize the app with the extension
db.init_app(app)

##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()
    
""" with app.app_context():
    book = Book(id=1, title="Harry Potter", author="J.K.Rowling", rating=9.3)
    db.session.add(book)
    db.session.commit() """
    
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    #print(result.all())
    all_books = result.scalars().all()
   
    print(all_books)
    
    for item in all_books:
        print(item)