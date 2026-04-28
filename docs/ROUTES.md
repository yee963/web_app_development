# 路由與頁面設計文件 (ROUTES)

本文件描述「AI 智慧食譜推薦系統」的路由規劃，包含前端頁面與對應的後端處理邏輯。

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| 首頁 / 輸入食材 | GET | `/` | `index.html` | 顯示首頁與剩餘食材輸入表單 |
| 個人化設定頁面 | GET | `/profile` | `profile.html` | 顯示使用者的飲食偏好與禁忌 |
| 更新個人設定 | POST | `/profile` | — | 接收表單更新偏好，重導向 `/profile` |
| 註冊頁面 | GET | `/register` | `register.html` | 顯示註冊表單 |
| 處理註冊 | POST | `/register` | — | 建立帳號，重導向 `/login` |
| 登入頁面 | GET | `/login` | `login.html` | 顯示登入表單 |
| 處理登入 | POST | `/login` | — | 驗證身分，重導向 `/` |
| 登出 | GET/POST | `/logout` | — | 清除 Session，重導向 `/` |
| 收藏/社群食譜牆 | GET | `/recipes` | `recipe_list.html` | 列出使用者收藏或公開分享的食譜 |
| 生成食譜推薦 | POST | `/recipe/generate` | — | 接收輸入的食材，呼叫 AI，寫入 DB，重導向 `/recipe/<id>` |
| 食譜詳細資訊 | GET | `/recipe/<id>` | `recipe_detail.html` | 顯示特定食譜的作法與營養分析 |
| 收藏/分享食譜 | POST | `/recipe/<id>/share` | — | 更新 is_public 狀態，重導向 `/recipes` |
| 檢視冰箱庫存 | GET | `/inventory` | `inventory_list.html` | 顯示目前冰箱現有食材清單 |
| 更新冰箱庫存 | POST | `/inventory/update` | — | 新增/修改冰箱食材，重導向 `/inventory` |
| 我的購物清單 | GET | `/inventory/shopping-list` | `shopping_list.html` | 檢視待採買項目 |
| 更新購物清單 | POST | `/inventory/shopping-list/update` | — | 新增/修改清單或標記已採買，重導向回清單 |

## 2. 每個路由的詳細說明

### 2.1 主頁與個人設定 (main.py)
- **GET `/`**: 渲染 `index.html`。傳遞目前登入使用者的基本資訊。
- **GET `/profile`**: 查詢 `User` Model 取出 `dietary_preferences` 與 `disliked_ingredients`，渲染 `profile.html`。
- **POST `/profile`**: 接收表單傳來的 `dietary_preferences` 等，呼叫 `User.update()`，成功後 `redirect('/profile')` 附帶成功訊息。

### 2.2 身分驗證 (auth.py)
- **GET/POST `/login`**, **`/register`**, **`/logout`**: 處理使用者 session。MVP 階段可以簡化實作。

### 2.3 食譜相關 (recipe.py)
- **POST `/recipe/generate`**: 接收來自首頁的食材清單，並讀取使用者的飲食偏好，呼叫外部 AI API。取得回應後呼叫 `Recipe.create()` 寫入資料庫，並 `redirect(url_for('recipe.detail', id=new_id))`。
- **GET `/recipe/<id>`**: 呼叫 `Recipe.get_by_id()`，渲染 `recipe_detail.html`。若找不到則回傳 404。
- **GET `/recipes`**: 呼叫 `Recipe.get_all(user_id)` 或 `Recipe.get_public_recipes()`，渲染 `recipe_list.html`。
- **POST `/recipe/<id>/share`**: 呼叫 `Recipe.update(recipe_id, is_public=True)`，然後重導向到列表頁。

### 2.4 食材與購物清單 (inventory.py)
- **GET `/inventory`**: 呼叫 `Ingredient.get_inventory()`，渲染 `inventory_list.html`。
- **POST `/inventory/update`**: 接收表單（名稱、數量、單位），呼叫 `Ingredient.create()` (type='inventory')。
- **GET `/inventory/shopping-list`**: 呼叫 `Ingredient.get_shopping_list()`，渲染 `shopping_list.html`。
- **POST `/inventory/shopping-list/update`**: 更新已採買狀態 `is_bought` 或新增項目。

## 3. Jinja2 模板清單

所有的 HTML 檔案都將繼承自 `base.html`，以保持統一的導覽列 (Navbar) 與頁尾 (Footer)。
1. `templates/base.html`：母模版
2. `templates/index.html`：首頁
3. `templates/profile.html`：個人設定
4. `templates/login.html`：登入頁面
5. `templates/register.html`：註冊頁面
6. `templates/recipe_list.html`：食譜列表（收藏與社群牆）
7. `templates/recipe_detail.html`：單一食譜詳情
8. `templates/inventory_list.html`：冰箱食材列表
9. `templates/shopping_list.html`：購物清單列表
