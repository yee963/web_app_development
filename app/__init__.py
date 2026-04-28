import os
from flask import Flask
from dotenv import load_dotenv
import sqlite3

# 載入環境變數
load_dotenv()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_default_secret')
    
    # 初始化資料庫
    with app.app_context():
        init_db()

    # 註冊 Blueprints
    from app.routes.main import bp as main_bp
    from app.routes.auth import bp as auth_bp
    from app.routes.recipe import bp as recipe_bp
    from app.routes.inventory import bp as inventory_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(recipe_bp)
    app.register_blueprint(inventory_bp)

    return app

def init_db():
    """初始化 SQLite 資料庫與表格"""
    os.makedirs('instance', exist_ok=True)
    db_path = os.path.join('instance', 'database.db')
    
    # 檢查資料庫檔案是否存在，若不存在則執行 schema.sql 建立表格
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        with open('database/schema.sql', 'r', encoding='utf-8') as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()
        print("Database initialized successfully.")
