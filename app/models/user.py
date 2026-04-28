from . import get_db_connection

class User:
    @staticmethod
    def create(username, password_hash=None, dietary_preferences=None, disliked_ingredients=None):
        """
        新增一筆使用者記錄。
        參數:
            username (str): 使用者名稱
            password_hash (str, optional): 密碼雜湊
            dietary_preferences (str, optional): 飲食偏好 (JSON 或字串)
            disliked_ingredients (str, optional): 不吃的食材 (JSON 或字串)
        回傳:
            int: 新增的記錄 ID，若失敗則回傳 None
        """
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (username, password_hash, dietary_preferences, disliked_ingredients)
                VALUES (?, ?, ?, ?)
            ''', (username, password_hash, dietary_preferences, disliked_ingredients))
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"User.create error: {e}")
            return None
        finally:
            if conn:
                conn.close()

    @staticmethod
    def get_by_id(user_id):
        """
        根據 ID 取得單筆使用者記錄。
        參數:
            user_id (int): 使用者 ID
        回傳:
            sqlite3.Row: 使用者記錄，找不到或失敗則回傳 None
        """
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"User.get_by_id error: {e}")
            return None
        finally:
            if conn:
                conn.close()

    @staticmethod
    def get_all():
        """
        取得所有使用者記錄。
        回傳:
            list[sqlite3.Row]: 使用者記錄列表
        """
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            return cursor.fetchall()
        except Exception as e:
            print(f"User.get_all error: {e}")
            return []
        finally:
            if conn:
                conn.close()

    @staticmethod
    def update(user_id, data):
        """
        更新使用者記錄的偏好設定。
        參數:
            user_id (int): 使用者 ID
            data (dict): 欲更新的欄位與值，例如 {'dietary_preferences': '...', 'disliked_ingredients': '...'}
        回傳:
            bool: 是否更新成功
        """
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            fields = []
            values = []
            if 'dietary_preferences' in data:
                fields.append("dietary_preferences = ?")
                values.append(data['dietary_preferences'])
            if 'disliked_ingredients' in data:
                fields.append("disliked_ingredients = ?")
                values.append(data['disliked_ingredients'])
                
            if not fields:
                return False
                
            query = f"UPDATE users SET {', '.join(fields)} WHERE id = ?"
            values.append(user_id)
            
            cursor.execute(query, tuple(values))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"User.update error: {e}")
            return False
        finally:
            if conn:
                conn.close()

    @staticmethod
    def delete(user_id):
        """
        刪除一筆使用者記錄。
        參數:
            user_id (int): 使用者 ID
        回傳:
            bool: 是否刪除成功
        """
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"User.delete error: {e}")
            return False
        finally:
            if conn:
                conn.close()
