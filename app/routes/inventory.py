from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.ingredient import Ingredient

bp = Blueprint('inventory', __name__, url_prefix='/inventory')

@bp.route('/')
def index():
    user_id = 1
    items = Ingredient.get_all(user_id, 'inventory')
    return render_template('inventory_list.html', items=items)

@bp.route('/update', methods=['POST'])
def update_inventory():
    user_id = 1
    name = request.form.get('name')
    if name:
        Ingredient.create({
            'user_id': user_id,
            'name': name,
            'quantity': request.form.get('quantity'),
            'unit': request.form.get('unit'),
            'type': 'inventory'
        })
        flash(f'已將 {name} 新增至冰箱庫存！', 'success')
    return redirect(url_for('inventory.index'))

@bp.route('/delete/<int:id>', methods=['POST'])
def delete_inventory(id):
    Ingredient.delete(id)
    flash('已從冰箱移除食材。', 'success')
    return redirect(url_for('inventory.index'))

@bp.route('/shopping-list')
def shopping_list():
    user_id = 1
    items = Ingredient.get_all(user_id, 'shopping_list')
    return render_template('shopping_list.html', items=items)

@bp.route('/shopping-list/update', methods=['POST'])
def update_shopping_list():
    user_id = 1
    name = request.form.get('name')
    if name:
        Ingredient.create({
            'user_id': user_id,
            'name': name,
            'quantity': request.form.get('quantity'),
            'unit': request.form.get('unit'),
            'type': 'shopping_list',
            'is_bought': False
        })
        flash(f'已將 {name} 加入購物清單！', 'success')
    return redirect(url_for('inventory.shopping_list'))

@bp.route('/shopping-list/toggle/<int:id>', methods=['POST'])
def toggle_shopping_list(id):
    item = Ingredient.get_by_id(id)
    if item:
        new_status = not item['is_bought']
        Ingredient.update(id, {'is_bought': new_status})
    return redirect(url_for('inventory.shopping_list'))

@bp.route('/shopping-list/delete/<int:id>', methods=['POST'])
def delete_shopping_list(id):
    Ingredient.delete(id)
    flash('已從購物清單移除！', 'success')
    return redirect(url_for('inventory.shopping_list'))
