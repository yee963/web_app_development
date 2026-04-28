import sqlite3
from flask import g, current_app

def get_db():
    if 'db' not in g:
        # Assuming the database is located at instance/database.db
        g.db = sqlite3.connect(
            'instance/database.db',
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
