from micro import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(length=60), nullable=False)
    data_de_nascimento = db.Column(db.String(length=10), nullable=False)
    nif = db.Column(db.Integer(), nullable=False)
    morada = db.Column(db.String(length=60), nullable = False)
    codigo_postal = db.Column(db.String(length=8), nullable=False)
    localidade = db.Column(db.String(length=30), nullable=False)
    email = db.Column(db.String(length=60), nullable=False)
    marketing = db.Column(db.String(length=4), nullable=False)

class Amigo(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(length=60), nullable=False)
    telemovel = db.Column(db.Integer(), nullable = False)
    email = db.Column(db.String(length=60), nullable=False)