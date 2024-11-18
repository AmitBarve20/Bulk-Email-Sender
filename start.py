import requests
import json

def send_bulk_emails(api_token, sender_email, subject, message, recipients):
    url = "https://api.mailersend.com/v1/email"

    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    data = {
        "from": sender_email,
        "subject": subject,
        "text": message,
        "recipients": recipients
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("Bulk emails sent successfully.")
    else:
        print("Failed to send bulk emails.")

# Provide your MailerSend API token here
api_token = "mlsn.1dd8d0f880b91f1294a5b685247aed43aed51993d4b7e8145016bc974c10656c"

# Sender's email address
sender_email = "sender@example.com"

# Subject of the email
subject = "Hello from the Bulk Email Sender"

# Message content of the email
message = "This is a sample message for testing the bulk email sender."

# List of recipients' email addresses
recipients = ["amitbarve93@gmail.com", "recipient2@example.com"]

# Call the function to send bulk emails
send_bulk_emails(api_token, sender_email, subject, message, recipients)
