#!/usr/bin/env python3
"""
Simple example script for sending fake emails
This is a minimal version similar to your original example
"""

import smtplib
from email.mime.text import MIMEText

def send_simple_fake_email():
    """Simple function to send a fake email"""
    
    # Real account credentials (your own mail)
    real_email = "yourrealmail@gmail.com"
    password = "yourpassword"
    
    # Receiver email
    to_email = "receiver@example.com"
    
    # Dummy sender (will show in inbox as "From")
    fake_sender = "support@dummycompany.com"
    
    # Create message
    msg = MIMEText("This is a test email using a dummy sender for display.")
    msg["Subject"] = "Test Email"
    msg["From"] = fake_sender
    msg["To"] = to_email
    
    try:
        # Send
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(real_email, password)
            server.sendmail(fake_sender, to_email, msg.as_string())
        
        print("Mail sent (may show via your Gmail).")
        
    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed. Please check your email and password.")
        print("💡 For Gmail, you might need to use an App Password instead of your regular password.")
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")

if __name__ == "__main__":
    print("⚠️  Remember to update the email credentials in this script before running!")
    print("This is a simple example - use fake_email_sender.py for the full interactive version.")
    send_simple_fake_email()
