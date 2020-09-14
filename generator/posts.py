import random
from common import gen_date
from common import gen_words

post_id = random.randint(834500, 1534500)


def gen_post(user_id, group_id):
    global post_id
    post_id += random.randint(1, 10)
    return {
        "post_id": post_id,
        "user_id": user_id,
        "group_id": group_id,
        "creation_time": gen_date(False),
        "post_text": " ".join(gen_words(40)),
        "post_type": random.choice(['default', 'pinned', 'special'])
    }
