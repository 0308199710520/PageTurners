from flask import Flask,Blueprint, render_template
from forms.review import ReviewForm, ReviewForm
app = Flask(__name__)

@app.route("/", methods=("GET", "POST"))
def index():
    books = None #HERE WILL BE THE DATABASE LOOKUP
    return render_template('index.html', books=books)

def sign_in():

    if request.method=="POST":
        username=form.username.data
        password=form.password.data
        if verification(username, password):
            g.user = user
        


    

