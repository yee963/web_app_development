from . import get_db

class Recipe:
    @staticmethod
    def create(user_id, title, instructions, calories=None, carbs=None, protein=None, fat=None, is_public=False):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            INSERT INTO recipes (user_id, title, instructions, calories, carbs, protein, fat, is_public)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (user_id, title, instructions, calories, carbs, protein, fat, is_public))
        db.commit()
        return cursor.lastrowid

    @staticmethod
    def get_by_id(recipe_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,))
        return cursor.fetchone()

    @staticmethod
    def get_all(user_id=None):
        db = get_db()
        cursor = db.cursor()
        if user_id:
            cursor.execute('SELECT * FROM recipes WHERE user_id = ? ORDER BY created_at DESC', (user_id,))
        else:
            cursor.execute('SELECT * FROM recipes ORDER BY created_at DESC')
        return cursor.fetchall()

    @staticmethod
    def get_public_recipes():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM recipes WHERE is_public = 1 ORDER BY created_at DESC')
        return cursor.fetchall()

    @staticmethod
    def update(recipe_id, is_public):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            UPDATE recipes
            SET is_public = ?
            WHERE id = ?
        ''', (is_public, recipe_id))
        db.commit()
        return cursor.rowcount > 0

    @staticmethod
    def delete(recipe_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,))
        db.commit()
        return cursor.rowcount > 0
