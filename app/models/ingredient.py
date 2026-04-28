from . import get_db

class Ingredient:
    @staticmethod
    def create(user_id, name, quantity, unit, type='inventory', is_bought=False):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            INSERT INTO ingredients (user_id, name, quantity, unit, type, is_bought)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (user_id, name, quantity, unit, type, is_bought))
        db.commit()
        return cursor.lastrowid

    @staticmethod
    def get_by_id(ingredient_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM ingredients WHERE id = ?', (ingredient_id,))
        return cursor.fetchone()

    @staticmethod
    def get_inventory(user_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM ingredients WHERE user_id = ? AND type = "inventory" ORDER BY created_at DESC', (user_id,))
        return cursor.fetchall()

    @staticmethod
    def get_shopping_list(user_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM ingredients WHERE user_id = ? AND type = "shopping_list" ORDER BY is_bought ASC, created_at DESC', (user_id,))
        return cursor.fetchall()

    @staticmethod
    def update(ingredient_id, name=None, quantity=None, unit=None, is_bought=None):
        db = get_db()
        cursor = db.cursor()
        
        # Build dynamic query based on provided fields
        fields = []
        values = []
        if name is not None:
            fields.append("name = ?")
            values.append(name)
        if quantity is not None:
            fields.append("quantity = ?")
            values.append(quantity)
        if unit is not None:
            fields.append("unit = ?")
            values.append(unit)
        if is_bought is not None:
            fields.append("is_bought = ?")
            values.append(is_bought)
            
        if not fields:
            return False
            
        query = f"UPDATE ingredients SET {', '.join(fields)} WHERE id = ?"
        values.append(ingredient_id)
        
        cursor.execute(query, tuple(values))
        db.commit()
        return cursor.rowcount > 0

    @staticmethod
    def delete(ingredient_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('DELETE FROM ingredients WHERE id = ?', (ingredient_id,))
        db.commit()
        return cursor.rowcount > 0
