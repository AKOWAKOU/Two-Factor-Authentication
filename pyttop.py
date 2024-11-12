from random import choice
import string


def generate_otp(number_of_digits):
    otp = ''.join(choice(string.digits) for _ in range(number_of_digits))
    return otp


print(generate_otp(6))