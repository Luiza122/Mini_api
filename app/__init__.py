from flask import Flask, jsonify
from .core.extensions import db, api
from .core.config import Config
from .routes.users import blp as UsersBlueprint

def create_app(config_object: type[Config] = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object)

    # init extensions
    db.init_app(app)
    api.init_app(app)

    # register blueprints
    api.register_blueprint(UsersBlueprint)

    # healthcheck
    @app.get("/health")
    def health():
        return {"status": "ok"}, 200

    # common error handlers
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"erro": "recurso_nao_encontrado"}), 404

    with app.app_context():
        db.create_all()

    return app

# For `flask --app app run`
app = create_app()
