import sqlite3
import os

"""
creat a file
creat tables and adding functions
make everything ready for the program
"""
def init_db():
    current = os.getcwd()
    path = os.path.join(current,"data")
    os.makedirs(path, exist_ok=True)
    # الاتصال بملف القاعدة (سينشئه إذا لم يكن موجوداً)
    conn = sqlite3.connect(os.path.join(path,"my_app_data.db"))
    cursor = conn.cursor()

    # 1. جدول الملاحظات
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT
        )
    """)

    # 2. جدول المهام
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT
        )
    """)

    # 3. جدول كلمات السر
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS secrets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            password TEXT
        )
    """)

    conn.commit()
    conn.close()

def add_note_data(text):
    current = os.getcwd()
    path = os.path.join(current, "data")
    conn = sqlite3.connect(os.path.join(path, "my_app_data.db"))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (text) VALUES (?)", (text,))
    conn.commit()
    conn.close()


def get_notes_data():
    current = os.getcwd()
    path = os.path.join(current, "data")
    conn = sqlite3.connect(os.path.join(path, "my_app_data.db"))  # مسار القاعدة
    cursor = conn.cursor()

    # جلب كل النصوص المحفوظة في جدول الملاحظات
    cursor.execute("SELECT text FROM notes")
    rows = cursor.fetchall()  # ترجع قائمة مثل: [("ملاحظة 1",), ("ملاحظة 2",)]

    conn.close()  # لا نحتاج commit لأننا لم نعدل شيء، فقط قراءة
    return rows

def add_todo_data(task):
    current = os.getcwd()
    path = os.path.join(current, "data")
    conn = sqlite3.connect(os.path.join(path, "my_app_data.db"))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todos (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()

def get_todos_data():
    current = os.getcwd()
    path = os.path.join(current, "data")
    conn = sqlite3.connect(os.path.join(path, "my_app_data.db"))  # مسار القاعدة
    cursor = conn.cursor()

    # جلب كل النصوص المحفوظة في جدول الملاحظات
    cursor.execute("SELECT task FROM todos")
    rows = cursor.fetchall()  # ترجع قائمة مثل: [("ملاحظة 1",), ("ملاحظة 2",)]

    conn.close()  # لا نحتاج commit لأننا لم نعدل شيء، فقط قراءة
    return rows

def add_secret_data(title,password):
    current = os.getcwd()
    path = os.path.join(current, "data")
    conn = sqlite3.connect(os.path.join(path, "my_app_data.db"))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO secrets (title, password) VALUES (?, ?)", (title, password))
    conn.commit()
    conn.close()

def get_secret_data():
    current = os.getcwd()
    path = os.path.join(current, "data")
    conn = sqlite3.connect(os.path.join(path, "my_app_data.db"))  # مسار القاعدة
    cursor = conn.cursor()

    # جلب كل النصوص المحفوظة في جدول الملاحظات
    cursor.execute("SELECT title, password FROM secrets")
    rows = cursor.fetchall()  # ترجع قائمة مثل: [("ملاحظة 1",), ("ملاحظة 2",)]

    conn.close()  # لا نحتاج commit لأننا لم نعدل شيء، فقط قراءة
    return rows