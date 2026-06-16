import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("chat_history.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            ai_message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()    

def save_chat(user_message, ai_message):
    conn = sqlite3.connect("chat_history.db")
    cursor = conn.cursor()

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute('''
        INSERT INTO chat_history (user_message, ai_message, created_at) 
        VALUES (?, ?, ?)
    ''', (user_message, ai_message, created_at))
    conn.commit()
    conn.close()

def get_chat_history():
    conn = sqlite3.connect("chat_history.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT id, user_message, ai_message, created_at FROM chat_history ORDER BY created_at DESC')
    history = cursor.fetchall()
    conn.close()
    return history