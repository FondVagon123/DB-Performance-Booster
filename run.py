from app import create_app  # Імпортуємо функцію create_app
from app.extensions import get_db_connection  # Функція для підключення до бази даних

# Створюємо додаток
app = create_app()

# Створюємо підключення до бази даних на старті
with app.app_context():
    # Тут можна додати додаткові ініціалізації або логіку, якщо необхідно
    pass

if __name__ == '__main__':
    app.run(debug=True)
