# 🎯 Job Tracker Bot - Quick Start Guide

## ✅ Setup Complete!

Your bot is ready to use! Bot username: **@arjit_job_tracker_bot**

## 🚀 How to Start the Bot

### Option 1: Using the startup script (Recommended)
```bash
cd /Users/I749429/Desktop/Vibe/job-tracker-bot
./start_bot.sh
```

### Option 2: Manual start
```bash
cd /Users/I749429/Desktop/Vibe/job-tracker-bot
source venv/bin/activate
python main.py
```

The bot will show:
```
🤖 Job Tracker Bot is running...
Press Ctrl+C to stop
```

## 📱 How to Use

### 1. Start the bot on Telegram
- Open Telegram (mobile or web)
- Search for: `@arjit_job_tracker_bot`
- Start a chat and send: `/start`

### 2. Save job posts
When you see ANY LinkedIn job-related URL:
- **Direct job postings** from LinkedIn Jobs
- **Posts about jobs** from people's feeds
- **Company career pages**
- ANY LinkedIn link related to a job opportunity

Just:
- Copy the LinkedIn URL
- Send it to the bot
- The bot will save it and reply with a confirmation

**Example URLs you can save:**
```
https://linkedin.com/jobs/view/123456
https://linkedin.com/posts/john-doe-abc123
https://linkedin.com/company/microsoft/jobs
```

Bot replies:
```
✅ Job saved!
🆔 Job ID: #1
🔗 [link]
Use /list to view all jobs
```

### 3. View your jobs
Send `/list` to see all pending jobs:
```
📋 Pending Jobs:

#1
   🔗 https://linkedin.com/jobs/view/123
   📅 Added: 2026-03-23 14:30

#2
   🔗 https://linkedin.com/posts/abc-123
   📅 Added: 2026-03-23 15:45
```

### 4. Mark as applied
After applying, send: `/applied 1` (replace 1 with job ID)

### 5. Delete a job
Send: `/delete 1` (replace 1 with job ID)

### 6. Search jobs
Send: `/search Google` (replace Google with company name)

### 7. View statistics
Send: `/stats` to see how many jobs you have

## 🎨 All Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/start` | Show welcome message | `/start` |
| `/help` | Show help message | `/help` |
| `/list` | View all pending jobs | `/list` |
| `/applied <id>` | Mark job as applied | `/applied 3` |
| `/delete <id>` | Delete a job | `/delete 5` |
| `/search <query>` | Search by company | `/search Microsoft` |
| `/stats` | View statistics | `/stats` |

## 💡 Tips

1. **Save ANY LinkedIn URL**: Job posts, profile posts about jobs, company pages - anything works!
2. **On Mobile**: Forward or share LinkedIn URLs directly to the bot
3. **Quick Save**: Just paste the URL - no need for commands
4. **Stay Organized**: Mark jobs as applied after submitting applications
5. **Simple Display**: Each job shows just the ID, URL, and when you saved it

## 🛠️ Troubleshooting

### Bot not responding?
1. Make sure the bot script is running on your PC
2. Check that you started the bot with `./start_bot.sh`
3. Look for error messages in the terminal

### Can't find the bot on Telegram?
Search for: `@arjit_job_tracker_bot`

### Want to stop the bot?
Press `Ctrl+C` in the terminal where it's running

## 📂 Files Location

Everything is in: `/Users/I749429/Desktop/Vibe/job-tracker-bot/`

- Database: `jobs.db` (auto-created)
- Logs: Check terminal output
- Config: `.env`

## 🔄 Restarting the Bot

If you close your terminal or restart your computer:
```bash
cd /Users/I749429/Desktop/Vibe/job-tracker-bot
./start_bot.sh
```

---

**Your bot is ready! 🎉**

Open Telegram and search for `@arjit_job_tracker_bot` to get started!
