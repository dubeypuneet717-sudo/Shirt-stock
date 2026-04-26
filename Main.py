import requests
import time

# 🔴 REPLACE THESE 2 VALUES
BOT_TOKEN = "8656964634:AAHQE8gxmCgNfIdqOwyrF7GhQSXeVWuznyQ"
CHAT_ID = "290306089"

# Shopify product JSON
URL = "https://tigc.in/products/mens-pink-slim-fit-vertical-striped-casual-shirt-1224-shlnyd-01-03-pink.js"

# Correct Variant ID for M size
TARGET_VARIANT = 50243521937624

def send_telegram(msg):
    try:
        r = requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            params={"chat_id": CHAT_ID, "text": msg}
        )
        print("Telegram response:", r.text)
    except Exception as e:
        print("Telegram error:", e)

def check_stock():
    try:
        data = requests.get(URL).json()

        for v in data["variants"]:
            if v["id"] == TARGET_VARIANT:
                print("Stock status:", v["available"])
                return v["available"]

    except Exception as e:
        print("Stock check error:", e)

    return False

# ✅ Send startup message (so you know it's working)
send_telegram("✅ Bot started and running!")

already_sent = False

while True:
    try:
        stock = check_stock()

        if stock and not already_sent:
            send_telegram("🔥 M size is BACK IN STOCK! Buy fast!")
            already_sent = True

        elif not stock:
            already_sent = False

        time.sleep(60)  # check every 1 minute

    except Exception as e:
        print("Loop error:", e)
        time.sleep(30)
