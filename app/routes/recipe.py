from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('recipe', __name__, url_prefix='/recipe')

@bp.route('/generate', methods=['POST'])
def generate():
    """
    接收輸入的食材清單，讀取使用者飲食偏好，呼叫外部 AI API 生成食譜。
    寫入資料庫後，重導向至 /recipe/<id> 檢視詳細內容。
    """
    pass

@bp.route('/<int:id>')
def detail(id):
    """
    查詢特定食譜並顯示其作法與營養分析。
    """
    pass

@bp.route('/<int:id>/share', methods=['POST'])
def share(id):
    """
    更新特定食譜的 is_public 狀態，並重導向至 /recipes。
    """
    pass

@bp.route('s')
def list_recipes():
    """
    列出使用者收藏或公開分享的食譜 (URL: /recipes)。
    """
    pass
