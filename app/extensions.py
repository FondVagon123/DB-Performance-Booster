import psycopg2
from flask_jwt_extended import JWTManager

# Ініціалізація JWT
jwt = JWTManager()

# Параметри підключення до вашої бази даних
DB_CONFIG = {
    'host': 'junction.proxy.rlwy.net',
    'port': '19910',
    'database': 'RailwayDB',
    'user': 'postgres',
    'password': 'ygenbXELPjFcAdfMKwzQwfXmPGDJIAqu'
}

# Функція для підключення до бази даних
def get_db_connection():
    # Підключення до бази даних PostgreSQL через psycopg2
    connection = psycopg2.connect(
        dbname=DB_CONFIG['database'],  # Ваше ім'я бази даних
        user=DB_CONFIG['user'],        # Ваш користувач PostgreSQL
        password=DB_CONFIG['password'],# Ваш пароль
        host=DB_CONFIG['host'],        # Хост вашої БД
        port=DB_CONFIG['port']         # Порт вашої БД
    )
    return connection
