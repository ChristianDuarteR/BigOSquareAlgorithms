import random
import string

from python import constants


def get_random_list(size, limit=constants.MAX_VALUE):
    answer = []
    while len(answer) < size:
        answer.append(random.randint(0, limit))

    return answer


def get_random_x(limit=constants.MAX_VALUE):
    return random.randint(1, limit)


def get_random_seq(size):
    x = ''.join(random.choices(string.ascii_lowercase, k=size))
    y = ''.join(random.choices(string.ascii_lowercase, k=size))
    answer = (x, y)
    return answer
