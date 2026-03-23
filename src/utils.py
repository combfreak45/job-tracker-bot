"""
Utility functions for Job Tracker Bot
"""
import re


def extract_linkedin_info(url):
    """
    Extract company and job info from LinkedIn URL
    Returns: (company_name, job_title)
    """
    company_name = "Unknown Company"
    job_title = "LinkedIn Job Post"

    # Try to extract more info from URL if possible
    # LinkedIn URLs can be complex, this is a basic implementation
    if 'linkedin.com/jobs/view' in url or 'linkedin.com/comm/jobs/view' in url:
        job_title = "LinkedIn Job Post"

    return company_name, job_title


def find_linkedin_urls(text):
    """
    Find all LinkedIn URLs in a text
    Returns: list of URLs
    """
    linkedin_pattern = r'https?://(?:www\.)?linkedin\.com/\S+'
    urls = re.findall(linkedin_pattern, text)
    return urls


def format_job_message(job):
    """
    Format a job tuple into a readable message
    job tuple: (id, company, title, url, date, status)
    """
    job_id, company, title, url, date, status = job

    message = f"*#{job_id}*\n"
    message += f"   🔗 {url}\n"
    message += f"   📅 Added: {date}\n"

    if status != 'pending':
        status_emoji = "✅" if status == "applied" else "ℹ️"
        message += f"   {status_emoji} Status: {status.title()}\n"

    return message
