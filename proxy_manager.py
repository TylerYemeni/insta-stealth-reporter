import random import time from instagrapi import Client from utils import create_account, save_account_to_file from proxy_manager import load_proxies, get_random_proxy, get_proxy_dict

تحميل البروكسيات

proxies = load_proxies()

عدد الحسابات المراد إنشاؤها

NUM_ACCOUNTS = 5

for i in range(NUM_ACCOUNTS): proxy = get_random_proxy(proxies) proxy_dict = get_proxy_dict(proxy)

print(f"[*] استخدام البروكسي: {proxy}")

try:
    # إنشاء حساب جديد
    username, password, email = create_account()

    cl = Client()
    cl.set_proxy(proxy_dict)
    cl.login(username, password)

    print(f"[+] تم تسجيل الدخول بالحساب: {username}")
    save_account_to_file(username, password, email)

    time.sleep(random.uniform(5, 10))  # تأخير عشوائي بين الحسابات

except Exception as e:
    print(f"[!] فشل إنشاء الحساب أو تسجيل الدخول: {e}")

