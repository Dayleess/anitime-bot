# Bot token
TOKEN = "8750613464:AAH2xaRWqVdUIuLw1BcvXOn-RW-xw8RwvyU"

# Admin Telegram ID'lari (o'zingizning ID'ingizni kiriting)
ADMIN_IDS = [6981254334]  # <-- shu yerga o'z Telegram ID'ingizni qo'ying

# Majburiy obuna kanallari (username yoki -100xxxxxxxx formatda ID)
REQUIRED_CHANNELS = [
    {"name": "Dayleess Donat", "username": "@Dayleess_Donat", "url": "https://t.me/Dayleess_Donat"},
    # Qo'shimcha kanal qo'shish uchun yuqoridagi formatda yozing
]
# Kanalga post joylash uchun kanal username yoki ID si
POST_CHANNEL = "@AniTime_here" 

# Ma'lumotlar bazasi (Cloud uchun PostgreSQL, aks holda SQLite)
import os
DATABASE_URL = os.getenv("DATABASE_URL") # Masalan: postgres://user:pass@host:port/db
