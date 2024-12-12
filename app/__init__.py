from flask import Flask
from .extensions import jwt
from .config import Config

def create_app():
    # Створення Flask додатку
    app = Flask(__name__)
    
    # Завантажуємо налаштування з класу Config
    app.config.from_object(Config)
    
    # Ініціалізація JWT
    jwt.init_app(app)

    # Регістрація ресурсів (API контролерів)
    from .resources.item import blp  # Імпортуємо Blueprint для елементів
    app.register_blueprint(blp)  # Регіструємо Blueprint в додатку

    return app
