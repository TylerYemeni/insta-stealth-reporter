main.py

from accounts_generator import create_fake_account from vpn_proxy import rotate_proxy from logger import log_action from instagrapi import Client import time, random

accounts_to_report = [ ("target_account1", 1), ("target_account2", 2), ]

def report_with_fake_account(): for _ in range(3):  # توليد 3 حسابات وهمية بشكل افتراضي email, username, password = create_fake_account() rotate_proxy()  # تبديل البروكسي قبل كل محاولة

cl = Client()
    try:
        cl.set_proxy("http://127.0.0.1:PORT")  # يتم الضبط تلقائياً في vpn_proxy.py
        cl.login(username, password)
        log_action("LOGIN_SUCCESS", username)

        for target, level in accounts_to_report:
            try:
                user_id = cl.user_id_from_username(target)
                cl.user_report(user_id, reason="It's inappropriate")
                log_action("REPORTED", f"{target} by {username}")
                time.sleep(random.uniform(10, 30))
            except Exception as e:
                log_action("REPORT_FAILED", str(e))

    except Exception as e:
        log_action("LOGIN_FAILED", str(e))

if name == "main": report_with_fake_account()

