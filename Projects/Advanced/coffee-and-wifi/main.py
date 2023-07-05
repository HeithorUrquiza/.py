from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
import csv
import os

app = Flask(__name__)
secret_key = os.urandom(24).hex()
app.config['SECRET_KEY'] = secret_key
bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired(message="Field is required")])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(message="Field is required"), URL(require_tld=False)])
    open_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired(message="Field is required")])
    close_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired(message="Field is required")])
    cf_rating = StringField('Coffee Rating (0-5)', validators=[DataRequired(message="Field is required")])
    wf_rating = StringField('Wifi Strength Rating (0-5)', validators=[DataRequired(message="Field is required")])
    pw = StringField('Power Socket Availability (0-5)', validators=[DataRequired(message="Field is required")])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    if form.validate_on_submit():
        print("True")
        with open('Projects\Advanced\coffee-and-wifi\cafe-data.csv', mode="a", newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([
                f"{form.cafe.data}", 
                f"{form.location.data}",
                f"{form.open_time.data}",
                f"{form.close_time.data}",
                f"{form.cf_rating.data}",
                f"{form.wf_rating.data}",
                f"{form.pw.data}"])
            return render_template('add.html', form=form, sent=True)
    return render_template('add.html', form=form, sent=False)


@app.route('/cafes')
def cafes():
    with open('Projects\Advanced\coffee-and-wifi\cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_row = [row for row in csv_data]
    return render_template('cafes.html', cafes=list_of_row)


if __name__ == '__main__':
    app.run(debug=True)
