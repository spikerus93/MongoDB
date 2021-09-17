import sys
import re
import json
from random import randint, choice
from datetime import datetime, timedelta


text = open('aiw.txt').read()
words = re.findall(
    r'[^a-z]([a-z]+)[^a-z]', 
    text.split('THE END')[0].split('CHAPTER I.')[-1].lower())
names = [name.title() for name in open('names.txt').read().split('\n')]
email_domains = ['example.com', 'example.net', 'example.info', 'example.ru']

users_output = 'users.json'
posts_output = 'posts.json'


used_emails = set()


def get_unique_email(first_name, last_name):
    email = f'{first_name[0]}{last_name}@{choice(email_domains)}'
    while email in used_emails:
        email = f'{first_name[0]}{last_name}{randint(1900, 2000)}@{choice(email_domains)}'
    email = email.lower()
    used_emails.add(email)
    return email

def text_generator():
    return ' '.join([choice(words) for _ in range(randint(10, 250))])


def encode_date(dt):
    return dt.isoformat().split('.')[0] + 'Z'


def generate(users_count=500):
    with open(users_output, 'w') as f:
        for i in range(users_count):
            first_name = choice(names)
            last_name = choice(names)
            registration_date = {"$date": encode_date(datetime(choice([2020, 2021]), randint(1,12), randint(1,28)))}
            birth_date = {"$date": encode_date(datetime(randint(1900, 2003), randint(1,12), randint(1,28)))}
            email = get_unique_email(first_name, last_name)
            user = {
                '_id': email,
                'first_name': first_name,
                'last_name': last_name,
                'registration_date': registration_date,
                'birth_date': birth_date,
                'visits': randint(1, 1000),
                'top_tags': {choice(words[:100]):randint(1, 10) for i in range(randint(2, 7))},
                'karma': randint(-100, 200)
            }
            f.write(json.dumps(user).replace('"$date"', '$date') + '\n')
    posts_count = users_count * 5
    topics = list(set(words[:100]))

    with open(posts_output, 'w') as f:
        for _ in range(posts_count):
            author = choice(list(used_emails))
            creation_date = {"$date": encode_date(datetime(choice([2020, 2021]), randint(1,12), randint(1,28)))}
            score = randint(-1000, 5000)
            post = {
                'author': author,
                'creation_date': creation_date,
                'topics': [choice(topics) for _ in range(randint(2, 5))],
                'score': score,
                'status': 'hidden' if score < -100 else 'published',
                'message': text_generator()
            }
            f.write(json.dumps(post).replace('"$date"', '$date') + '\n')

if __name__ == '__main__':
    generate(int(sys.argv[1]))