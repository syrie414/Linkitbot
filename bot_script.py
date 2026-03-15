import os
import asyncio
from telegram import Bot

# جلب البيانات من البيئة (التي عرفتها أنت في ملف الـ YAML)
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
REPO_NAME = os.getenv('REPO_NAME')
COMMIT_MSG = os.getenv('COMMIT_MSG')

async def main():
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("❌ Error: TELEGRAM_TOKEN or CHAT_ID is missing in Secrets!")
        return

    bot = Bot(token=TELEGRAM_TOKEN)
    
    # رسالة احترافية تصلك عند تشغيل الـ Action
    message_text = (
        f"🚀 **Bot is now Online!**\n\n"
        f"📂 **Repository:** `{REPO_NAME}`\n"
        f"📝 **Last Commit:** `{COMMIT_MSG}`\n"
        f"⏳ **Status:** Running on GitHub Actions (5 min session)."
    )

    try:
        await bot.send_message(chat_id=CHAT_ID, text=message_text, parse_mode='Markdown')
        print("✅ Message sent to Telegram!")
    except Exception as e:
        print(f"❌ Failed to send message: {e}")

if __name__ == '__main__':
    asyncio.run(main())

