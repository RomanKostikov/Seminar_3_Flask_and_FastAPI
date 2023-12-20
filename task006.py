# Задание №6
# Дополняем прошлую задачу
# Создайте форму для регистрации пользователей в вашем
# веб-приложении.
# Форма должна содержать следующие поля: имя
# пользователя, электронная почта, пароль и подтверждение
# пароля.
# Все поля обязательны для заполнения, и электронная почта
# должна быть валидным адресом.
# После отправки формы, выведите успешное сообщение об
# успешной регистрации.

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from forms_6 import SingUpForm

app = Flask(__name__)
# Example secret key. REPLACE IT WITH REAL SECRET KEY
app.config['SECRET_KEY'] = '3aa6d8a359ff3cf7f0eac295629748935cb45a059e392cc9f2a8e8fe9ac04c9f'
csrf = CSRFProtect(app)
"""
Генерация токена
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SingUpForm()
    form_notifications = []
    if request.method == 'POST' and form.validate():
        username = form.name.data
        email = form.email.data
        form_notifications.append(
            f'User {username}({email}) successfully registered!'
        )
        return render_template(
            'task004.html', form=form, form_notifications=form_notifications
        )
    return render_template('task004.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
