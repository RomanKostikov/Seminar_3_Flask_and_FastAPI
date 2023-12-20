# Задание №3
# Доработаем задачу про студентов
# Создать базу данных для хранения информации о студентах и их оценках в
# учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
# и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название
# предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их оценок.

from faker import Faker
from flask import Flask, render_template
from random import choice, randint

from models_3 import db, Student, Grade


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///3.sqlite'
db.init_app(app)
fake = Faker('ru-RU')


@app.route('/')
def index():
    students = Student.query.all()
    context = {'students': students}
    return render_template('task003.html', **context)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Database created successfully!')


@app.cli.command('fill-db')
def fill_db():
    disciplines = [
        'Математика',
        'Физика',
        'Информатика и программирование',
        'Английский язык',
        'Физическая культура',
    ]
    groups = ['Е-333', 'Е-334']
    for _ in range(10):
        student = Student(
            name=fake.first_name(),
            last_name=fake.last_name(),
            group=choice(groups),
            email=fake.safe_email(),
        )
        db.session.add(student)
        print(f'Created student: {student}')

        for _ in range(20):
            grade = Grade(
                student=student,
                discipline_name=choice(disciplines),
                grade=randint(2, 5),
            )
            db.session.add(grade)

        print(f'Filled grades for student: {student}')

    db.session.commit()
    print('Database filled successfully!')


if __name__ == '__main__':
    app.run(debug=True)
