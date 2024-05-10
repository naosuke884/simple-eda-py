from api import create_app

app = create_app()  # Flaskアプリケーションを作成

if __name__ == "__main__":
    app.run()  # アプリケーションを実行
