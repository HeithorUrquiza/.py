from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:\\Users\\heith\\Documents\\GitHub\\.py\\Projects\\Advanced\\library-site\\books-collection.db"
db = SQLAlchemy()
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = Book(
            title = request.form["bookname"],
            author = request.form["author"],
            rating = request.form["rating"]
        )
        db.session.add(book)
        db.session.commit()
        #NOTE: You can use the redirect method from flask to redirect to another route 
        # e.g. in this case to the home page after the form has been submitted.
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit", methods = ["GET", "POST"])
def edit():
    book_id = request.args.get('id')
    book_to_update = db.get_or_404(Book, book_id)
    if request.method == "POST": 
        book_to_update.rating = request.form["newrating"]
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', book=book_to_update)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

