import requests
import random
import string
import time
from instagrapi import Client

MAIL_API = "https://www.1secmail.com/api/v1/"
DOMAINS = ["1secmail.com", "1secmail.org", "1secmail.net"]

def generate_username():
    return "user" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

def generate_email():
    name = generate_username()
    domain = random.choice(DOMAINS)
    return f"{name}@{domain}", name, domain

def wait_for_email(login, domain):
    for _ in range(20):
        time.sleep(5)
        res = requests.get(f"{MAIL_API}?action=getMessages&login={login}&domain={domain}")
        if res.json():
            return res.json()[0]["id"]
    return None

def read_email(login, domain, msg_id):
    res = requests.get(f"{MAIL_API}?action=readMessage&login={login}&domain={domain}&id={msg_id}")
    return res.json()

def create_account():
    email, login, domain = generate_email()
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    username = generate_username()

    # تسجيل دخول إلى إنستغرام – اختياري للمحاكاة فقط، لأن التسجيل الكامل يحتاج تحديات
    cl = Client()
    print(f"تم توليد الحساب: {email} | كلمة السر: {password}")
    
    # ملاحظة: عملية التسجيل تحتاج تخطي reCAPTCHA وتأكيد بالبريد (وهذا صعب يتم بالكامل تلقائيًا)

    return {
        "username": username,
        "password": password,
        "email": email
    }

if __name__ == "__main__":
    account = create_account()
