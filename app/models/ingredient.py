from . import get_db_connection

class Ingredient:
    @staticmethod
    def create(data):
        """
        新增一筆食材或購物清單記錄。
        參數:
            data (dict): 包含 user_id, name, quantity, unit, type 等欄位的字典
        回傳:
            int: 新增的記錄 ID，若失敗則回傳 None
        """
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO ingredients (user_id, name, quantity, unit, type, is_bought)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                data.get('user_id'),
                data.get('name'),
                data.get('quantity'),
                data.get('unit'),
                data.get('type', 'inventory'),
                data.get('is_bought', False)
            ))
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Ingredient.create error: {e}")
            return None
        finally:
            if conn:
                conn.close()

    @staticmethod
    def get_by_id(ingredient_id):
        """
        根據 ID 取得單筆記錄。
        參數:
            ingredient_id (int): 記錄 ID
        回傳:
            sqlite3.Row: 記錄，找不到或失敗則回傳 None
        """
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM ingredients WHERE id = ?', (ingredient_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Ingredient.get_by_id error: {e}")
            return None
        finally:
            if conn:
                conn.close()

    @staticmethod
    def get_all(user_id, type='inventory'):
        """
        取得特定使用者的食材庫存或購物清單。
        參數:
            user_id (int): 使用者 ID
            type (str): 'inventory' 或 'shopping_list'
        回傳:
            list[sqlite3.Row]: 記錄列表
        """
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            if type == 'shopping_list':
                cursor.execute('SELECT * FROM ingredients WHERE user_id = ? AND type = ? ORDER BY is_bought ASC, created_at DESC', (user_id, type))
            else:
                cursor.execute('SELECT * FROM ingredients WHERE user_id = ? AND type = ? ORDER BY created_at DESC', (user_id, type))
            return cursor.fetchall()
        except Exception as e:
            print(f"Ingredient.get_all error: {e}")
            return []
        finally:
            if conn:
                conn.close()

    @staticmethod
    def update(ingredient_id, data):
        """
        更新記錄。
        參數:
            ingredient_id (int): 記錄 ID
            data (dict): 欲更新的欄位與值
        回傳:
            bool: 是否更新成功
        """
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            fields = []
            values = []
            if 'name' in data:
                fields.append("name = ?")
                values.append(data['name'])
            if 'quantity' in data:
                fields.append("quantity = ?")
                values.append(data['quantity'])
            if 'unit' in data:
                fields.append("unit = ?")
                values.append(data['unit'])
            if 'is_bought' in data:
                fields.append("is_bought = ?")
                values.append(data['is_bought'])
            if 'type' in data:
                fields.append("type = ?")
                values.append(data['type'])
                
            if not fields:
                return False
                
            query = f"UPDATE ingredients SET {', '.join(fields)} WHERE id = ?"
            values.append(ingredient_id)
            
            cursor.execute(query, tuple(values))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Ingredient.update error: {e}")
            return False
        finally:
            if conn:
                conn.close()

    @staticmethod
    def delete(ingredient_id):
        """
        刪除一筆記錄。
        參數:
            ingredient_id (int): 記錄 ID
        回傳:
            bool: 是否刪除成功
        """
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM ingredients WHERE id = ?', (ingredient_id,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Ingredient.delete error: {e}")
            return False
        finally:
            if conn:
                conn.close()
