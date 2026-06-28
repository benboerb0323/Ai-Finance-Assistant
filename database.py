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

def get_chat_history(page=1, per_page=10):
    conn = sqlite3.connect("chat_history.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    offset = (page - 1) * per_page

    cursor.execute('SELECT id, user_message, ai_message, created_at FROM chat_history ORDER BY created_at DESC LIMIT ? OFFSET ?', (per_page, offset))
    history = cursor.fetchall()
    conn.close()
    return history

def delete_all_history():
    conn = sqlite3.connect("chat_history.db")
    cursor = conn.cursor()
    cursor.execute('DELETE FROM chat_history')
    conn.commit()
    conn.close()

def delete_history_by_id(record_id):
    conn = sqlite3.connect("chat_history.db")
    cursor = conn.cursor()
    cursor.execute('DELETE FROM chat_history WHERE id = ?', (record_id,))
    conn.commit()
    conn.close()


def search_chat_history(keyword):
    conn = sqlite3.connect("chat_history.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, user_message, ai_message, created_at 
        FROM chat_history 
        WHERE user_message LIKE ? OR ai_message LIKE ? 
        ORDER BY created_at DESC
    ''', (f'%{keyword}%', f'%{keyword}%'))
    history = cursor.fetchall()
    conn.close()
    return history