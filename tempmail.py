import requests
import random
import string

def random_string(length=7):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def create_email_account():
    name = random_string()
    domain = random.choice([
        "1secmail.com", "1secmail.net", "1secmail.org"
    ])
    return f"{name}@{domain}"
