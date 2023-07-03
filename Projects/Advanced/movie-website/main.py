from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import requests
import os

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
Bootstrap5(app)

# Create DB
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:\\Users\\heith\\Documents\\GitHub\\.py\\Projects\\Advanced\\movie-website\\movies.db"
db = SQLAlchemy()
db.init_app(app)

search_url = "https://api.themoviedb.org/3/search/movie"
details_url = "https://api.themoviedb.org/3/movie/"

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)
    
with app.app_context():
    db.create_all()
    
    
class RateMovieForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 (e.g: 75)', validators=[DataRequired(message='Field is required')])
    review = StringField('Your Review', validators=[DataRequired(message='Field is required')])
    submit = SubmitField('Done')
    
    
class AddMovie(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired(message="Field is required")])
    submit = SubmitField('Add Movie')


@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = movies.scalars().all()
    
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    movie_id = request.args.get('id')
    movie_to_update = db.get_or_404(Movie, movie_id)
    form = RateMovieForm()
    if form.validate_on_submit():
        print("Form sent!!")
        # Att Rating and Review from movie
        movie_to_update.rating = float(form.rating.data)
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, movie=movie_to_update)


@app.route("/delete")
def delete():
    move_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, move_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        # Search for a film using API
        params = {"api_key": os.getenv("API_KEY"), "query": form.title.data}
        resp = requests.get(url=search_url, params=params)
        data = resp.json()["results"]
        return render_template('select.html', data=data)
    return render_template('add.html', form=form)


@app.route("/find")
def find_movie():
    # Find details of a movie with its id
    movie_id = request.args.get('id')
    if movie_id:
        params = {"api_key": os.getenv("API_KEY")}
        resp = requests.get(url=f"{details_url}{movie_id}", params=params)
        data = resp.json()
        
        # Create a new record
        new_movie = Movie(
            title=data["title"], 
            year=data["release_date"].split("-")[0], 
            description=data["overview"], 
            rating = 0.0,
            ranking = 0,
            review = "None",
            img_url=f"https://image.tmdb.org/t/p/original{data['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', id=new_movie.id))
    

if __name__ == '__main__':
    app.run(debug=True)