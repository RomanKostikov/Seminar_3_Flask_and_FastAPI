from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class SingUpForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired(), Length(min=4)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6)]
    )
    password_confirmation = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')]
    )
