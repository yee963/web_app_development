from flask import Blueprint

# 之後在主程式 (app.py) 中，將會 import 這些藍圖並註冊
from .main import bp as main_bp
from .auth import bp as auth_bp
from .recipe import bp as recipe_bp
from .inventory import bp as inventory_bp
