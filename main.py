import os
import time

print("Bot started...")

TOKEN = os.getenv("DERIV_TOKEN")

if not TOKEN:
    print("No DERIV_TOKEN found. Add it in Settings > Secrets.")
else:
    print("Token found! Bot would connect to Deriv here.")

for i in range(5):
    print(f"Bot is running... {i+1}/5")
    time.sleep(2)

print("Bot finished test run OK")
