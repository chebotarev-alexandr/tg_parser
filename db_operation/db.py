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

    def add_admitad_cupons_to_database(self, id, name, description, date_start, date_end, promo):
        try:
            self.cursor.execute(f'INSERT INTO Admitad_cupons(id, name, description, date_start, date_end, promo) VALUES({id}, "{name}", "{description}", "{date_start}", "{date_end}", "{promo}")')
            self.connection.commit()
        except sqlite3.Error as e: 
            print(f'DB Error {e}')

    def close_connection(self):
        self.connection.close()
