from flask import Flask
from .routes import init_routes  # ルーティングの初期化関数をインポート


def create_app():
    app = Flask(__name__)

    # アプリケーションの設定をロード
    app.config.from_object("api.config.Config")

    # ルーティングの初期化
    init_routes(app)

    return app
