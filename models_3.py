from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    group = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    grades = db.relationship('Grade', backref='student')

    def __repr__(self) -> str:
        return f'Student({self.name}, {self.last_name}, \
{self.group}, {self.email})'

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    discipline_name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f'Grade({self.student_id}, {self.discipline_name}, \
{self.grade})'

    def __str__(self) -> str:
        return f'{self.discipline_name}: {self.grade}'
