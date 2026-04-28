from flask import Blueprint, render_template, request, redirect, url_for, flash

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        flash('目前為 MVP 版本，已為您自動配置預設帳號，可以直接開始使用！', 'info')
        return redirect(url_for('main.index'))
    return render_template('register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        flash('登入成功！歡迎回來。', 'success')
        return redirect(url_for('main.index'))
    return render_template('login.html')

@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    flash('您已成功登出。', 'success')
    return redirect(url_for('main.index'))
