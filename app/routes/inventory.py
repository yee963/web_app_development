from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('inventory', __name__, url_prefix='/inventory')

@bp.route('/')
def index():
    """
    顯示目前冰箱現有食材清單。
    """
    pass

@bp.route('/update', methods=['POST'])
def update_inventory():
    """
    接收表單資料，新增或修改冰箱食材庫存，重導向至 /inventory。
    """
    pass

@bp.route('/shopping-list')
def shopping_list():
    """
    檢視待採買的購物清單項目。
    """
    pass

@bp.route('/shopping-list/update', methods=['POST'])
def update_shopping_list():
    """
    新增/修改購物清單項目，或標記為已採買，完成後重導向回 /inventory/shopping-list。
    """
    pass
