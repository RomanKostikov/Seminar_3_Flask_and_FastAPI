# Задание №2
# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.

from random import randint
from flask import Flask, render_template
from models_2 import db, Author, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.sqlite'
db.init_app(app)


@app.route('/')
def index():
    books = Book.query.all()
    context = {
        'books': books
    }
    return render_template('books.html', **context)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Created DB!')


@app.cli.command('fill-db')
def fill_db():
    for i in range(5):
        author = Author(name=f'Name {i}', last_name=f'Last Name {i}')
        db.session.add(author)
        for j in range(4):
            book = Book(
                name=f'Name {j}-{i}',
                release_year=randint(1900, 2023),
                copies=randint(10_000, 100_000),
                author=author
            )
            db.session.add(book)
    db.session.commit()
    print('DB Filled!')


if __name__ == '__main__':
    app.run(debug=True)
