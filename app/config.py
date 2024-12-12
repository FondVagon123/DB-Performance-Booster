class Config:
    """Клас для зберігання налаштувань конфігурації додатку"""

    # Налаштування для бази даних
    SQLALCHEMY_DATABASE_URI = (
        'postgresql://postgres:ygenbXELPjFcAdfMKwzQwfXmPGDJIAqu@junction.proxy.rlwy.net:19910/RailwayDB'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Отключаємо модифікацію трекінгу

    # Налаштування для JWT
    JWT_SECRET_KEY = 'your-secret-key'  # Замість 'your-secret-key' використовуйте ваш секретний ключ
    JWT_ACCESS_TOKEN_EXPIRES = 30  # Термін дії токену - 30 днів

    # Логування
    LOGGING_LEVEL = 'DEBUG'
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'