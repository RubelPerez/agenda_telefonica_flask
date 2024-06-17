from flask import Flask
from flask_migrate import Migrate

from models.gestor_agenda import db
from routes.telefonos_route import telefonos_bp
from routes.usuarios_route import usuarios_bp

app = Flask(__name__)
app.config.from_object("config")
db.init_app(app)
db.app = app
migrate = Migrate(app, db)

app.register_blueprint(usuarios_bp, url_prefix="/api/usuarios")
app.register_blueprint(telefonos_bp, url_prefix="/api/telefonos")

if __name__ == '__main__':
    app.run(DEBUG=True, env="development")
