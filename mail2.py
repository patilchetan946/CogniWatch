import sqlite3
import smtplib
from email.message import EmailMessage

SENDER_EMAIL = "svm892073@gmail.com"
APP_PASSWORD = "xjpbqxdhiywmtuqp"

def send_email(subject, recipients):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = ", ".join(recipients)
    msg.set_content('Suspicious Activity Detected')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
            print("Mail sent successfully")
    except Exception as e:
        print("Failed to send email:", e)

def fetch_recipients_from_database():
    recipients = []
    try:
        conn = sqlite3.connect('evaluation.db')
        cursor = conn.cursor()
        cursor.execute("SELECT Email FROM admin_registration")
        recipients = [row[0] for row in cursor.fetchall()]
    except Exception as e:
        print("Error fetching recipients from database:", e)
    finally:
        cursor.close()
        conn.close()
    return recipients

def detect_suspicious_activity():
    return True  # Replace this with your actual detection logic

def main():
    recipients = fetch_recipients_from_database()
    if recipients:
        if detect_suspicious_activity():
            send_email("Suspicious Activity Detection", recipients)

if __name__ == "__main__":
    main()
