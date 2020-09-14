import random
import datetime

words = open('words.txt').read().splitlines()


def gen_words(max_words, min_words=2):
    cnt = random.randint(min_words, max_words)
    return [random.choice(words) for i in range(cnt)]


def gen_date(birth, dmin=10, dmax=1000):
    days = random.randint(dmin, dmax)
    date = datetime.datetime.now() - datetime.timedelta(days=days)
    if birth:
        years = random.randint(18, 99)
        date -= datetime.timedelta(days=365 * years)
        return date.strftime("%Y-%m-%d")
    return date.strftime("%Y-%m-%d %H:%M:%S")
