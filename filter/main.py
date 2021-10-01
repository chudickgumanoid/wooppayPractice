from flask import Flask, render_template, url_for, request, flash, session, redirect, abort


#экземпляр класса с аргументом ввиде имени
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'aboba228'


#для отображения менюшки
menu = [{"name": "Главная", "url": "/"},
        {"name": "Авторизация", "url": "login"},
        {"name": "Обратная связь", "url": "contact"},
        {"name": "О сайте", "url": "about"}]


#обработчик главной страницы
@app.route("/")
def index():
    print(url_for('index'))
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
            flash('Сообщение отправлено!! только куда..', category='success')
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