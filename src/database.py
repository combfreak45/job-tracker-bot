"""
Database module for Job Tracker Bot
Handles all database operations
"""
import sqlite3
from datetime import datetime
from .config import DB_NAME, STATUS_PENDING


class JobDatabase:
    """Handle all database operations for jobs"""

    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name
        self.init_db()

    def _get_connection(self):
        """Get database connection"""
        return sqlite3.connect(self.db_name)

    def init_db(self):
        """Initialize the SQLite database"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name TEXT,
                job_title TEXT,
                linkedin_url TEXT,
                date_added TEXT,
                status TEXT DEFAULT 'pending'
            )
        ''')
        conn.commit()
        conn.close()

    def add_job(self, url, company=None, title=None):
        """Add a job to the database"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO jobs (linkedin_url, date_added, status)
            VALUES (?, ?, ?)
        ''', (url, datetime.now().strftime('%Y-%m-%d %H:%M'), STATUS_PENDING))
        job_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return job_id

    def get_jobs(self, status=None):
        """Get all jobs, optionally filtered by status"""
        conn = self._get_connection()
        cursor = conn.cursor()

        if status:
            cursor.execute('SELECT * FROM jobs WHERE status = ? ORDER BY id DESC', (status,))
        else:
            cursor.execute('SELECT * FROM jobs ORDER BY id DESC')

        jobs = cursor.fetchall()
        conn.close()
        return jobs

    def get_job_by_id(self, job_id):
        """Get a specific job by ID"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM jobs WHERE id = ?', (job_id,))
        job = cursor.fetchone()
        conn.close()
        return job

    def update_job_status(self, job_id, status):
        """Update job status"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE jobs SET status = ? WHERE id = ?', (status, job_id))
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0

    def delete_job(self, job_id):
        """Delete a job"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM jobs WHERE id = ?', (job_id,))
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0

    def search_jobs(self, query):
        """Search jobs by company name or job title"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM jobs
            WHERE company_name LIKE ? OR job_title LIKE ?
            ORDER BY id DESC
        ''', (f'%{query}%', f'%{query}%'))
        jobs = cursor.fetchall()
        conn.close()
        return jobs

    def get_stats(self):
        """Get statistics about jobs"""
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT COUNT(*) FROM jobs')
        total = cursor.fetchone()[0]

        cursor.execute('SELECT COUNT(*) FROM jobs WHERE status = ?', (STATUS_PENDING,))
        pending = cursor.fetchone()[0]

        cursor.execute('SELECT COUNT(*) FROM jobs WHERE status != ?', (STATUS_PENDING,))
        applied = cursor.fetchone()[0]

        conn.close()
        return {
            'total': total,
            'pending': pending,
            'applied': applied
        }
