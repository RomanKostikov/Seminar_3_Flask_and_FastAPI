# Задание №7
# Создайте форму регистрации пользователей в приложении Flask. Форма должна
# содержать поля: имя, фамилия, email, пароль и подтверждение пароля. При отправке
# формы данные должны валидироваться на следующие условия:
# ○ Все поля обязательны для заполнения.
# ○ Поле email должно быть валидным email адресом.
# ○ Поле пароль должно содержать не менее 8 символов, включая хотя бы одну букву и
# одну цифру.
# ○ Поле подтверждения пароля должно совпадать с полем пароля.
# ○ Если данные формы не прошли валидацию, на странице должна быть выведена
# соответствующая ошибка.
# ○ Если данные формы прошли валидацию, на странице должно быть выведено
# сообщение об успешной регистрации.

from string import ascii_lowercase
from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from forms_7 import SingUpForm

app = Flask(__name__)
# Example secret key. REPLACE IT WITH REAL SECRET KEY
app.config['SECRET_KEY'] = '3aa6d8a359ff3cf7f0eac295629748935cb45a059e392cc9f2a8e8fe9ac04c9f'
csrf = CSRFProtect(app)
"""
Генерация токена
>>> import secrets
>>> secrets.token_hex()
"""


def validate_password(password: str) -> bool:
    has_letters = False
    has_digits = False
    for character in password.lower():
        if character in ascii_lowercase:
            has_letters = True
        if character.isdigit():
            has_digits = True

    if has_letters and has_digits:
        return True
    return False


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SingUpForm()
    form_notifications = []
    form_errors = []
    if request.method == 'POST' and form.validate():
        name = form.name.data
        last_name = form.last_name.data
        password = form.password.data
        if validate_password(password):
            form_notifications.append(
                f'User {name} {last_name} successfully registered!'
            )
        else:
            form.password.errors.append(
                'Password must contain at least one letter and one digit'
            )
    return render_template(
        'task004.html',
        form=form,
        form_errors=form_errors,
        form_notifications=form_notifications,
    )


if __name__ == '__main__':
    app.run(debug=True)
