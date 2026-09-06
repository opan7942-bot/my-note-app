import sqlite3
import os

"""
Database initialization and CRUD operations module.
Handles sqlite database operations for Notes, Todos, Secrets, and Image Paths.
"""


def get_db_path():
    """حفظ قاعدة البيانات في مجلد AppData الخاص بنظام الويندوز لحل مشاكل سطح المكتب والـ EXE"""
    # جلب مسار مجلد AppData الخاص بالمستخدم الحالي
    user_appdata = os.environ.get('LOCALAPPDATA', os.path.expanduser('~'))

    # إنشاء مجلد ثابت باسم برنامجك داخل AppData
    app_folder = os.path.join(user_appdata, "MyDesktopApp")
    data_dir = os.path.join(app_folder, "data")

    # التأكد من وجود المجلد
    os.makedirs(data_dir, exist_ok=True)

    return os.path.join(data_dir, "my_app_data.db")

def init_db():
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()

    # 1. Notes Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT
        )
    """)

    # 2. Todos Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT
        )
    """)

    # 3. Secrets Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS secrets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            password TEXT
        )
    """)

    # 4. Image Paths Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pic_path (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT
        )
    """)

    conn.commit()
    conn.close()

# --- NOTES ---

def add_note_data(text):
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (text) VALUES (?)", (text,))
    conn.commit()
    conn.close()

def get_notes_data():
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("SELECT id, text FROM notes")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_note_data(note_id):
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()

# --- TODOS ---

def add_todo_data(task):
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todos (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()

def get_todos_data():
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("SELECT id, task FROM todos")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_todo_data(todo_id):
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()

# --- SECRETS ---

def add_secret_data(title, password):
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("INSERT INTO secrets (title, password) VALUES (?, ?)", (title, password))
    conn.commit()
    conn.close()

def get_secret_data():
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, password FROM secrets")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_secret_data(secret_id):
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("DELETE FROM secrets WHERE id = ?", (secret_id,))
    conn.commit()
    conn.close()

# --- PICTURE PATHS ---

def add_pic(pic_path):
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pic_path (text) VALUES (?)", (pic_path,))
    conn.commit()
    conn.close()

def get_pic_path():
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("SELECT id, text FROM pic_path")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_pic_path(image_id):
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pic_path WHERE id = ?", (image_id,))
    conn.commit()
    conn.close()