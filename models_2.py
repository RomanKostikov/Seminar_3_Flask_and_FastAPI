from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    books = db.relationship('Book', backref='author')

    def __repr__(self) -> str:
        return f'Author({self.name}, {self.last_name})'

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    release_year = db.Column(
        db.Integer, nullable=False, default=datetime.now().year
    )
    copies = db.Column(db.Integer, nullable=False)
    author_id = db.Column(
        db.Integer, db.ForeignKey('author.id'), nullable=False
    )

    def __repr__(self) -> str:
        return f'Book({self.name}, {self.release_year}, \
{self.copies}, {self.author_id})'
