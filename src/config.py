"""
Configuration module for Job Tracker Bot
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
ALLOWED_USER_ID = int(os.getenv('ALLOWED_USER_ID', '0'))

# Database Configuration
DB_NAME = 'jobs.db'

# Job Status
STATUS_PENDING = 'pending'
STATUS_APPLIED = 'applied'
