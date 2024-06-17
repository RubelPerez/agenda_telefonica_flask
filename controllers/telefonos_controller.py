from flask import jsonify
from models.gestor_agenda import db
from models.gestor_agenda import tb_telefonos


def show_all_phones():
    "select * from telefonos"
    data = []
    telefonos = tb_telefonos.query.all()
    for telefono in telefonos:
        data.append({
            "id": telefono.id,
            "usuario_id": telefono.usuario_id,
            "telefono": telefono.telefono,
            "tipo": telefono.tipo,
        })
    return jsonify(data)


def get_phone_id(id):
    "select * from telefonos where id = id"
    data = []
    telefonos = tb_telefonos.query.filter_by(id=id).all()
    for telefono in telefonos:
        data.append({
            "id": telefono.id,
            "usuario_id": telefono.usuario_id,
            "telefono": telefono.telefono,
            "tipo": telefono.tipo,
        })
    return jsonify(data)


def store_register(new_data):
    "insert into telefonos (usuario_id,telefono, tipo) values (new_data.usuario_id,new_data.telefono,new_data.tipo)"
    usuario_id = new_data['usuario_id']
    telefono = new_data['telefono']
    tipo = new_data['tipo']
    try:
        telefonos = tb_telefonos(usuario_id, telefono, tipo)
        db.session.add(telefonos)
        db.session.commit()
        return "data inserted", 200
    except Exception as ex:
        db.session.rollback()
        return f"Error inserting data {ex}", 401


def updated_data(data_to_update):
    "update telefono set [campo a modificar] = [valores a modificar] where id = id"
    try:
        id = data_to_update['id']
        telefono = tb_telefonos.query.filter_by(id=id).first()
        telefono.usuario_id = data_to_update['usuario_id']
        telefono.telefono = data_to_update['telefono']
        telefono.tipo = data_to_update['tipo']
        db.session.merge(telefono)
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
        usuario = tb_telefonos.query.filter_by(id=id).first()
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return "Eliminado realizado correctamente"
        else:
            return f"no fue encontrado nadie con el ID: {id}"
    except Exception as ex:
        db.session.rollback()
        return f"Error tratando de Eliminar: {ex}"
