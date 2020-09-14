import random
from common import gen_date
from common import gen_words

message_id = random.randint(2345900, 9345900)


def gen_message(user_id1, user_id2):
    global message_id
    message_id += random.randint(1, 10)
    is_read = 1 if random.randint(0, 10) < 8 else 0
    return {
        "message_id": message_id,
        "user_from_id": user_id1,
        "user_to_id": user_id2,
        "send_time": gen_date(False, 100, 120),
        "is_read": is_read,
        "read_time": gen_date(False, 80, 99) if is_read == 1 else 'NULL',
        "message_text": " ".join(gen_words(20))
    }
