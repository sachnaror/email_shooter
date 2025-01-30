import time
import random
from celery import shared_task
from django.utils.timezone import now, timedelta
from .models import EmailLog
from .utils import send_email_via_mailgun, modify_email_content, generate_subject_line

@shared_task
def test_task():
    return "✅ Celery is working!"

EMAIL_INTERVAL = timedelta(hours=6)  # 6-hour interval
DAILY_EMAIL_LIMIT = 50  # Max 50 emails per day

# ✅ Read recipients from a text file
def get_email_list():
    file_path = "/Users/homesachin/Desktop/zoneone/email_shooter/email_ids.txt"

    try:
        with open(file_path, "r") as file:
            emails = [line.strip() for line in file.readlines()]
        return emails if emails else []
    except FileNotFoundError:
        print("❌ Error: email_ids.txt not found.")
        return []

# ✅ Read email content from a text file
def get_email_content():
    file_path = "/Users/homesachin/Desktop/zoneone/email_shooter/email_content.txt"

    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("❌ Error: email_content.txt not found.")
        return "Default email content. Please update email_content.txt."

@shared_task
def send_email_task():
    email_list = get_email_list()

    if not email_list:
        print("❌ No emails found in email_ids.txt")
        return

    # ✅ Remove emails that bounced or never opened
    valid_emails = [
        email for email in email_list
        if not EmailLog.objects.filter(recipient=email, opened=False).exists()
    ]

    if not valid_emails:
        print("⚠️ No valid emails to send.")
        return

    # ✅ Enforce daily email limit
    today_sent_count = EmailLog.objects.filter(sent_at__date=now().date()).count()
    if today_sent_count >= DAILY_EMAIL_LIMIT:
        print(f"🚫 Daily email limit reached ({DAILY_EMAIL_LIMIT}), skipping...")
        return

    emails_to_send = valid_emails[:DAILY_EMAIL_LIMIT - today_sent_count]

    for recipient_email in emails_to_send:
        last_email = EmailLog.objects.filter(recipient=recipient_email).order_by('-sent_at').first()

        if last_email and now() - last_email.sent_at < EMAIL_INTERVAL:
            print(f"⏳ Skipping {recipient_email}, last sent at {last_email.sent_at}")
            continue

        # ✅ Generate dynamic subject and modify email content
        subject = generate_subject_line()
        email_body = modify_email_content(get_email_content())

        # ✅ Add email tracking pixel
        email_body += f'\n\n<img src="http://127.0.0.1:8000/track/{recipient_email}/" width="1" height="1">'

        # ✅ Send email via Mailgun
        if send_email_via_mailgun(recipient_email, subject, email_body):
            EmailLog.objects.update_or_create(
                recipient=recipient_email,
                defaults={"sent_at": now(), "opened": False, "clicked_link": False, "subject": subject}
            )
            print(f"✅ Email sent successfully to {recipient_email}")
        else:
            print(f"❌ Failed to send email to {recipient_email}")

        time.sleep(10)  # ✅ Reduced wait time for testing, change to `21600` for production
