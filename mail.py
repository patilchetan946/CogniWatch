import smtplib
from email.message import EmailMessage

# Step 1: Enable 2-Step Verification in Google Account
# Step 2: Go to "App Passwords" in Google Security Settings
# Step 3: Generate an "App Password" for Mail
# Step 4: Copy and paste the generated password below

SENDER_EMAIL = "example@gmail.com"
APP_PASSWORD = "your-app-password-here"  # Replace with your App Password


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
    recipients = ["example1@gmail.com", "example2@gmail.com", "example3@gmail.com"]

    if detect_suspicious_activity():
        send_email("Suspicious Activity Detection", recipients)


if __name__ == "__main__":
    main()

