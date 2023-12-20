# Задание №1
# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
# возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название
# факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их факультета.

from flask import Flask, render_template
from models_1 import db, Student, Faculty
from faker import Faker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db.init_app(app)
fake = Faker('ru_RU')


@app.route('/')
def index():
    students = Student.query.all()
    context = {
        'students': students
    }
    return render_template('index.html', **context)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('База данных создана')


@app.cli.command('fill-db')
def fill_db():
    for i in range(5):
        faculty = Faculty(faculty_name=f'Faculty {i + 1}')
        db.session.add(faculty)
        for _ in range(3):
            student = Student(
                name=fake.first_name(),
                surname=fake.last_name(),
                age=fake.random_int(min=18, max=100),
                gender=fake.random_element(elements=('male', 'female')),
                group=fake.random_int(min=1, max=10),
                faculty=faculty
            )
            db.session.add(student)
    db.session.commit()
    print('База данных заполнена')


if __name__ == '__main__':
    app.run(debug=True)
