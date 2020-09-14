import random
import json
from common import gen_words
from common import gen_date

group_id = random.randint(198500, 821900)


def gen_group(admin_id):
    global group_id
    group_id += random.randint(1, 10)
    return {
        "group_id": group_id,
        "creation_time": gen_date(False),
        "name": " ".join(gen_words(4)),
        "description": " ".join(gen_words(14)),
        "group_tags": json.dumps(gen_words(5)),
        "admin_user_id": admin_id,
        "approve_required": 1 if random.randint(0, 10) < 8 else 0,
    }


def gen_join_group(user, group, approved):
    return {
        "user_id": user,
        "group_id": group,
        "joined_time": gen_date(False, 100, 1000),
        "approved": approved,
        "approved_time": gen_date(False, 10, 100) if approved == 1 else 'NULL',
    }
