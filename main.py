from account_generator import generate_account
from proxy_manager import get_random_proxy, set_proxy
from instagrapi import Client
import time
import random

# تحميل الأهداف من ملف
def load_targets():
    with open("targets.txt", "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

# تنفيذ البلاغات
def report_targets(cl, targets):
    for username in targets:
        try:
            user_id = cl.user_id_from_username(username)
            cl.user_report(user_id, "This account is posting inappropriate content.")
            print(f"[✔] تم إرسال بلاغ على: {username}")
            time.sleep(random.uniform(5, 15))  # تأخير عشوائي
        except Exception as e:
            print(f"[!] فشل بلاغ على {username}: {e}")

def run():
    targets = load_targets()

    # توليد حساب وهمي مع بريد
    account = generate_account()

    # إعداد البروكسي
    proxy = get_random_proxy()
    if proxy:
        set_proxy(proxy)

    # تسجيل الدخول
    cl = Client()
    try:
        cl.login(account["username"], account["password"])
        print(f"[+] تسجيل الدخول بـ: {account['username']}")
        report_targets(cl, targets)
    except Exception as e:
        print(f"[!] فشل تسجيل الدخول: {e}")

if __name__ == "__main__":
    run()
