import os
import openai
import random
import string
import requests
from dotenv import load_dotenv

# ✅ Load environment variables from .env file
load_dotenv()

# ✅ OpenAI API Key (Loaded from .env)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ✅ Mailgun API settings (Loaded from .env)
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_DOMAIN = "kompanycheck.com"  # Update your domain if necessary
MAILGUN_URL = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages"

# ✅ Generate a random sender email address
def generate_random_email():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{random_string}@{MAILGUN_DOMAIN}"

# ✅ Generate a subject line dynamically
def generate_subject_line():
    subject_options = [
        "Give my money back",
        "Give our money back",
        "Give our due money back",
        "Refund the payment now",
        "Urgent: Settle our dues"
    ]
    return random.choice(subject_options)

# ✅ Modify email content slightly (Uses OpenAI API)
def modify_email_content(original_content):
    prompt = f"Rewrite this email with slight variations:\n{original_content}\nKeep it professional but urgent."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.7
    )

    return response["choices"][0]["message"]["content"]

# ✅ Send email via Mailgun API
def send_email_via_mailgun(recipient_email, subject, body):
    sender_email = generate_random_email()  # Use a new email for each send

    response = requests.post(
        MAILGUN_URL,
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": f"Sachin Arora <{sender_email}>",
            "to": recipient_email,
            "subject": subject,
            "text": body
        }
    )

    if response.status_code == 200:
        print(f"✅ Email sent successfully from {sender_email} to {recipient_email}")
        return True
    else:
        print(f"❌ Failed to send email: {response.text}")
        return False
