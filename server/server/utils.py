import random


def generate_four_digit_code():
    return f"{random.randrange(1, 10**4):04}"
