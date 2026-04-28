from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.user import User

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """首頁與剩餘食材輸入表單。"""
    user_id = 1
    # 確保預設使用者存在
    if not User.get_by_id(user_id):
        User.create("default_user")
    user = User.get_by_id(user_id)
    return render_template('index.html', user=user)

@bp.route('/profile', methods=['GET', 'POST'])
def profile():
    """個人口味設定"""
    user_id = 1
    if request.method == 'POST':
        dietary_preferences = request.form.get('dietary_preferences')
        disliked_ingredients = request.form.get('disliked_ingredients')
        if not User.get_by_id(user_id):
            User.create("default_user")
        User.update(user_id, {
            'dietary_preferences': dietary_preferences,
            'disliked_ingredients': disliked_ingredients
        })
        flash('偏好設定已成功更新！', 'success')
        return redirect(url_for('main.profile'))
    
    user = User.get_by_id(user_id)
    return render_template('profile.html', user=user)
