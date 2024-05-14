from flask import Flask
from .routes import init_routes  # ルーティングの初期化関数をインポート
from .config import Config


def load_config():
    return Config()


def create_app(config: Config):
    app = Flask(__name__)

    # アプリケーションの設定をロード
    app.config.from_object(config)
    # ルーティングの初期化
    init_routes(app)

    return app
