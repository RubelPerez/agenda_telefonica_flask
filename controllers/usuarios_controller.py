from flask import jsonify
from models.gestor_agenda import db
from models.gestor_agenda import tb_usuarios


def show_all_users():
    "select * from usuarios"
    data = []
    usuarios = tb_usuarios.query.all()
    for usuario in usuarios:
        data.append({
            "id": usuario.id,
            "nombre": usuario.nombre,
            "apellido": usuario.apellido,
            "apodo": usuario.apodo,
        })
    return jsonify(data)


def get_user_id(id):
    "select * from usuarios where id = id"
    data = []
    usuarios = tb_usuarios.query.filter_by(id=id).all()
    for usuario in usuarios:
        data.append({
            "id": usuario.id,
            "nombre": usuario.nombre,
            "apellido": usuario.apellido,
            "apodo": usuario.apodo,
        })
    return jsonify(data)


def store_register(new_data):
    "insert into usuarios (nombre,apellido, apodo) values (new_data.nombre,new_data.apellido,new_data.apodo)"
    nombre = new_data['nombre']
    apellido = new_data['apellido']
    apodo = new_data['apodo']
    try:
        usuario = tb_usuarios(nombre, apellido, apodo)
        db.session.add(usuario)
        db.session.commit()
        return "data inserted", 200
    except Exception as ex:
        db.session.rollback()
        return f"Error inserting data {ex}", 401


def updated_data(data_to_update):
    "update usuarios set [campo a modificar] = [valores a modificar] where id = id"
    try:
        id = data_to_update['id']
        usuario = tb_usuarios.query.filter_by(id=id).first()
        usuario.nombre = data_to_update['nombre']
        usuario.apellido = data_to_update['apellido']
        usuario.apodo = data_to_update['apodo']
        db.session.merge(usuario)
        db.session.flush()
        db.session.commit()
        return "Actualizacion realizada correctamente"
    except Exception as ex:
        db.session.rollback()
        return f"Error tratando de actualizar: {ex}"


def deleted_data(data_to_delete):
    "update usuarios set [campo a modificar] = [valores a modificar] where id = id"
    try:
        id = data_to_delete['id']
        usuario = tb_usuarios.query.filter_by(id=id).first()
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return "Eliminado realizado correctamente"
        else:
            return f"no fue encontrado nadie con el ID: {id}"
    except Exception as ex:
        db.session.rollback()
        return f"Error tratando de Eliminar: {ex}"
