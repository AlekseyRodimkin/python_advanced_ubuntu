"""
Довольно неудобно использовать встроенный валидатор NumberRange для ограничения числа по его длине.
Создадим свой для поля phone. Создайте валидатор обоими способами.
Валидатор должен принимать на вход параметры min и max — минимальная и максимальная длина,
а также опциональный параметр message (см. рекомендации к предыдущему заданию).
"""
from typing import Optional

from flask_wtf import FlaskForm
from wtforms import Field, IntegerField, StringField
from wtforms.validators import ValidationError, InputRequired


def number_length(min: int, max: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        if not min < len(str(field)) < max:
            raise ValidationError(message=message)

    return _number_length


number = IntegerField(validators=[InputRequired(), number_length])


class NumberLength:
    def __init__(self, min: int, max: int, message: Optional[str] = None):
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        if not self.min < len(str(field)) < self.max:
            raise ValidationError(message=self.message)


number_2 = IntegerField(validators=[InputRequired(), NumberLength()])

