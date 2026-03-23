# Job Tracker Telegram Bot

A modular Telegram bot to track LinkedIn job postings for future applications.

**Bot**: [@arjit_job_tracker_bot](https://t.me/arjit_job_tracker_bot)

**Deployed on**: Railway (24/7 hosting)

## Features

✅ Save any LinkedIn URL (job posts, profile posts, company pages)
✅ Track job application status (pending/applied)
✅ Search and manage saved jobs
✅ View statistics
✅ Simple SQLite database storage
✅ Modular, maintainable code structure
✅ Secure: only authorized user can access

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
├── requirements.txt     # Python dependencies
└── README.md
```

## Usage

See [USAGE_GUIDE.md](USAGE_GUIDE.md) for detailed instructions.

### Quick Start
- Search for [@arjit_job_tracker_bot](https://t.me/arjit_job_tracker_bot) on Telegram
- Send `/start` to begin
- Forward any LinkedIn URL to save it
- Use `/list` to view saved jobs

### Commands
- `/start` or `/help` - Show welcome message and commands
- `/list` - View all pending jobs
- `/applied <id>` - Mark job as applied (e.g., `/applied 5`)
- `/delete <id>` - Remove a job (e.g., `/delete 3`)
- `/search <company>` - Search by company name (e.g., `/search Google`)
- `/stats` - View statistics (total, pending, applied)

## Local Development

1. **Clone the repository:**
```bash
git clone https://github.com/combfreak45/job-tracker-bot.git
cd job-tracker-bot
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables:**
Create a `.env` file:
```env
BOT_TOKEN=your_bot_token_here
ALLOWED_USER_ID=your_user_id_here
```

4. **Run locally:**
```bash
python main.py
```

Or use the startup script:
```bash
./start_bot.sh
```

## Deployment

Currently deployed on **Railway** with 24/7 uptime.

To deploy your own instance:
1. Fork this repository
2. Sign up on [Railway](https://railway.app)
3. Create new project from your GitHub repo
4. Add environment variables: `BOT_TOKEN` and `ALLOWED_USER_ID`
5. Deploy!

## Tech Stack

- **Python 3.11+**
- **python-telegram-bot 21.10** - Telegram Bot API wrapper
- **SQLite** - Lightweight database
- **python-dotenv** - Environment variable management

## Modules

- **config.py**: Centralized configuration management
- **database.py**: Database operations with JobDatabase class
- **handlers.py**: All bot command handlers in JobTrackerHandlers class
- **utils.py**: Helper functions for URL parsing and formatting
- **main.py**: Application entry point and bot initialization
