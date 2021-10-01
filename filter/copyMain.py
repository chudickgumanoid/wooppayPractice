from flask import Flask, render_template, url_for, request, flash, session, redirect, abort
import sqlite3
import os
#http://127.0.0.1:5000/
#конфигурационная инфа
DATABASE = '/tmp/mainbd.db'
DEBUG = True
SECRET_KEY = 'abobus'

#экземпляр класса с аргументом ввиде имени
app = Flask(__name__)
app.config.from_object(__name__)
#переопределение пути
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'mainbd.db')))
#app.config['SECRET_KEY'] = 'aboba228'


#для отображения менюшки
menu = [{"name": "Главная", "url": "/"},
        {"name": "Авторизация", "url": "autorization"},
        {"name": "Обратная связь", "url": "contact"},
        {"name": "О сайте", "url": "about"}]


#обработчик главной страницы
@app.route("/")
def index():
    print( url_for('index') )
    return render_template('index.html', menu = menu)


#обработчик странички about
@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title = 'О сайте', menu = menu)


#обработчик странички contact
@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        # проверка формы, если в поле больше 2х символов
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено!!', category='success')
        else:
            flash('Ошибка отправки', category='error')

    return render_template('contact.html', title = 'Обратная связь', menu = menu)


#декоратор ошибки сервера
@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title='Ой! Страница не найдена...', menu=menu), 404


#обработчик для login
@app.route("/login", methods=["POST", "GET"])
def login():
    #проверяем свойство userLogged и делаем переадресацию
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "amogus" and request.form['psw'] == "123":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title="Авторизация", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)

    return f"Профиль пользователя: {username}"


#для запуска локалки
if __name__ == "__main__":
    app.run(debug=True)

















"""
import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort

#конфигурационная инфа
DATABASE = '/tmp/main.db'
DEBUG = True
SECRET_KEY = 'abobus'

#экземпляр класса с аргументом ввиде имени
app = Flask(__name__)
app.config.from_object(__name__)
#переопределение пути
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'main.db')))


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

#для запуска локалки
#if __name__ == "__main__":
#    app.run(debug=True)
"""