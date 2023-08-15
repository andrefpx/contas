from api import db

class Conta(db.Model):
    __tablename__= 'Conta'
    id = db.Column(db.Integer,primary_key=True,autoincrement=true,nullable=False)
    nome = db.Column(db.String(50),nullable=False)
    resumo = db.Column(db.String(100),nullable=False)
    valor = db.Columns(db.Float, nullable=False)