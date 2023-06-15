# create function that returns random string of specific length
import random

def random_string(length=10):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(length))