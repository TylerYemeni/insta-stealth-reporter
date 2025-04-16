import random
import requests

# ملف فيه قائمة بروكسيات، سطر لكل بروكسي بصيغة ip:port أو user:pass@ip:port
PROXY_LIST_FILE = "proxies.txt"

def load_proxies():
    with open(PROXY_LIST_FILE, "r") as f:
        proxies = [line.strip() for line in f if line.strip()]
    return proxies

def get_random_proxy():
    proxies = load_proxies()
    proxy = random.choice(proxies)
    return format_proxy(proxy)

def format_proxy(proxy_str):
    if "@" in proxy_str:
        # With authentication
        auth, ip_port = proxy_str.split("@")
        user, pwd = auth.split(":")
        ip, port = ip_port.split(":")
        return {
            "http": f"http://{user}:{pwd}@{ip}:{port}",
            "https": f"http://{user}:{pwd}@{ip}:{port}"
        }
    else:
        ip, port = proxy_str.split(":")
        return {
            "http": f"http://{ip}:{port}",
            "https": f"http://{ip}:{port}"
        }

def test_proxy(proxy):
    try:
        r = requests.get("http://ip-api.com/json", proxies=proxy, timeout=5)
        if r.status_code == 200:
            print("[+] بروكسي صالح:", r.json()["query"])
            return True
    except:
        pass
    return False

if __name__ == "__main__":
    proxy = get_random_proxy()
    if test_proxy(proxy):
        print("البروكسي جاهز للاستخدام")
    else:
        print("فشل في الاتصال بالبروكسي")
