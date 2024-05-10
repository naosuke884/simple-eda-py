from flask import Blueprint

bp = Blueprint("api", __name__)


@bp.route("/set/dataset")
def set_dataset():
    return "Hello, World!"


def init_routes(app):
    app.register_blueprint(bp)  # Blueprintをアプリケーションに登録
