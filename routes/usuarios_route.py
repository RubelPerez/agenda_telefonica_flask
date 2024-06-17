from flask import Blueprint, request

from controllers.usuarios_controller import show_all_users, get_user_id, store_register, updated_data, deleted_data

usuarios_bp = Blueprint('usuarios', __name__)


@usuarios_bp.route("/")
def index():
    return show_all_users()


@usuarios_bp.route("/<int:id>")
def get_user_by_id(id):
    return get_user_id(id)


@usuarios_bp.route("/", methods=['POST'])
def store_data():
    new_data = request.get_json()
    return store_register(new_data)

@usuarios_bp.route("/", methods=['PUT'])
def update_data():
    data_to_update = request.get_json()
    return updated_data(data_to_update)

@usuarios_bp.route("/", methods=['DELETE'])
def delete_data():
    data_to_delete = request.get_json()
    return deleted_data(data_to_delete)
