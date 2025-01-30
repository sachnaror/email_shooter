# 📩 The Ultimate Email Ninja - ReadMe

## 🎉 Welcome to the Email Automation Madness! 🚀

Hello there, fellow email overlords! 👋 Are you tired of sending emails manually? Wasting your time crafting the same boring messages? Or worse... getting ghosted by your recipients? 😱 Worry not! Enter the **Ultimate Email Ninja** – an advanced, *cunningly sneaky* yet totally **legit** email automation tool that ensures your emails are dynamic, smart, and completely non-spammy (wink wink). 🤭

---

## 🔥 What This Beast Does

- **📩 Sends personalized emails** every 6 hours without repeating the same message.
- **🁏 Uses AI (OpenAI) to tweak content** dynamically so no two recipients see the same exact message.
- **🍮 Randomly picks a different sender email** each time (no patterns, no spam flags, just ✨pure chaos✨).
- **🌍 Uses rotating proxy IPs** to send emails from different locations (stealth mode: ON 🕵️‍♂️).
- **🔍 Tracks email opens and interactions** (so you know who's ghosting you! 👀).
- **💀 Mercilessly removes inactive email IDs** – because why waste your pixels on unread messages?
- **🚫 Ensures no bulk spamming** – Only 50 emails per day, no batch explosion.

---

## 💡 How It Works

1. **🎩 Gathers emails from a text file** (`email_ids.txt`)
2. **📝 Fetches email content from another file** (`email_content.txt`)
3. **🎨 Uses OpenAI to slightly change** each email’s content dynamically.
4. **📤 Shoots emails every 6 hours**, randomly selecting sender IDs.
5. **🔎 Tracks whether the email was opened**, and if not, *poof* ✨that recipient vanishes forever! 😆
6. **♲️ Rinse & Repeat** – Only genuine, engaged recipients keep getting emails.

---

## 🏠 Project Directory Structure

```bash
email_sender_project/
│── email_sender/
│   ├── tasks.py  # Handles scheduling and email dispatching
│   ├── views.py  # Handles email tracking & analytics
│   ├── models.py # Stores email logs & open tracking
│   ├── utils.py  # Generates dynamic content & random sender emails
│── email_content.txt  # File containing the base email content
│── email_ids.txt  # File containing recipient emails (auto-updates)
│── settings.py  # Django settings
│── celery.py  # Celery configuration
│── manage.py  # Django admin management
│── README.md  # You’re reading it, buddy 😆
```

---

## 🏆 Features That Make It LEGENDARY 💪

### **1️⃣ Dynamic Email Content**
💡 *Same message, but never really the same.* OpenAI tweaks every email’s wording so that recipients don’t get bored. No two emails are the same, and spam filters stay clueless. 😎

### **2️⃣ Intelligent Recipient Management**
📩 If someone doesn’t open your email, they are DEAD TO US! Their email gets removed automatically, leaving you only with legit, engaged users. 💀

### **3️⃣ Random Sender Emails**
🎮 Every email comes from a new, randomly generated email address via Mailgun. Spammers send bulk emails from the same ID – we don’t! We’re stealthy like ninjas. 🥷

### **4️⃣ Proxy Rotation for IP Masking**
🕵️ Emails are sent through rotating proxy IPs, making sure you’re not flagged for mass mailing. *Because let’s face it, who likes getting blocked?* 🛇

### **5️⃣ Open Tracking (Who Opened, Who Ignored)**
📊 A sneaky tracking pixel lets us see who’s reading your emails (👀 *we see you, Karen!*). Recipients who open emails remain on the list, while those who don’t *disappear into the void.*

### **6️⃣ Controlled Sending (Not a Spam Cannon)**
🚀 Sends **max 50 emails per day**, with a **6-hour delay per recipient**, so no overloading and no getting flagged. 🎯

---

# 📖 Case: Automated Email Shootings to 40 Emails-ids

## **📌 Overview**
This user story explains how the automated email system works when there are **40 recipient email IDs** in a day.
The system follows:

✅ **Emails sent every 6 hours per recipient**

✅ **Random sender email IDs used for each email**

✅ **Each email has a unique subject & slightly modified content**

✅ **Max 50 emails per day limit applies**

✅ **If the email was not opened, that recipient is removed from future rounds**

---

## **📅 Email Schedule**
| Time Slot  | Emails Sent | Sender Email (Random) | Recipient Email | Subject Line (Generated) | Status |
|------------|------------|----------------------|----------------|--------------------------|--------|
| **00:00 AM** | 10 emails | `user123@mailgun.com` | `email1@example.com` | "Exclusive Offer Just For You" | ✅ Sent |
|            |            | `temp987@mailgun.com` | `email2@example.com` | "Your Special Deal Awaits" | ✅ Sent |
|            |            | `random321@mailgun.com` | `email3@example.com` | "Don't Miss Out Today" | ✅ Sent |
| **06:00 AM** | 10 emails | `coolname456@mailgun.com` | `email4@example.com` | "Limited Time Alert" | ✅ Sent |
|            |            | `promo987@mailgun.com` | `email5@example.com` | "Check This Out Now" | ✅ Sent |
| **12:00 PM** | 10 emails | `dailybuzz234@mailgun.com` | `email6@example.com` | "Update: You Need This!" | ✅ Sent |
|            |            | `hotnews987@mailgun.com` | `email7@example.com` | "Special Deal Ends Soon" | ✅ Sent |
| **06:00 PM** | 10 emails | `funoffer657@mailgun.com` | `email8@example.com` | "Just for You – Act Now" | ✅ Sent |
|            |            | `lucky777@mailgun.com` | `email9@example.com` | "Get This Before It's Gone" | ✅ Sent |

---

## **💡 Key Highlights**
1️⃣ **Each recipient receives an email every 6 hours.**
2️⃣ **Different sender email addresses are used per email.**
3️⃣ **The subject is uniquely generated for each email.**
4️⃣ **Only recipients who opened previous emails remain for future rounds.**
5️⃣ **At the end of the day, non-responsive email IDs are removed.**

---

## **✅ How This Works**
1. **At 00:00 AM, the first batch of emails (10 recipients) is sent.**
2. **Every 6 hours, a new batch of 10 emails is sent.**
3. **After each email batch, the system checks whether recipients opened previous emails.**
4. **If a recipient didn't open any emails, they are removed from the next batch.**
5. **By the end of the day, only engaged users remain for future emails.**

---

## **📌 Next Steps**
🔹 **Want to increase the per-day limit from 50 to 100?**
🔹 **Need email click tracking in addition to open tracking?**
🔹 **Want real-time email response analytics?**

Let me know how we can improve this! 🚀📧
---

## 🚀 How To Run This Beast

### **1️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **2️⃣ Start Redis (for Celery Queue Processing)**
```bash
redis-server
```

### **3️⃣ Start Celery Worker (To Handle Email Tasks)**
```bash
celery -A email_sender_project worker --loglevel=info
```

### **4️⃣ Start Django Server**
```bash
python manage.py runserver
```

### **5️⃣ Trigger Email Sending**
📨 Open your browser and go to:
```bash
http://127.0.0.1:8000/start_email_sending/
```

BOOM 💥 Emails start rolling out like a well-oiled automation machine. 🏃‍♂️

---

## 📩 Contact

| Name              | Details                             |
|-------------------|-------------------------------------|
| **👨‍💻 Developer**   | Sachin Arora                      |
| **💎 Email**       | [schnaror@gmail.com](mailto:schnaror@gmail.com) |
| **📍 Location**    | Noida, India                       |
| **📄 GitHub**      | [github.com/sachnaror](https://github.com/sachnaror?tab=repositories&q=&type=public&language=&sort=) |
| **🌐 Website**     | [https://about.me/sachin-arora](https://about.me/sachin-arora) |
| **📱 WhatsApp**    | [WhatsApp Me](https://wa.me/919560330483?text=Hello%20Sachin) |

