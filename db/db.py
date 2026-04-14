import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
db = sqlite3.connect(BASE_DIR / 'identifier.sqlite',check_same_thread=False)
cursor = db.cursor()


def add_hash(hash,ios,tg_id):
    cursor.execute('INSERT INTO verification_code (hash,seller_or_investor,tg_id) VALUES (?,?,?)', (hash,ios,tg_id))
    db.commit()

def get_verification_code(tg_id):
    cursor.execute('SELECT * FROM verification_code WHERE tg_id =?',(tg_id,))
    res = cursor.fetchone()
    if res:
        return res
    else:
        return None


def add_waiting(tg_id,com=None):
    cursor.execute('INSERT INTO waiting (tg_id,comment) VALUES (?)',(tg_id,com))
    db.commit()

def get_waiting():
    cursor.execute('SELECT * FROM waiting')
    res = cursor.fetchall()
    if res:
        return res
    else:
        return None