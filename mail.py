import smtplib
from email.message import EmailMessage

# SENDER_EMAIL = "svm892073@gmail.com"
# APP_PASSWORD = "xjpbqxdhiywmtuqp"

SENDER_EMAIL = "abc@gmail.com"
APP_PASSWORD = "iopiouidhfscwavc"

def send_email(subject, recipients):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = ", ".join(recipients)
    msg.set_content('Suspicious Activity Detected at \n location: \n area: \n take an appropriate actions')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
            print("Mail sent successfully")
    except Exception as e:
        print("Failed to send email:", e)

# Example function to detect suspicious activity
def detect_suspicious_activity():
    return True  # Replace this with your actual detection logic

def main():
    # recipients = ["abc012@gmail.com"]  # Add more email addresses as needed
    recipients = ["ab123@gmail.com", "bcd285@gmail.com", "pqr@gmail.com"]

    if detect_suspicious_activity():
        send_email("Suspicious Activity Detection", recipients)


if __name__ == "__main__":
    main()

