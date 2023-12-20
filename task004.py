# Задание №4
# Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
# содержать следующие поля:
# ○ Имя пользователя (обязательное поле)
# ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
# ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
# ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
# и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
# заполнено или данные не прошли валидацию, то должно выводиться соответствующее
# сообщение об ошибке.
# Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
# базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
# об ошибке.

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from forms_4 import SingUpForm
from models_4 import db, User

app = Flask(__name__)
# Example secret key. REPLACE IT WITH REAL SECRET KEY
app.config['SECRET_KEY'] = '3aa6d8a359ff3cf7f0eac295629748935cb45a059e392cc9f2a8e8fe9ac04c9f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///4.sqlite'
db.init_app(app)
csrf = CSRFProtect(app)
"""
Генерация токена
>>> import secrets
>>> secrets.token_hex()
"""


def add_user(username, email, password):
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SingUpForm()
    form_errors = []
    if request.method == 'POST' and form.validate():
        username = form.name.data
        email = form.email.data
        if User.query.filter(User.username == username).count() > 0:
            form_errors.append(f'Username {username} already taken!')
        if User.query.filter(User.email == email).count() > 0:
            form_errors.append(f'Email {email} already taken!')
        else:
            print(f'Adding user {username}!')
            add_user(username, form.email.data, form.password.data)
            form_notifications = [f'User {username} successfully registered!']
            return render_template(
                'task004.html', form=form, form_notifications=form_notifications
            )
    return render_template('task004.html', form=form, form_errors=form_errors)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Database created successfully!')


if __name__ == '__main__':
    app.run(debug=True)
