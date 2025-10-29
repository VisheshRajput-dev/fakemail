#!/usr/bin/env python3
"""
Advanced Fake Email Sender
This version tries multiple techniques to make the fake sender more prominent
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import sys


class AdvancedFakeEmailSender:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        
    def send_email(self, real_email, password, to_email, fake_sender, subject, message, attachment_path=None):
        """
        Send an email with enhanced fake sender techniques
        """
        try:
            # Create message container
            msg = MIMEMultipart()
            
            # Multiple techniques to make fake sender more prominent
            msg["From"] = f'"{fake_sender}" <{fake_sender}>'
            msg["Reply-To"] = fake_sender
            msg["Return-Path"] = fake_sender
            msg["Sender"] = fake_sender
            msg["X-Sender"] = fake_sender
            msg["X-From"] = fake_sender
            
            msg["To"] = to_email
            msg["Subject"] = subject
            
            # Add custom headers
            msg["X-Mailer"] = "Custom Mailer"
            msg["X-Priority"] = "3"
            
            # Add body to email
            msg.attach(MIMEText(message, "plain"))
            
            # Add attachment if provided
            if attachment_path and os.path.isfile(attachment_path):
                with open(attachment_path, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                    
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {os.path.basename(attachment_path)}"
                )
                msg.attach(part)
                print(f"Attachment '{os.path.basename(attachment_path)}' added to email.")
            
            # Connect to server and send email
            print(f"Connecting to {self.smtp_server}:{self.smtp_port}...")
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                print("Logging in...")
                server.login(real_email, password)
                print("Sending email...")
                
                # Try sending with fake sender in the envelope
                server.sendmail(fake_sender, to_email, msg.as_string())
            
            print("✅ Email sent successfully!")
            print(f"📧 From: {fake_sender}")
            print(f"📧 To: {to_email}")
            print(f"📧 Subject: {subject}")
            print("\n💡 Note: Gmail may still show your real address for security reasons.")
            print("   The fake sender might appear in some email clients or when replying.")
            
        except smtplib.SMTPAuthenticationError:
            print("❌ Authentication failed. Please check your email and password.")
            print("💡 For Gmail, you might need to use an App Password instead of your regular password.")
        except Exception as e:
            print(f"❌ An error occurred: {str(e)}")
    
    def interactive_mode(self):
        """Interactive mode to get email details from user"""
        print("=== Advanced Fake Email Sender ===")
        print("This version uses multiple techniques to make the fake sender more prominent.")
        print("Note: Gmail may still show your real address for security reasons.\n")
        
        # Get real email credentials
        real_email = input("Enter your real Gmail address: ").strip()
        if not real_email:
            print("❌ Email address is required.")
            return
            
        password = input("Enter your Gmail password (or App Password): ").strip()
        if not password:
            print("❌ Password is required.")
            return
        
        # Get recipient details
        to_email = input("Enter recipient email address: ").strip()
        if not to_email:
            print("❌ Recipient email is required.")
            return
            
        fake_sender = input("Enter fake sender email (e.g., support@dummycompany.com): ").strip()
        if not fake_sender:
            fake_sender = "support@dummycompany.com"
            print(f"Using default fake sender: {fake_sender}")
        
        subject = input("Enter email subject: ").strip()
        if not subject:
            subject = "Test Email"
            print(f"Using default subject: {subject}")
        
        print("\nEnter email message (press Enter twice when done):")
        message_lines = []
        while True:
            line = input()
            if line == "" and message_lines and message_lines[-1] == "":
                break
            message_lines.append(line)
        
        message = "\n".join(message_lines[:-1]) if message_lines else "This is a test email using a dummy sender for display."
        
        # Ask for attachment
        attachment_path = input("\nEnter path to attachment file (optional, press Enter to skip): ").strip()
        if attachment_path and not os.path.isfile(attachment_path):
            print(f"⚠️  Warning: File '{attachment_path}' not found. Sending without attachment.")
            attachment_path = None
        
        # Send email
        print("\n" + "="*50)
        self.send_email(real_email, password, to_email, fake_sender, subject, message, attachment_path)


def main():
    """Main function"""
    sender = AdvancedFakeEmailSender()
    sender.interactive_mode()


if __name__ == "__main__":
    main()
