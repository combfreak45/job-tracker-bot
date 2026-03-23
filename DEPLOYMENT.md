# Job Tracker Telegram Bot - Deployment Guide

## Deploying to Render

This bot is ready to deploy to Render's free tier for 24/7 hosting.

### Prerequisites
- GitHub account
- Render account (free): https://render.com

### Deployment Steps

#### 1. Push to GitHub

```bash
cd /Users/I749429/Desktop/Vibe/job-tracker-bot

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Job Tracker Bot"

# Create a new repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/job-tracker-bot.git
git branch -M main
git push -u origin main
```

#### 2. Deploy on Render

1. Go to https://render.com and sign up/login
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: `job-tracker-bot`
   - **Environment**: `Python 3`
   - **Build Command**: `./render-build.sh`
   - **Start Command**: `python main.py`
   - **Plan**: `Free`

5. Add Environment Variables:
   - Click "Environment" tab
   - Add:
     - `BOT_TOKEN` = `your_bot_token`
     - `ALLOWED_USER_ID` = `your_user_id`

6. Click "Create Web Service"

#### 3. Wait for Deployment

Render will build and deploy your bot (takes 2-3 minutes).

Once deployed, your bot will run 24/7!

### Important Notes

- **Free tier limitations**:
  - Bot may sleep after 15 minutes of inactivity
  - 750 hours/month free (plenty for one bot)

- **Database**:
  - SQLite database will reset on each deploy
  - For persistent storage, upgrade to paid tier or use external database

### Monitoring

- View logs: Render Dashboard → Your Service → Logs
- Check status: Dashboard shows if bot is running
- Restart: Dashboard → Manual Deploy → Clear build cache & deploy

### Troubleshooting

If bot doesn't start:
1. Check logs in Render dashboard
2. Verify environment variables are set correctly
3. Make sure GitHub repo has all files committed
