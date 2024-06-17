from flask import Blueprint, request

from controllers.telefonos_controller import show_all_phones, get_phone_id, store_register, updated_data, deleted_data

telefonos_bp = Blueprint('telefonos', __name__)


@telefonos_bp.route("/")
def index():
    return show_all_phones()


@telefonos_bp.route("/<int:id>")
def get_phone_by_id(id):
    return get_phone_id(id)


@telefonos_bp.route("/", methods=['POST'])
def store_data():
    new_data = request.get_json()
    return store_register(new_data)


@telefonos_bp.route("/", methods=['PUT'])
def update_data():
    data_to_update = request.get_json()
    return updated_data(data_to_update)


@telefonos_bp.route("/", methods=['DELETE'])
def delete_data():
    data_to_delete = request.get_json()
    return deleted_data(data_to_delete)
