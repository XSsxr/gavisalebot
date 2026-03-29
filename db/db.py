import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
db = sqlite3.connect(BASE_DIR / 'identifier.sqlite',check_same_thread=False)
cursor = db.cursor()


def add_hash(hash,ios,tg_id):
    cursor.execute('INSERT INTO verification_code (hash,seller_or_investor,tg_id) VALUES (?,?,?)', (hash,ios,tg_id))
    db.commit()