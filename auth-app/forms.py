from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    IntegerField,
    DateField,
    TextAreaField,
)

from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, EqualTo, Email, Regexp ,Optional
import email_validator
from flask_login import current_user
from wtforms import ValidationError,validators
from models import User


class login_form(FlaskForm):
    username = StringField(validators=[InputRequired()])
    pwd = PasswordField(validators=[InputRequired(), Length(min=8, max=72)])
    phone = StringField(validators=[InputRequired()])



class register_form(FlaskForm):
    username = StringField(
        validators=[
            InputRequired(),
            Length(3, 20, message="Пожалуйста, выберите допустимое имя (как минимум из трёх символов)"),
            Regexp(
                "^[A-Za-z0-9_.]*$",
                0,
                "Имя пользователя должно содержать только латинские буквы, " "цифры, точки или знаки подчеркивания",
            ),
        ]
    )
    pwd = PasswordField(validators=[InputRequired(), Length(8, 72)])
    cpwd = PasswordField(

        validators=[
            InputRequired(),
            Length(8, 72),
            EqualTo("pwd", message="Пароли должны совпадать"),
        ]
    )
    phone = StringField(validators=[InputRequired(message='Телефон, к которому привязан аккаунт Telegram.')])


    def validate_uname(self, uname):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError("Это имя пользователя уже занято")