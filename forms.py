from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

class RegistrationForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    membership_type = SelectField('Тип абонемента', choices=[
        ('Normal', 'Normal'),
        ('Normal+', 'Normal+'),
        ('VIP', 'VIP'),
        ('VIP+', 'VIP+'),
        ('Unlim', 'Unlim')
    ])
    submit = SubmitField('Зарегистрироваться')
