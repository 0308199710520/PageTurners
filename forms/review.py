from wtforms import StringField, SelectField
from flask_wtf import FlaskForm
class ReviewForm(FlaskForm):
    title = StringField("What is your books title")
    author = StringField("Who Wrote this book")
    rating = SelectField("What do you rate it", choice=[1,2,3,4,5])