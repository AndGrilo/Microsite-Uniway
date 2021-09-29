from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Length, DataRequired, Email
from micro.models import User, Amigo

class RegisterForm(FlaskForm):
    nome = StringField(label='Nome Completo*', validators=[Length(min=3, max=60), DataRequired()])
    data_de_nascimento = StringField(label='Data de Nascimento*', validators=[Length(min=6, max=10), DataRequired()])
    nif = IntegerField(label='Número de Contribuinte*', validators=[DataRequired()])
    morada = StringField(label='Morada*', validators=[Length(min=5, max=60), DataRequired()])
    codigo_postal = StringField(label='Código Postal*', validators=[Length(min=6, max=8), DataRequired()])
    localidade = StringField(label='Localidade')
    email = StringField(label='Email')
    submit = SubmitField(label='Submeter')

class IndicaForm(FlaskForm):
    sim = SubmitField(label='Sim')
    nao = SubmitField(label="Não")

class NaoIndicaForm(FlaskForm):
    nao = SubmitField(label="Não")

class AmigoForm(FlaskForm):
    nome = StringField(label='Nome*', validators=[Length(min=2, max=60), DataRequired()])
    telemovel = IntegerField(label='Telemóvel*', validators=[DataRequired()])
    email = StringField(label='Email')
    submit = SubmitField(label='Submeter')