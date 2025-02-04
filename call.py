from twilio.rest import Client

# Step 1: Sign up on Twilio and verify your phone number
# Step 2: Go to Twilio Console (https://www.twilio.com/console)
# Step 3: Get your Account SID and Auth Token
# Step 4: Replace the dummy credentials below with your actual details

# Twilio credentials (Use environment variables for security)
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'  # Replace with your Account SID
auth_token = 'your-auth-token-here'  # Replace with your Auth Token
twilio_phone_number = '+1234567890'  # Replace with your Twilio phone number

# Recipient's mobile number (Ensure it's in international format)
recipient_mobile_number = '+91987xxxxx10'  # Replace with the recipient's number

# Step 5: Use this script to send messages via Twilio
client = Client(account_sid, auth_token)

def make_phone_call():
    message = "Suspicious Activity Detected. Please check immediately."

    try:
        call = client.calls.create(
            twiml=f'<Response><Say>{message}</Say></Response>',
            to=recipient_mobile_number,
            from_=twilio_phone_number
        )
        print(f"Call SID: {call.sid}")
    except Exception as e:
        print(f"Error making call: {e}")

# Example function to detect suspicious activity
def detect_suspicious_activity():
    return True  # Replace this with your actual detection logic

def main():
    if detect_suspicious_activity():
        make_phone_call()

if __name__ == "__main__":
    main()
