import sqlite3
import datetime

now = datetime.datetime.now()
__connection = None

def get_conection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect('bot.db')
    return __connection


def init_db(force: bool = False):
    conn = get_conection()

    c = conn.cursor()
    if force:
        c.execute('DROP TABLE IF EXISTS user_message')

    c.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id           INTEGER PRIMARY KEY,
                user_id      INTEGER,
                username     TEXT,
                first_name   TEXT,
                last_name    TEXT,
                date_reg     INT  
                )
            ''')
    conn.commit()

    c.execute('''
            CREATE TABLE IF NOT EXISTS user_message(
            id           INTEGER PRIMARY KEY,
            user_id      INTEGER NOT NULL,
            username     TEXT,
            text         TEXT NOT NULL,
            date_time    INT
            )
        ''')
    # Сохраняем изменнения
    conn.commit()

    c.execute('''
               CREATE TABLE IF NOT EXISTS bot_answer(
               id           INTEGER PRIMARY KEY,
               user_id      INTEGER NOT NULL,
               username     TEXT,
               text         TEXT NOT NULL,
               date_time    INT
               )
           ''')
    # Сохраняем изменнения
    conn.commit()

    c.execute('''
                CREATE TABLE IF NOT EXISTS time_mail_message(
                    id           INTEGER PRIMARY KEY,
                    user_id      INTEGER,
                    username     TEXT,
                    time_mail    TEXT 
                    )
                ''')

    # Сохраняем изменнения
    conn.commit()

def add_message(user_id: int, username: str, text: str):
    init_db()
    conn = get_conection()
    c = conn.cursor()
    c.execute('INSERT INTO user_message (user_id, username, text, date_time) VALUES (?, ?, ?, ?)', (user_id, username, text, now.strftime('%d-%m-%Y %H:%M:%S')))
    conn.commit()

def bot_answer(user_id: int, username: str, text: str):
    init_db()
    conn = get_conection()
    c = conn.cursor()
    c.execute('INSERT INTO bot_answer (user_id, username, text, date_time) VALUES (?, ?, ?, ?)', (user_id, username, text, now.strftime('%d-%m-%Y %H:%M:%S')))
    conn.commit()


def users(user_id: int, username: str, first_name: str, last_name: str):
    init_db()
    conn = get_conection()
    c = conn.cursor()
    user = user_id
    c.execute(f'SELECT user_id FROM users WHERE user_id = {user}')
    data = c.fetchone()
    if data is None:
        c.execute('INSERT INTO users (user_id, username, first_name, last_name, date_reg) VALUES (?, ?, ?, ?, ?)', (user_id, username, first_name, last_name, now.strftime('%d-%m-%Y %H:%M:%S')))
        conn.commit()

def time_mail_message(user_id: int, username: str, time_mail: int):
    init_db()
    conn = get_conection()
    c = conn.cursor()
    c.execute('INSERT INTO time_mail_message (user_id, username, time_mail) VALUES (?, ?, ?)', (user_id, username, time_mail))
    conn.commit()



if __name__ == '__main__':
    """new_user(user_id=111242212, username='starboy', first_name='old', last_name='kukold')"""
    time_mail_message(user_id=573056381, username='doginigi', time_mail='6:00')
    """add_message(user_id=12345, username='scriptonit', text="kekwerw")"""