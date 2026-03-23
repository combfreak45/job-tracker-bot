"""
Test script to verify bot token and connectivity
"""
import asyncio
from src.config import BOT_TOKEN
from telegram import Bot


async def test_bot():
    """Test bot connectivity"""
    print(f"Testing bot with token: {BOT_TOKEN[:15]}...")

    bot = Bot(token=BOT_TOKEN)

    try:
        print("Attempting to connect to Telegram...")
        me = await bot.get_me()
        print(f"✅ Success! Bot connected: @{me.username}")
        print(f"Bot name: {me.first_name}")
        print(f"Bot ID: {me.id}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    finally:
        # Cleanup
        await bot.close()


if __name__ == '__main__':
    asyncio.run(test_bot())
