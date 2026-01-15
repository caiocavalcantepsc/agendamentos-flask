from estudo import db, login_manager
from datetime import datetime
from flask_login import UserMixin 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin ):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable = True)
    sobrenome = db.Column(db.String(100), nullable = True)
    email = db.Column(db.String(100), nullable = True)
    senha = db.Column(db.String(100), nullable = True)


class Contato(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data_envio = db.Column(db.DateTime, default=datetime.utcnow())
    nome = db.Column(db.String(100), nullable = True)
    email = db.Column(db.String(100), nullable = True)
    assunto = db.Column(db.String(100), nullable = True)
    mensagem = db.Column(db.String(100), nullable = True)
