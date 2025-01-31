from twilio.rest import Client

# Twilio credentials
account_sid = 'AC7a5f80ee03788801972b92f73686ee95'
auth_token = '146039babb8a47a5ed2a128f2f517728'
twilio_phone_number = '+12512748049'  # Include the '+' sign before the country code

# Recipient's mobile number
recipient_mobile_number = '+919420574956'  # Include the '+' sign before the country code

# Initialize Twilio client
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
