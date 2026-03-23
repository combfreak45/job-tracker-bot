#!/bin/bash

# Job Tracker Bot Startup Script

cd "$(dirname "$0")"

# Activate virtual environment
source venv/bin/activate

# Start the bot
echo "Starting Job Tracker Bot..."
python main.py
