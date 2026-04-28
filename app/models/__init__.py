import sqlite3

def get_db_connection():
    """
    取得 SQLite 資料庫連線。
    確保回傳的連線具備 row_factory = sqlite3.Row，方便以字典方式存取欄位。
    """
    conn = sqlite3.connect('instance/database.db')
    conn.row_factory = sqlite3.Row
    return conn
