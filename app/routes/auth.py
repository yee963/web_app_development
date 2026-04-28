from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    GET: 顯示註冊表單。
    POST: 建立帳號，重導向至 /login。
    """
    pass

@bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    GET: 顯示登入表單。
    POST: 驗證身分，重導向至 /。
    """
    pass

@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    """
    清除 Session，重導向至 /。
    """
    pass
