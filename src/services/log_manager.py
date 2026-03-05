import time
from config import COOLDOWN_SECONDS

last_seen = {}

def can_log(identity):
    now = time.time()
    if identity not in last_seen:
        last_seen[identity] = now
        return True

    if now - last_seen[identity] > COOLDOWN_SECONDS:
        last_seen[identity] = now
        return True

    return False