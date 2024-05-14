from api import create_app, load_config

config = load_config()
app = create_app(config)
