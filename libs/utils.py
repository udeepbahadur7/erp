import random
import string


def generate_random_chars(length, prefix="", suffix="", digits_only=False,
                          letters_only=False):
    s = ""
    if digits_only:
        s += string.digits * 2
    elif letters_only:
        s += string.ascii_letters
    else:
        s += string.ascii_letters + string.digits
    return prefix + ''.join([random.choice(s) for _ in range(length)]) + suffix
