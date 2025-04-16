from instagrapi import Client
from tempmail import create_email_account
import random
import string
import time

def random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def create_ig_account():
    email = create_email_account()
    username = "ig_" + random_string(8)
    password = random_string(12)

    cl = Client()
    try:
        # تسجيل حساب جديد (محاكاة فقط لأن Instagram API لا تسمح بإنشاء الحساب مباشرة)
        print(f"[!] توليد حساب وهمي جاهز:")
        print(f"    البريد: {email}")
        print(f"    المستخدم: {username}")
        print(f"    كلمة السر: {password}")
        
        # يمكن هنا استخدام مكتبات أخرى للتسجيل الحقيقي إذا توفر API خارجي أو محاكاة متصفح آلي
        return {
            "email": email,
            "username": username,
            "password": password
        }
    except Exception as e:
        print(f"[X] فشل إنشاء الحساب: {e}")
        return None
