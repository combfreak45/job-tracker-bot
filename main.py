"""
Job Tracker Telegram Bot - Main Entry Point
"""
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from src.config import BOT_TOKEN
from src.handlers import JobTrackerHandlers


async def main():
    """Start the bot"""
    # Initialize handlers
    handlers = JobTrackerHandlers()

    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", handlers.start))
    application.add_handler(CommandHandler("help", handlers.help_command))
    application.add_handler(CommandHandler("list", handlers.list_jobs))
    application.add_handler(CommandHandler("applied", handlers.mark_applied))
    application.add_handler(CommandHandler("delete", handlers.delete_job_command))
    application.add_handler(CommandHandler("search", handlers.search_command))
    application.add_handler(CommandHandler("stats", handlers.stats_command))

    # Register message handler
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.handle_message)
    )

    # Initialize application
    await application.initialize()
    await application.start()

    print("🤖 Job Tracker Bot is running...")
    print(f"📱 Bot: @{(await application.bot.get_me()).username}")
    print("Press Ctrl+C to stop")

    # Start polling
    await application.updater.start_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True
    )

    # Keep the bot running
    try:
        # Run forever until interrupted
        stop_event = asyncio.Event()
        await stop_event.wait()
    except (KeyboardInterrupt, SystemExit):
        print("\n🛑 Stopping bot...")
    finally:
        # Cleanup
        await application.updater.stop()
        await application.stop()
        await application.shutdown()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Bot stopped!")
