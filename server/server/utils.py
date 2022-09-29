import random


def generate_four_digit_code():
    return '{:04}'.format(random.randrange(1, 10**4))