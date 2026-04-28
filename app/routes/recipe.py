from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.recipe import Recipe
import random

bp = Blueprint('recipe', __name__, url_prefix='/recipe')

@bp.route('/generate', methods=['POST'])
def generate():
    user_id = 1
    ingredients = request.form.get('ingredients')
    if not ingredients:
        flash('請至少輸入一項食材！', 'danger')
        return redirect(url_for('main.index'))
    
    # MVP 模擬 AI 生成結果
    first_ingredient = ingredients.split(',')[0].strip() if ',' in ingredients else ingredients.split(' ')[0].strip()
    fake_recipe = {
        'user_id': user_id,
        'title': f'特製 {first_ingredient[:6]} 風味創意料理',
        'instructions': f'1. 將 {ingredients} 清洗乾淨並切塊備用。\n2. 熱鍋下少許油，將較難熟的食材先下鍋煸香。\n3. 加入剩下的食材大火快炒。\n4. 加入適量鹽巴與黑胡椒調味。\n5. 蓋上鍋蓋燜煮約 3-5 分鐘即可盛盤上桌！',
        'calories': random.randint(300, 700),
        'carbs': random.randint(20, 70),
        'protein': random.randint(15, 45),
        'fat': random.randint(10, 35),
        'is_public': False
    }
    
    recipe_id = Recipe.create(fake_recipe)
    if recipe_id:
        flash('太棒了！AI 已經為您生成專屬食譜。', 'success')
        return redirect(url_for('recipe.detail', id=recipe_id))
    else:
        flash('發生錯誤，食譜生成失敗。', 'danger')
        return redirect(url_for('main.index'))

@bp.route('/<int:id>')
def detail(id):
    recipe = Recipe.get_by_id(id)
    if not recipe:
        flash('找不到該食譜。', 'danger')
        return redirect(url_for('recipe.list_recipes'))
    return render_template('recipe_detail.html', recipe=recipe, current_user_id=1)

@bp.route('/<int:id>/share', methods=['POST'])
def share(id):
    recipe = Recipe.get_by_id(id)
    if recipe:
        new_status = not recipe['is_public']
        Recipe.update(id, {'is_public': new_status})
        status_text = '公開' if new_status else '私人'
        flash(f'食譜已設為{status_text}！', 'success')
    return redirect(url_for('recipe.detail', id=id))

@bp.route('s')
def list_recipes():
    # MVP 階段直接列出所有公開的食譜
    recipes = Recipe.get_all()
    # 過濾出 is_public 的，或是當前使用者的
    display_recipes = [r for r in recipes if r['is_public'] or r['user_id'] == 1]
    return render_template('recipe_list.html', recipes=display_recipes)
