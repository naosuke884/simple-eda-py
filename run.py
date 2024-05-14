from api import create_app, load_config

config = load_config()
app = create_app(config)

if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT)
