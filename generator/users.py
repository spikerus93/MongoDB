import json
import random
import hashlib
import datetime
import os
from common import gen_date

passwords = open('passwords.txt').read().splitlines()
logins = open('logins.txt').read().splitlines()
names = open('names.txt').read().splitlines()
email_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
reg_types = ['email', 'facebook', 'vk', 'google']
user_id = random.randint(1985, 8219)


def gen_hashed_password():
    password = random.choice(passwords)
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 3)
    return (salt + key).hex()


def gen_email(login):
    domain = random.choice(email_domains)
    return f"{login}@{domain}"

def gen_metadata():
    data = {
        "posts_per_page": random.choice([10, 25, 50, 100]),
        "default_theme": random.choice(['light', 'dark', 'blue']),
        "notifications": random.choice(['disabled', 'all', 'important_only'])
    }
    return json.dumps(data)


def gen_name():
    name = random.choice(names)
    return name[0].upper() + name[1:]


def gen_user():
    global user_id
    user_id += random.randint(1, 10)
    login = random.choice(logins)
    return {
        "user_id": user_id,
        "registration_time": gen_date(False),
        "login": f"{login}_{user_id}",
        "password_hash": gen_hashed_password(),
        "email": gen_email(login),
        "date_of_birth": gen_date(True),
        "metadata": gen_metadata(),
        "is_active": 1 if random.randint(0, 10) < 8 else 0,
        "registration_type": random.choice(reg_types),
        "first_name": gen_name(),
        "last_name": gen_name(),
    }
