import sqlite3
import os
from wsgiref.simple_server import WSGIServer

from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g

#конфигурационная инфа
DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'abobus'

#экземпляр класса с аргументом ввиде имени
app = Flask(__name__)
app.config.from_object(__name__)
#переопределение пути
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))


#общая функция для соединения с БД
def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


#создает БД без запуска веб сервера
def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


#связь с бд если она ещё не установилась
def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    return render_template('index.html', menu = [])

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

#для запуска локалки
if __name__ == "__main__":
    app.run(debug=True)