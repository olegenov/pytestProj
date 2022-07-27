import time
import random

def generate_email():
    return str(time.time()) + "@fakemail.org"


def generate_password():
    password = ''

    for i in range(6):
        password += chr(random.randint(48, 122))
    
    return password
