#!/usr/bin/env python3
"""
Multiple Fake Email Sender
Sends multiple emails to the same recipient, each with a different fake sender address
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time


class MultipleFakeEmailSender:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        
    def send_email(self, real_email, password, to_email, fake_sender, subject, message):
        """
        Send an email with fake sender
        """
        try:
            # Create message container
            msg = MIMEMultipart()
            
            # Set headers to make fake sender more prominent
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
            
            # Connect to server and send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(real_email, password)
                server.sendmail(fake_sender, to_email, msg.as_string())
            
            return True, None
            
        except smtplib.SMTPAuthenticationError as e:
            return False, f"Authentication failed: {str(e)}"
        except smtplib.SMTPRecipientsRefused as e:
            return False, f"Recipient refused: {str(e)}"
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def send_multiple_emails(self, real_email, password, to_email, fake_senders_list, subject, message, delay=2):
        """
        Send multiple emails, one for each fake sender
        
        Args:
            real_email: Your real Gmail address
            password: Your Gmail App Password
            to_email: Recipient email address
            fake_senders_list: List of fake sender email addresses
            subject: Email subject
            message: Email message body
            delay: Delay in seconds between emails (default: 2)
        """
        # Configuration
        print("=" * 70)
        print("🚀 MULTIPLE FAKE EMAIL SENDER")
        print("=" * 70)
        print(f"📧 Real Gmail: {real_email}")
        print(f"📧 Recipient: {to_email}")
        print(f"📧 Subject: {subject}")
        print(f"📧 Total fake senders: {len(fake_senders_list)}")
        print(f"⏱️  Delay between emails: {delay} seconds")
        print("=" * 70)
        print()
        
        # Connect once and reuse connection
        try:
            print("🔌 Connecting to Gmail SMTP server...")
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            print("🔐 Logging in...")
            server.login(real_email, password)
            print("✅ Connected and authenticated successfully!")
            print()
            
            successful = 0
            failed = 0
            failed_senders = []
            
            # Send emails one by one
            for i, fake_sender in enumerate(fake_senders_list, 1):
                fake_sender = fake_sender.strip()  # Remove any whitespace
                if not fake_sender:
                    continue
                
                print(f"[{i}/{len(fake_senders_list)}] 📤 Sending from: {fake_sender}")
                
                try:
                    # Create message
                    msg = MIMEMultipart()
                    msg["From"] = f'"{fake_sender}" <{fake_sender}>'
                    msg["Reply-To"] = fake_sender
                    msg["Return-Path"] = fake_sender
                    msg["Sender"] = fake_sender
                    msg["X-Sender"] = fake_sender
                    msg["X-From"] = fake_sender
                    msg["To"] = to_email
                    msg["Subject"] = subject
                    msg["X-Mailer"] = "Custom Mailer"
                    msg["X-Priority"] = "3"
                    msg.attach(MIMEText(message, "plain"))
                    
                    # Send email
                    server.sendmail(fake_sender, to_email, msg.as_string())
                    successful += 1
                    print(f"      ✅ Success!")
                    
                    # Delay between emails to avoid rate limiting
                    if i < len(fake_senders_list):
                        time.sleep(delay)
                        
                except Exception as e:
                    failed += 1
                    error_msg = str(e)
                    failed_senders.append((fake_sender, error_msg))
                    print(f"      ❌ Failed: {error_msg}")
                    time.sleep(1)  # Short delay even on failure
            
            # Close connection
            server.quit()
            
            # Summary
            print()
            print("=" * 70)
            print("📊 SUMMARY")
            print("=" * 70)
            print(f"✅ Successful: {successful}/{len(fake_senders_list)}")
            print(f"❌ Failed: {failed}/{len(fake_senders_list)}")
            
            if failed_senders:
                print("\n⚠️  Failed senders:")
                for sender, error in failed_senders:
                    print(f"   - {sender}: {error}")
            
            print("=" * 70)
            
        except smtplib.SMTPAuthenticationError:
            print("❌ Authentication failed!")
            print("💡 Please check your Gmail address and App Password.")
        except Exception as e:
            print(f"❌ Connection error: {str(e)}")


def main():
    """Main function with your provided credentials"""
    
    # ⚠️ YOUR CONFIGURATION
    REAL_EMAIL = "somiyasingh041@gmail.com"
    PASSWORD = "epvv pjvd zzii mqmi"  # Remove spaces if needed
    TO_EMAIL = "mohds@gttfoundation.org"
    
    # Multiple fake sender emails (comma-separated)
    FAKE_SENDERS = """hr@acestayz.com,
hr@adeccoindia.com,
hr@androitsynergies.com,
hr@applypolicy.com,
hr@bmapfintech.com,
hr@buzzworksbusiness.com,
hr@hdbfinancial.com,
hr@kotakmahindra.com,
hr@leadtoconnect.com,
hr@mihitinsurance.com,
hr@quesscorp.com,
hr@siddhiinfonet.com,
hr@simplesteploan.com,
hr@vdeals.com,
hr@vprotectimf.com,
hr@yashikafacility.com"""
    
    SUBJECT = "working candidates"
    MESSAGE = "aakriti"
    DELAY_BETWEEN_EMAILS = 2  # seconds (to avoid rate limiting)
    
    # ⚠️ WARNING
    print("\n" + "⚠️" * 35)
    print("WARNING: This script will send multiple emails to the same recipient.")
    print("Make sure you have permission to send these emails!")
    print("⚠️" * 35 + "\n")
    
    response = input("Do you want to continue? (yes/no): ").strip().lower()
    if response not in ['yes', 'y']:
        print("❌ Cancelled by user.")
        return
    
    # Clean password (remove spaces if any)
    password_cleaned = PASSWORD.replace(" ", "")
    
    # Parse fake senders list
    fake_senders_list = [s.strip() for s in FAKE_SENDERS.split(",") if s.strip()]
    
    print(f"\n📋 Configuration:")
    print(f"   Real Email: {REAL_EMAIL}")
    print(f"   Recipient: {TO_EMAIL}")
    print(f"   Fake Senders: {len(fake_senders_list)} addresses")
    print(f"   Subject: {SUBJECT}")
    print(f"   Message: {MESSAGE}")
    print(f"   Delay: {DELAY_BETWEEN_EMAILS} seconds between emails")
    print()
    
    # Initialize sender and send emails
    sender = MultipleFakeEmailSender()
    sender.send_multiple_emails(
        real_email=REAL_EMAIL,
        password=password_cleaned,
        to_email=TO_EMAIL,
        fake_senders_list=fake_senders_list,
        subject=SUBJECT,
        message=MESSAGE,
        delay=DELAY_BETWEEN_EMAILS
    )


if __name__ == "__main__":
    main()
