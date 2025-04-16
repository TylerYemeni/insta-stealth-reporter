from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

def random_string(length=8):
    """إرجاع سلسلة عشوائية من الأحرف والأرقام"""
    return ''.join(random.choices("abcdefghijklmnopqrstuvwxyz1234567890", k=length))

def create_email_account():
    """توليد بريد مؤقت من tempmail (يمكنك تخصيصه أو استخدام API خارجي)"""
    return f"{random_string(8)}@tempmail.com"

def register_instagram_account():
    """تسجيل حساب إنستغرام باستخدام Selenium"""
    email = create_email_account()
    username = f"user_{random_string(8)}"
    password = random_string(12)

    # إعداد المتصفح
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # تشغيل المتصفح في الخلفية
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # فتح صفحة التسجيل في إنستغرام
        driver.get("https://www.instagram.com/accounts/emailsignup/")
        time.sleep(2)

        # تعبئة البيانات في النموذج
        driver.find_element(By.NAME, "emailOrPhone").send_keys(email)
        driver.find_element(By.NAME, "fullName").send_keys(f"User {random_string(5)}")
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)

        # الضغط على زر التسجيل
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

        print(f"[✔️] تم إنشاء الحساب بنجاح:")
        print(f"    البريد: {email}")
        print(f"    المستخدم: {username}")
        print(f"    كلمة السر: {password}")

    except Exception as e:
        print(f"[X] فشل في التسجيل: {e}")

    finally:
        driver.quit()

# اختبار الدالة
if __name__ == "__main__":
    register_instagram_account()
