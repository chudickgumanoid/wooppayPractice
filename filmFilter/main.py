import pandas as pd

from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = '099'
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/')
def indexx():
    return render_template('index.html')


@app.route('/app')
def cbox():
    return render_template('login.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.id.desc()).all()
    return render_template('posts.html', articles=articles)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')

    if login and password in db:
        return render_template('success.html')
    else:
        return 'uncorrect'


@app.route('/add', methods=['POST', 'GET'])
def addlp():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        article = Article(login=login, password=password)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except:
            return 'Данные при вводе неверны'
    else:
        return render_template('add.html')

    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)


