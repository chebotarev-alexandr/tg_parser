import sqlite3

class DB_Operation:
    def __init__(self) -> None:
        try:
            self.connection = sqlite3.connect('cupon_database.db')
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print(f'Connetion Eroor: {e}')

    def add_subscription_and_cupon_to_database(self, message_text, cupon_name, source):
        try:
            self.cursor.execute(f'INSERT INTO cupon(message_text, cupon_name, source) VALUES ("{message_text}", "{cupon_name}", "{source}")')
            self.connection.commit()
        except sqlite3.Error as e:
            print(f'DB Eroor {e}')
