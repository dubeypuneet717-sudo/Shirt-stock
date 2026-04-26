import requests
import time

BOT_TOKEN = "8656964634:AAHQE8gxmCgNfIdqOwyrF7GhQSXeVWuznyQ"
CHAT_ID = "8656964634"

URL = "https://tigc.in/products/mens-pink-slim-fit-vertical-striped-casual-shirt-1224-shlnyd-01-03-pink.js"
TARGET_VARIANT = 50243521937624 # M size

def send_telegram(msg):
    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={"chat_id": CHAT_ID, "text": msg}
    )

def check_stock():
    data = requests.get(URL).json()
    for v in data["variants"]:
        if v["id"] == TARGET_VARIANT:
            return v["available"]
    return False

already_sent = False

while True:
    try:
        stock = check_stock()

        if stock and not already_sent:
            send_telegram("🔥 M size is BACK IN STOCK!")
            already_sent = True

        elif not stock:
            already_sent = False

        time.sleep(60)

    except:
        time.sleep(30)
