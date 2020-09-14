#!/usr/bin/env python3

from users import gen_user
from groups import gen_group
from groups import gen_join_group
from posts import gen_post
from messages import gen_message
import random
import sys

USERS_TABLE = "`skillboxdb`.`user`"
GROUPS_TABLE = "`skillboxdb`.`discussion_group`"
POSTS_TABLE = "`skillboxdb`.`user_group_post`"
GROUP_JOIN_TABLE = "`skillboxdb`.`users_to_discussion_groups`"
MESSAGES_TABLE = "`skillboxdb`.`user_private_message`"


def wrap_null(v):
    if v == 'NULL':
        return v
    return f"'{v}'"


def make_insert(table, items):
    columns = items[0].keys()
    col_list = ", ".join([f"`{k}`" for k in items[0].keys()])
    values_sql = []
    for item in items:
        values = [wrap_null(val) for val in [item[key] for key in columns]]
        values_sql.append("\t(" + ", ".join(values) + ")")
    values_sql_joined = ",\n".join(values_sql)
    return f"INSERT INTO {table}({col_list}) VALUES\n{values_sql_joined}"


def make_users(n):
    users = [gen_user() for i in range(n)]
    sql = make_insert(USERS_TABLE, users)
    print(f"-- USERS({n}) : {USERS_TABLE} -- \n\n{sql};\n\n")
    return [user["user_id"] for user in users]


def make_groups(n, user_id_list):
    groups = [gen_group(random.choice(user_id_list)) for i in range(n)]
    sql = make_insert(GROUPS_TABLE, groups)
    print(f"-- GROUPS({n}) : {GROUPS_TABLE} -- \n\n{sql};\n\n")
    return [group["group_id"] for group in groups]


def make_posts(n, user_id_list, group_id_list):
    user_to_group = set()
    posts = []
    for i in range(n):
        user = random.choice(user_id_list)
        group = random.choice(group_id_list)
        number_of_posts = random.randint(0, 5)
        for k in range(0, number_of_posts):
            posts.append(gen_post(user, group))
        user_to_group.add((user, group, number_of_posts))
    sql = make_insert(POSTS_TABLE, posts)
    print(f"-- POSTS({n}) : {POSTS_TABLE} -- \n\n{sql};\n\n")
    return user_to_group


def make_group_joins(user_to_group):
    group_joins = []
    n = len(user_to_group)
    for (user, group, number_of_posts) in user_to_group:
        approved = 0 if number_of_posts == 0 else 1
        group_joins.append(gen_join_group(user, group, approved))
    sql = make_insert(GROUP_JOIN_TABLE, group_joins)
    print(f"-- GROUP_JOIN_TABLE({n}) : {GROUP_JOIN_TABLE} -- \n\n{sql};\n\n")


def make_messages(n, users):
    cnt = 0
    messages = []
    while cnt < n:
        user_id1 = random.choice(users)
        user_id2 = random.choice(users)
        if user_id1 == user_id2:
            continue
        cnt += 1
        messages.append(gen_message(user_id1, user_id2))
    sql = make_insert(MESSAGES_TABLE, messages)
    print(f"-- MESSAGES_TABLE({n}) : {MESSAGES_TABLE} -- \n\n{sql};\n\n")


try:
    users_count = int(sys.argv[1])
except:
    users_count = 1000

user_ids = make_users(users_count)
group_ids = make_groups(users_count // 10, user_ids)
user_to_group_join = make_posts(users_count // 2, user_ids, group_ids)
make_group_joins(user_to_group_join)
make_messages(users_count * 2, user_ids)
