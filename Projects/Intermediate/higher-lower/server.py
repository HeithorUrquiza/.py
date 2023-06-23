from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def root_page():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>'\
            '<img style="display: block; margin-left: auto; margin-right: auto;" src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'
            
            
rand_num = random.randint(0, 9)
@app.route("/<int:num>")
def guess_number(num):
    if num > rand_num:
        return '<h1 style="color: orange; text-align: center">It\'s too high! Try again...</h1>' \
                '<img style="display: block; margin-left: auto; margin-right: auto;" src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif num < rand_num:
        return '<h1 style="color: red; text-align: center">It\'s too low! Try again...</h1>'\
                '<img style="display: block; margin-left: auto; margin-right: auto;" src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<h1 style="color: green; text-align: center">You founded!!</h1>'\
                '<img style="display: block; margin-left: auto; margin-right: auto;" src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=1)