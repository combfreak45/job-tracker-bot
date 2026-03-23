# Job Tracker Telegram Bot

A modular Telegram bot to track LinkedIn job postings for future applications.

## Project Structure

```
job-tracker-bot/
├── main.py              # Entry point
├── src/
│   ├── __init__.py
│   ├── config.py        # Configuration and environment variables
│   ├── database.py      # Database operations
│   ├── handlers.py      # Bot command handlers
│   └── utils.py         # Utility functions
├── .env                 # Environment variables (not in git)
├── requirements.txt     # Python dependencies
└── README.md
```

## Setup

1. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

2. **Configure environment variables:**
   - Edit `.env` file
   - Add your bot token from @BotFather
   - Add your Telegram user ID from @userinfobot

```env
BOT_TOKEN=your_bot_token_here
ALLOWED_USER_ID=your_user_id_here
```

3. **Run the bot:**
```bash
python main.py
```

## Usage

### Saving Jobs
- Send or forward ANY LinkedIn URL to the bot
- Works with: job postings, posts about jobs, company pages, etc.
- The bot will automatically save them to your list

### Commands
- `/start` or `/help` - Show welcome message and commands
- `/list` - View all pending jobs
- `/applied <id>` - Mark job as applied (e.g., `/applied 5`)
- `/delete <id>` - Remove a job (e.g., `/delete 3`)
- `/search <company>` - Search by company name (e.g., `/search Google`)
- `/stats` - View statistics (total, pending, applied)

## Features

✅ Save LinkedIn job posts by forwarding/sending URLs
✅ Track job application status (pending/applied)
✅ Search saved jobs by company name
✅ View statistics
✅ Simple SQLite database storage
✅ Modular, maintainable code structure
✅ Secure: only authorized user can access

## Modules

- **config.py**: Centralized configuration management
- **database.py**: Database operations with JobDatabase class
- **handlers.py**: All bot command handlers in JobTrackerHandlers class
- **utils.py**: Helper functions for URL parsing and formatting
- **main.py**: Application entry point and bot initialization
