# Developer Guide - Job Tracker Bot

Welcome! This guide will help you understand the codebase and get started with development.

## 📚 Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture](#architecture)
3. [Prerequisites & Learning Resources](#prerequisites--learning-resources)
4. [Code Structure](#code-structure)
5. [How It Works](#how-it-works)
6. [Development Setup](#development-setup)
7. [Adding New Features](#adding-new-features)
8. [Deployment](#deployment)

---

## 🎯 Project Overview

**What is this?**
A Telegram bot that helps users track LinkedIn job postings they want to apply to later.

**Why was it built?**
- Users see job posts on LinkedIn while scrolling
- They want to save them for later without cluttering WhatsApp
- Need a simple way to track which jobs they've applied to

**Core functionality:**
- Save LinkedIn URLs (any type: job posts, profile posts, company pages)
- List all saved jobs
- Mark jobs as "applied"
- Delete jobs
- Search by company name
- View statistics

---

## 🏗️ Architecture

### High-Level Design

```
User (Telegram)
    ↕️
Telegram Bot API
    ↕️
Our Bot (Python)
    ↕️
SQLite Database
```

### Modular Structure

We follow a **modular architecture** to keep code organized and maintainable:

```
job-tracker-bot/
├── main.py                 # Entry point - starts the bot
├── src/                    # Core application code
│   ├── config.py          # Configuration & environment variables
│   ├── database.py        # Database operations (CRUD)
│   ├── handlers.py        # Bot command handlers
│   └── utils.py           # Helper functions
├── requirements.txt        # Python dependencies
└── .env                   # Environment variables (not in git)
```

**Why modular?**
- ✅ **Separation of Concerns**: Each file has one responsibility
- ✅ **Easy to Test**: Can test each module independently
- ✅ **Easy to Extend**: Add features without touching existing code
- ✅ **Easy to Debug**: Know exactly where to look for issues

---

## 📖 Prerequisites & Learning Resources

### What You Need to Know

#### 1. **Python Basics** (Essential)
- Variables, functions, classes
- Async/await (asynchronous programming)
- Imports and modules
- Exception handling

**Resources:**
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Asyncio Basics](https://docs.python.org/3/library/asyncio.html)

#### 2. **Telegram Bot API** (Important)
- How Telegram bots work
- Commands, messages, and handlers
- Bot authorization

**Resources:**
- [Telegram Bot API Docs](https://core.telegram.org/bots/api)
- [python-telegram-bot Tutorial](https://github.com/python-telegram-bot/python-telegram-bot/wiki)

#### 3. **SQLite/Databases** (Helpful)
- Basic SQL (SELECT, INSERT, UPDATE, DELETE)
- Database schema design

**Resources:**
- [SQLite Tutorial](https://www.sqlitetutorial.net/)

#### 4. **Git/GitHub** (Helpful)
- Basic git commands
- Clone, commit, push, pull

**Resources:**
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)

---

## 📁 Code Structure

### File-by-File Breakdown

#### **`main.py`** - Entry Point
**Purpose:** Starts the bot and registers all handlers

```python
# What it does:
1. Creates bot application
2. Registers command handlers (/start, /list, etc.)
3. Starts polling for messages
4. Keeps bot running 24/7
```

**Key concepts:**
- `Application.builder()` - Creates the bot
- `add_handler()` - Registers commands
- `run_polling()` - Starts listening for messages

---

#### **`src/config.py`** - Configuration
**Purpose:** Centralized configuration management

```python
# What it does:
1. Loads environment variables from .env
2. Stores bot token and user ID
3. Defines constants (database name, status values)
```

**Why separate config?**
- ✅ All settings in one place
- ✅ Easy to change without touching code
- ✅ Keeps secrets out of code (security)

---

#### **`src/database.py`** - Database Layer
**Purpose:** All database operations

```python
# What it does:
1. Creates database tables
2. Adds jobs to database
3. Retrieves jobs (all, by status, by ID)
4. Updates job status
5. Deletes jobs
6. Searches jobs
7. Gets statistics
```

**Class: `JobDatabase`**
- Encapsulates all database logic
- Uses SQLite (lightweight, file-based database)
- CRUD operations: Create, Read, Update, Delete

**Database Schema:**
```sql
jobs (
    id INTEGER PRIMARY KEY,
    company_name TEXT,
    job_title TEXT,
    linkedin_url TEXT,
    date_added TEXT,
    status TEXT  -- 'pending' or 'applied'
)
```

**Why a class?**
- ✅ Reusable across the app
- ✅ Easy to test
- ✅ Can swap database later (e.g., PostgreSQL)

---

#### **`src/handlers.py`** - Bot Logic
**Purpose:** Handles all user commands and messages

```python
# What it does:
1. Checks user authorization
2. Handles /start, /list, /applied, /delete, /search, /stats
3. Processes incoming messages (LinkedIn URLs)
4. Formats and sends responses
```

**Class: `JobTrackerHandlers`**
- One method per command
- Each method is async (non-blocking)
- Uses `database.py` to store/retrieve data

**Flow example - User sends a LinkedIn URL:**
```
1. User sends URL → Telegram API → Our bot
2. handle_message() receives it
3. Checks if user is authorized
4. Extracts LinkedIn URL from message
5. Calls database.add_job(url)
6. Sends confirmation to user
```

---

#### **`src/utils.py`** - Helper Functions
**Purpose:** Utility functions used across the app

```python
# What it does:
1. extract_linkedin_info() - Parse LinkedIn URLs
2. find_linkedin_urls() - Find URLs in text using regex
3. format_job_message() - Format job data for display
```

**Why separate utils?**
- ✅ Reusable functions
- ✅ Keeps handlers.py cleaner
- ✅ Easy to test independently

---

## ⚙️ How It Works

### User Journey: Saving a Job

```
1. User sees job on LinkedIn
   ↓
2. Copies LinkedIn URL
   ↓
3. Opens Telegram → Sends URL to bot
   ↓
4. Bot receives message
   ↓
5. handlers.handle_message() is called
   ↓
6. Checks authorization (only you can use bot)
   ↓
7. Extracts URL from message (utils.find_linkedin_urls)
   ↓
8. Saves to database (database.add_job)
   ↓
9. Sends confirmation to user
   ↓
10. User sees: "✅ Job saved! ID: #5"
```

### User Journey: Viewing Jobs

```
1. User sends /list
   ↓
2. Bot receives command
   ↓
3. handlers.list_jobs() is called
   ↓
4. Gets all pending jobs (database.get_jobs('pending'))
   ↓
5. Formats each job (utils.format_job_message)
   ↓
6. Sends formatted list to user
   ↓
7. User sees all saved jobs with IDs and links
```

### User Journey: Marking as Applied

```
1. User sends /applied 5
   ↓
2. handlers.mark_applied() is called
   ↓
3. Extracts job ID from command (context.args[0])
   ↓
4. Updates database (database.update_job_status(5, 'applied'))
   ↓
5. Sends confirmation: "✅ Job #5 marked as applied!"
```

---

## 🛠️ Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/combfreak45/job-tracker-bot.git
cd job-tracker-bot
```

### 2. Create Virtual Environment

```bash
# Create venv
python3 -m venv venv

# Activate it
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file:

```env
BOT_TOKEN=your_test_bot_token_here
ALLOWED_USER_ID=your_telegram_user_id
```

**Getting a test bot token:**
1. Message [@BotFather](https://t.me/BotFather) on Telegram
2. Send `/newbot`
3. Follow instructions
4. Copy the token

**Getting your user ID:**
1. Message [@userinfobot](https://t.me/userinfobot)
2. It will show your user ID

### 5. Run the Bot

```bash
python main.py
```

You should see:
```
🤖 Job Tracker Bot is running...
📱 Bot: @your_bot_username
Press Ctrl+C to stop
```

### 6. Test It

- Open Telegram
- Search for your bot
- Send `/start`
- Try saving a LinkedIn URL!

---

## 🚀 Adding New Features

### Example: Add a `/clear` Command to Delete All Jobs

#### Step 1: Add Database Method

**File: `src/database.py`**

```python
def clear_all_jobs(self):
    """Delete all jobs from database"""
    conn = self._get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM jobs')
    deleted_count = cursor.rowcount
    conn.commit()
    conn.close()
    return deleted_count
```

#### Step 2: Add Handler

**File: `src/handlers.py`**

```python
async def clear_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Clear all jobs"""
    if not self.check_authorization(update.effective_user.id):
        return

    count = self.db.clear_all_jobs()
    await update.message.reply_text(
        f"🗑️ Cleared {count} jobs from your list!"
    )
```

#### Step 3: Register Handler

**File: `main.py`**

```python
# Add this line with other handlers:
application.add_handler(CommandHandler("clear", handlers.clear_command))
```

#### Step 4: Test It

```bash
python main.py
```

Send `/clear` to your bot!

---

### Example: Add Email Notifications

**What you'd need:**
1. Add email configuration to `config.py`
2. Create `src/email_service.py` for sending emails
3. Modify `handlers.py` to send email when job is added
4. Add email library to `requirements.txt` (e.g., `smtplib`)

---

## 🚢 Deployment

### Current Setup: Railway

The bot is deployed on [Railway](https://railway.app) for 24/7 hosting.

**How it works:**
1. Code is pushed to GitHub
2. Railway watches the repo
3. On push, Railway automatically:
   - Pulls latest code
   - Installs dependencies
   - Restarts the bot

**Environment variables are set in Railway dashboard:**
- `BOT_TOKEN`
- `ALLOWED_USER_ID`

### Deploying Changes

```bash
# Make your changes
git add .
git commit -m "Add new feature"
git push

# Railway auto-deploys!
```

### Monitoring

**Railway Dashboard:**
- **Logs**: See what's happening in real-time
- **Metrics**: CPU/Memory usage
- **Deploy**: Manual redeploy if needed

---

## 🐛 Common Issues & Debugging

### Issue: Bot not responding

**Check:**
1. Is bot running? Check Railway logs
2. Is BOT_TOKEN correct?
3. Did you send `/start` first?

### Issue: "Not authorized" message

**Fix:**
- Verify ALLOWED_USER_ID matches your Telegram user ID

### Issue: Database changes not persisting

**Note:**
- Railway uses ephemeral storage
- Database resets on redeploy
- For persistent storage, use external database (upgrade)

### Debugging Tips

**Add logging:**
```python
import logging
logging.basicConfig(level=logging.INFO)
```

**Print statements:**
```python
print(f"User sent: {update.message.text}")
```

**Check Railway logs:**
- Go to Railway dashboard
- Click on your service
- View "Logs" tab

---

## 📚 Further Learning

### Next Steps

1. **Add unit tests** - Learn `pytest`
2. **Add webhook support** - More efficient than polling
3. **Use PostgreSQL** - For persistent storage
4. **Add more commands** - `/remind`, `/export`, etc.
5. **Add inline keyboards** - Better UX with buttons
6. **Add error handling** - Try/except blocks
7. **Add rate limiting** - Prevent spam

### Resources

- [python-telegram-bot Examples](https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples)
- [Telegram Bot Best Practices](https://core.telegram.org/bots/faq)
- [Python Async Programming](https://realpython.com/async-io-python/)

---

## 🤝 Contributing

Want to improve the bot?

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Commit: `git commit -m "Add feature"`
6. Push: `git push origin feature-name`
7. Create a Pull Request

---

## 📧 Questions?

If you're stuck or have questions:
1. Check existing code comments
2. Read python-telegram-bot docs
3. Search GitHub issues
4. Ask in discussions

---

**Happy Coding!** 🚀

Built with ❤️ using Python and Telegram Bot API
