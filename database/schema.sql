-- 建立 users 表格
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password_hash TEXT,
    dietary_preferences TEXT,
    disliked_ingredients TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 建立 recipes 表格
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    instructions TEXT NOT NULL,
    calories INTEGER,
    carbs INTEGER,
    protein INTEGER,
    fat INTEGER,
    is_public BOOLEAN DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- 建立 ingredients 表格 (整合冰箱食材與購物清單)
CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    quantity TEXT,
    unit TEXT,
    type TEXT NOT NULL, -- 'inventory' 或 'shopping_list'
    is_bought BOOLEAN DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
