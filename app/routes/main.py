from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """
    首頁與剩餘食材輸入表單。
    """
    pass

@bp.route('/profile', methods=['GET', 'POST'])
def profile():
    """
    GET: 顯示使用者的飲食偏好與禁忌設定頁面。
    POST: 接收表單更新偏好，重導向至 /profile 並顯示成功訊息。
    """
    pass
