from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail


app = Flask(__name__)


ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Sandymacob05!@localhost/flaskday'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    weekday = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text(), nullable=False)

    def __init__(self, name, weekday, rating, comments):
        self.name = name
        self.weekday = weekday
        self.rating = rating
        self.comments = comments


@app. route ('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        weekday = request.form['weekday']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(name, weekday, rating, comments)
        if name == '' or weekday == '':
            return render_template('index.html', message='Please enter required fields')
        if db.session.query(Feedback).filter(Feedback.name == name).count() == 0:
            data = Feedback(name, weekday, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(name, weekday, rating, comments)
            return render_template('success.html')
        #return render_template('index.html', message='You have already submitted feedback')
        return render_template('success.html')


@app.route('/success')
def success():
    
    return render_template('success.html')


if __name__ == '__main__':
    app.run()
