"""
Bot command handlers for Job Tracker Bot
"""
from telegram import Update
from telegram.ext import ContextTypes
from .config import ALLOWED_USER_ID, STATUS_PENDING
from .database import JobDatabase
from .utils import extract_linkedin_info, find_linkedin_urls, format_job_message


class JobTrackerHandlers:
    """Handlers for bot commands and messages"""

    def __init__(self):
        self.db = JobDatabase()

    def check_authorization(self, user_id):
        """Check if user is authorized"""
        return user_id == ALLOWED_USER_ID

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send a message when the command /start is issued"""
        if not self.check_authorization(update.effective_user.id):
            await update.message.reply_text("Sorry, you're not authorized to use this bot.")
            return

        welcome_message = """
🎯 *Welcome to Job Tracker Bot!*

*How to use:*
• Forward/send LinkedIn job posts to save them
• Use commands below to manage your list

*Commands:*
/list - View all pending jobs
/applied <id> - Mark job as applied
/delete <id> - Remove a job
/search <company> - Search by company name
/stats - View statistics
/help - Show this message
"""
        await update.message.reply_text(welcome_message, parse_mode='Markdown')

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send help message"""
        await self.start(update, context)

    async def list_jobs(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """List all pending jobs"""
        if not self.check_authorization(update.effective_user.id):
            return

        jobs = self.db.get_jobs(STATUS_PENDING)

        if not jobs:
            await update.message.reply_text("📭 No pending jobs! Your list is empty.")
            return

        message = "📋 *Pending Jobs:*\n\n"
        for job in jobs:
            message += format_job_message(job) + "\n"

        await update.message.reply_text(
            message,
            parse_mode='Markdown',
            disable_web_page_preview=True
        )

    async def mark_applied(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Mark a job as applied"""
        if not self.check_authorization(update.effective_user.id):
            return

        if not context.args:
            await update.message.reply_text("Usage: /applied <job_id>\nExample: /applied 3")
            return

        try:
            job_id = int(context.args[0])
            if self.db.update_job_status(job_id, 'applied'):
                await update.message.reply_text(f"✅ Job #{job_id} marked as applied!")
            else:
                await update.message.reply_text(f"❌ Job #{job_id} not found.")
        except ValueError:
            await update.message.reply_text("Please provide a valid job ID number.")

    async def delete_job_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Delete a job"""
        if not self.check_authorization(update.effective_user.id):
            return

        if not context.args:
            await update.message.reply_text("Usage: /delete <job_id>\nExample: /delete 3")
            return

        try:
            job_id = int(context.args[0])
            if self.db.delete_job(job_id):
                await update.message.reply_text(f"🗑️ Job #{job_id} deleted!")
            else:
                await update.message.reply_text(f"❌ Job #{job_id} not found.")
        except ValueError:
            await update.message.reply_text("Please provide a valid job ID number.")

    async def search_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Search jobs"""
        if not self.check_authorization(update.effective_user.id):
            return

        if not context.args:
            await update.message.reply_text("Usage: /search <company name>\nExample: /search Google")
            return

        query = ' '.join(context.args)
        jobs = self.db.search_jobs(query)

        if not jobs:
            await update.message.reply_text(f"🔍 No jobs found matching '{query}'")
            return

        message = f"🔍 *Search results for '{query}':*\n\n"
        for job in jobs:
            message += format_job_message(job) + "\n"

        await update.message.reply_text(
            message,
            parse_mode='Markdown',
            disable_web_page_preview=True
        )

    async def stats_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show statistics"""
        if not self.check_authorization(update.effective_user.id):
            return

        stats = self.db.get_stats()

        message = f"""
📊 *Job Tracker Statistics*

📋 Total Jobs: {stats['total']}
⏳ Pending: {stats['pending']}
✅ Applied: {stats['applied']}
"""
        await update.message.reply_text(message, parse_mode='Markdown')

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle incoming messages (LinkedIn URLs)"""
        if not self.check_authorization(update.effective_user.id):
            return

        text = update.message.text
        urls = find_linkedin_urls(text)

        if urls:
            for url in urls:
                job_id = self.db.add_job(url)

                await update.message.reply_text(
                    f"✅ *Job saved!*\n\n"
                    f"🆔 Job ID: #{job_id}\n"
                    f"🔗 {url}\n\n"
                    f"Use /list to view all jobs",
                    parse_mode='Markdown',
                    disable_web_page_preview=True
                )
        else:
            await update.message.reply_text(
                "Please send a LinkedIn URL.\n\n"
                "Use /help to see available commands."
            )
