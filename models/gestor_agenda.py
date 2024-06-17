from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String

db = SQLAlchemy()


class tb_telefonos(db.Model):
    __tablename__ = "telefonos"
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer)
    telefono = db.Column(String(20))
    tipo = db.Column(String(20))

    def __init__(self, usuario_id, telefono, tipo):
        self.usuario_id = usuario_id
        self.telefono = telefono
        self.tipo = tipo


class tb_usuarios(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(String(50))
    apellido = db.Column(String(50))
    apodo = db.Column(String(50))

    def __init__(self, nombre, apellido, apodo):
        self.nombre = nombre
        self.apellido = apellido
        self.apodo = apodo
