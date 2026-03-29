import base64
import hashlib
import random
import time

from db.db import add_hash


def gen_hash(IorS,user_tg_id):
    data = f"{time.time()}_{random.random()}"
    hash = hashlib.sha256(data.encode()).digest()
    short_hash = base64.urlsafe_b64encode(hash).decode()
    add_hash(short_hash,IorS,user_tg_id)
    return short_hash
