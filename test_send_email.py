import os
import django
import random
from dotenv import load_dotenv
from app1.utils import send_email_via_mailgun, generate_subject_line, modify_email_content

# ✅ Load environment variables (API Keys)
load_dotenv()

# ✅ Set up Django environment for standalone script
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "email_shooter.settings")
django.setup()

# ✅ Read email IDs from the text file
def get_random_email():
    file_path = "/Users/homesachin/Desktop/zoneone/email_shooter/email_ids.txt"

    if not os.path.exists(file_path):
        print("❌ Error: email_ids.txt file not found.")
        return None

    with open(file_path, "r") as file:
        emails = [line.strip() for line in file.readlines()]

    return random.choice(emails) if emails else None  # Pick a random email

# ✅ Read email content from the text file
def get_email_content():
    file_path = "/Users/homesachin/Desktop/zoneone/email_shooter/email_content.txt"

    if not os.path.exists(file_path):
        print("❌ Error: email_content.txt file not found.")
        return "Default email content. Please update email_content.txt."

    with open(file_path, "r") as file:
        return file.read()

# ✅ Send a test email using Mailgun
def send_test_email():
    recipient_email = get_random_email()
    if not recipient_email:
        print("❌ No valid email found in email_ids.txt")
        return

    subject = generate_subject_line()  # ✅ Generate subject dynamically
    email_body = modify_email_content(get_email_content())  # ✅ Modify email content dynamically

    # ✅ Send email using existing Mailgun function
    success = send_email_via_mailgun(recipient_email, subject, email_body)

    if success:
        print(f"✅ Test email sent successfully to {recipient_email}")
    else:
        print(f"❌ Test email failed to send to {recipient_email}")

# ✅ Run the test email function
if __name__ == "__main__":
    send_test_email()
