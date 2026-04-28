from . import get_db

class User:
    @staticmethod
    def create(username, password_hash=None, dietary_preferences=None, disliked_ingredients=None):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            INSERT INTO users (username, password_hash, dietary_preferences, disliked_ingredients)
            VALUES (?, ?, ?, ?)
        ''', (username, password_hash, dietary_preferences, disliked_ingredients))
        db.commit()
        return cursor.lastrowid

    @staticmethod
    def get_by_id(user_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        return cursor.fetchone()

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users')
        return cursor.fetchall()

    @staticmethod
    def update(user_id, dietary_preferences=None, disliked_ingredients=None):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            UPDATE users
            SET dietary_preferences = ?, disliked_ingredients = ?
            WHERE id = ?
        ''', (dietary_preferences, disliked_ingredients, user_id))
        db.commit()
        return cursor.rowcount > 0

    @staticmethod
    def delete(user_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        db.commit()
        return cursor.rowcount > 0
