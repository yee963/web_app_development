from . import get_db_connection

class Recipe:
    @staticmethod
    def create(data):
        """
        新增一筆食譜記錄。
        參數:
            data (dict): 包含 user_id, title, instructions 等欄位的字典
        回傳:
            int: 新增的記錄 ID，若失敗則回傳 None
        """
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO recipes (user_id, title, instructions, calories, carbs, protein, fat, is_public)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                data.get('user_id'),
                data.get('title'),
                data.get('instructions'),
                data.get('calories'),
                data.get('carbs'),
                data.get('protein'),
                data.get('fat'),
                data.get('is_public', False)
            ))
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Recipe.create error: {e}")
            return None
        finally:
            if conn:
                conn.close()

    @staticmethod
    def get_by_id(recipe_id):
        """
        根據 ID 取得單筆食譜記錄。
        參數:
            recipe_id (int): 食譜 ID
        回傳:
            sqlite3.Row: 食譜記錄，找不到或失敗則回傳 None
        """
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Recipe.get_by_id error: {e}")
            return None
        finally:
            if conn:
                conn.close()

    @staticmethod
    def get_all(user_id=None):
        """
        取得所有食譜記錄。若提供 user_id，則只取得該使用者的食譜。
        參數:
            user_id (int, optional): 使用者 ID
        回傳:
            list[sqlite3.Row]: 食譜記錄列表
        """
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            if user_id:
                cursor.execute('SELECT * FROM recipes WHERE user_id = ? ORDER BY created_at DESC', (user_id,))
            else:
                cursor.execute('SELECT * FROM recipes ORDER BY created_at DESC')
            return cursor.fetchall()
        except Exception as e:
            print(f"Recipe.get_all error: {e}")
            return []
        finally:
            if conn:
                conn.close()

    @staticmethod
    def update(recipe_id, data):
        """
        更新食譜記錄。
        參數:
            recipe_id (int): 食譜 ID
            data (dict): 欲更新的欄位與值，例如 {'is_public': True}
        回傳:
            bool: 是否更新成功
        """
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            fields = []
            values = []
            if 'is_public' in data:
                fields.append("is_public = ?")
                values.append(data['is_public'])
                
            if not fields:
                return False
                
            query = f"UPDATE recipes SET {', '.join(fields)} WHERE id = ?"
            values.append(recipe_id)
            
            cursor.execute(query, tuple(values))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Recipe.update error: {e}")
            return False
        finally:
            if conn:
                conn.close()

    @staticmethod
    def delete(recipe_id):
        """
        刪除一筆食譜記錄。
        參數:
            recipe_id (int): 食譜 ID
        回傳:
            bool: 是否刪除成功
        """
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Recipe.delete error: {e}")
            return False
        finally:
            if conn:
                conn.close()
