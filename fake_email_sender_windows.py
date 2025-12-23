#!/usr/bin/env python3
"""
Fake Email Sender - Windows Compatible Version
A Python program to send emails with a fake sender address for display purposes.
This version is optimized for Windows and avoids getpass issues.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import sys

# Optional import for Word document support
try:
    import mammoth
    WORD_SUPPORT = True
except ImportError:
    WORD_SUPPORT = False


class FakeEmailSender:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

    def convert_word_to_html(self, word_file_path):
        """
        Convert a Word document (.docx) to HTML

        Args:
            word_file_path (str): Path to the Word document

        Returns:
            str: HTML content of the document
        """
        if not WORD_SUPPORT:
            raise ImportError("Word document support requires 'mammoth' library. Install with: pip install mammoth")

        try:
            with open(word_file_path, "rb") as docx_file:
                result = mammoth.convert_to_html(docx_file)
                html_content = result.value

                # Add basic styling to make it look better in emails
                styled_html = f"""
                <html>
                <head>
                    <meta charset="utf-8">
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            line-height: 1.6;
                            color: #333;
                        }}
                        table {{
                            border-collapse: collapse;
                            width: 100%;
                            margin: 10px 0;
                        }}
                        th, td {{
                            border: 1px solid #ddd;
                            padding: 8px;
                            text-align: left;
                        }}
                        th {{
                            background-color: #f2f2f2;
                            font-weight: bold;
                        }}
                    </style>
                </head>
                <body>
                    {html_content}
                </body>
                </html>
                """

                return styled_html

        except Exception as e:
            raise Exception(f"Error converting Word document: {str(e)}")
        
    def send_email(self, real_email, password, to_email, fake_sender, subject, message, attachment_path=None, is_html=False):
        """
        Send an email with a fake sender address

        Args:
            real_email (str): Your real Gmail address
            password (str): Your Gmail password or app password
            to_email (str): Recipient's email address
            fake_sender (str): Fake sender address to display
            subject (str): Email subject
            message (str): Email body content
            attachment_path (str, optional): Path to file to attach
            is_html (bool): Whether the message is HTML formatted
        """
        try:
            # Create message container
            msg = MIMEMultipart()
            
            # Try different techniques to make fake sender more prominent
            msg["From"] = f"{fake_sender} <{fake_sender}>"
            msg["Reply-To"] = fake_sender
            msg["Return-Path"] = fake_sender
            msg["Sender"] = fake_sender
            
            msg["To"] = to_email
            msg["Subject"] = subject
            
            # Add body to email
            msg.attach(MIMEText(message, "html" if is_html else "plain"))
            
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
                server.sendmail(fake_sender, to_email, msg.as_string())
            
            print("✅ Email sent successfully!")
            print(f"📧 From: {fake_sender}")
            print(f"📧 To: {to_email}")
            print(f"📧 Subject: {subject}")
            
        except smtplib.SMTPAuthenticationError:
            print("❌ Authentication failed. Please check your email and password.")
            print("💡 For Gmail, you might need to use an App Password instead of your regular password.")
            print("   Go to: Google Account > Security > 2-Step Verification > App passwords")
        except smtplib.SMTPRecipientsRefused:
            print("❌ Recipient email address was refused.")
        except smtplib.SMTPServerDisconnected:
            print("❌ Server disconnected unexpectedly.")
        except Exception as e:
            print(f"❌ An error occurred: {str(e)}")
    
    def interactive_mode(self):
        """Interactive mode to get email details from user"""
        print("=== Fake Email Sender (Windows Compatible) ===")
        print("This program sends emails with a fake sender address for display purposes.")
        print("Note: This is for educational/testing purposes only.\n")
        
        # Get real email credentials
        real_email = input("Enter your real Gmail address: ").strip()
        if not real_email:
            print("❌ Email address is required.")
            return
            
        # Use regular input instead of getpass to avoid Windows issues
        print("⚠️  Password will be visible as you type (Windows compatibility)")
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

        # Ask for message format
        message_type = input("Send as HTML email? (y/n, allows tables and formatting): ").strip().lower()
        is_html = message_type in ['y', 'yes']

        if is_html:
            print("\nChoose content source:")
            print("1. Type HTML content manually")
            print("2. Read from HTML file")
            if WORD_SUPPORT:
                print("3. Convert Word document (.docx) to HTML")
            else:
                print("3. Word document support (install 'mammoth' with: pip install mammoth)")

            content_choice = input("Enter choice (1-3): ").strip()

            if content_choice == "2":
                html_file = input("Enter path to HTML file: ").strip()
                if os.path.isfile(html_file):
                    with open(html_file, 'r', encoding='utf-8') as f:
                        message = f.read()
                    print(f"✅ HTML content loaded from '{html_file}'")
                else:
                    print(f"❌ File '{html_file}' not found. Switching to manual input.")
                    content_choice = "1"

            elif content_choice == "3" and WORD_SUPPORT:
                word_file = input("Enter path to Word document (.docx): ").strip()
                if os.path.isfile(word_file):
                    try:
                        message = self.convert_word_to_html(word_file)
                        print(f"✅ Word document converted to HTML from '{word_file}'")
                    except Exception as e:
                        print(f"❌ Error converting Word document: {e}")
                        print("Switching to manual input.")
                        content_choice = "1"
                else:
                    print(f"❌ File '{word_file}' not found. Switching to manual input.")
                    content_choice = "1"

            if content_choice not in ["2", "3"] or (content_choice == "3" and not WORD_SUPPORT):
                print("\nEnter HTML message content (press Enter twice when done):")
                print("💡 Tip: Use <table>, <tr>, <td> tags for tables. Example:")
                print("   <table border='1'><tr><th>Header 1</th><th>Header 2</th></tr><tr><td>Data 1</td><td>Data 2</td></tr></table>")
                message_lines = []
                while True:
                    line = input()
                    if line == "" and message_lines and message_lines[-1] == "":
                        break
                    message_lines.append(line)

                message = "\n".join(message_lines[:-1]) if message_lines else "<html><body><p>This is a test HTML email with a dummy sender for display.</p></body></html>"
        else:
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
        self.send_email(real_email, password, to_email, fake_sender, subject, message, attachment_path, is_html)


def main():
    """Main function"""
    sender = FakeEmailSender()
    
    if len(sys.argv) > 1:
        # Command line mode
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print("Fake Email Sender - Windows Compatible")
            print("Usage:")
            print("  python fake_email_sender_windows.py                    # Interactive mode")
            print("  python fake_email_sender_windows.py --help             # Show this help")
            print("\nInteractive mode will prompt you for all required information.")
            print("This version uses regular input instead of getpass for better Windows compatibility.")
            print("\nFeatures:")
            print("• Send emails with fake sender addresses")
            print("• Support for HTML emails with tables")
            print("• Convert Word documents (.docx) to HTML (requires: pip install mammoth)")
            print("• Attach files to emails")
            return
        
        print("❌ Invalid arguments. Use --help for usage information.")
        return
    
    # Interactive mode
    sender.interactive_mode()


if __name__ == "__main__":
    main()
