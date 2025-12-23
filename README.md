# Fake Email Sender 🔐

A Python program that sends emails with a fake sender address for display purposes. This tool is designed for **educational, testing, and legitimate purposes only**.

---

## ⚠️ **CRITICAL WARNINGS - READ BEFORE USE**

### 🚨 **Legal Warning**
- **This tool may be illegal in your jurisdiction** - Email spoofing is prohibited by law in many countries
- **Using this tool for malicious purposes (phishing, fraud, impersonation) is a serious crime**
- **You may face criminal charges, fines, or imprisonment for misuse**
- **The authors/developers are NOT responsible for any illegal use**

### 🛡️ **Security & Ethics Warning**
- **Gmail and other email providers have security measures** that show the real sender
- **Fake sender addresses may not work as expected** - recipients may still see your real email
- **This tool does NOT guarantee anonymity** - your real email is always traceable
- **Only use with explicit consent** from recipients (e.g., authorized testing)
- **Do NOT use to impersonate real companies, organizations, or individuals**

### 📧 **Email Provider Limitations**
- **Gmail will show your real sender address** despite the fake sender field
- **Most modern email providers detect and prevent sender spoofing**
- **The fake sender may only appear in email headers, not in the inbox view**
- **Recipients can always see your real email address through email headers**

### ✅ **Acceptable Use Cases**
- Educational purposes (learning how email works)
- Testing your own email systems
- Authorized penetration testing (with permission)
- Development and debugging (on your own systems)

---

## 📋 **Requirements**

### **System Requirements**
- **Operating System**: Windows 10/11, Linux, or macOS
- **Python Version**: Python 3.6 or higher
- **Internet Connection**: Required for sending emails

### **Gmail Account Requirements**
- ✅ Active Gmail account
- ✅ **2-Factor Authentication (2FA) enabled** (required)
- ✅ **App Password generated** (cannot use regular password)
- ✅ Account must have "Less secure app access" capability (if applicable)

### **Software Dependencies**
- ✅ **No external packages needed!** (uses only Python standard library)
- ✅ All dependencies are included with Python:
  - `smtplib` (email sending)
  - `email` (email formatting)
  - `getpass` (secure password input)
  - `os` (file operations)
  - `sys` (command-line arguments)

### **Knowledge Requirements**
- Basic understanding of command-line interface
- Ability to generate Gmail App Passwords
- Understanding of email security implications

---

## 🚀 **Installation & Setup**

### **Step 1: Install Python**

**Windows:**
1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, check ✅ "Add Python to PATH"
3. Verify installation:
   ```cmd
   python --version
   ```

**Linux/macOS:**
- Usually pre-installed
- If not: `sudo apt-get install python3` (Linux) or use Homebrew (macOS)

### **Step 2: Enable Gmail App Password**

1. **Go to Google Account**: [myaccount.google.com](https://myaccount.google.com)
2. **Enable 2-Step Verification**:
   - Security → 2-Step Verification → Turn it on
3. **Generate App Password**:
   - Security → 2-Step Verification → App passwords
   - Select "Mail" as app type
   - Select "Other (Custom name)" as device
   - Enter name: "Fake Email Sender"
   - Click "Generate"
   - **Copy the 16-character password** (you'll need it!)

### **Step 3: Download/Clone Project**

```cmd
git clone <repository-url>
cd fakemail
```

Or download and extract the ZIP file.

### **Step 4: Verify Files**

Make sure these files exist:
- ✅ `fake_email_sender.py` (main program)
- ✅ `fake_email_sender_windows.py` (Windows-optimized version)
- ✅ `advanced_fake_email_sender.py` (advanced version)
- ✅ `simple_example.py` (simple example)
- ✅ `requirements.txt` (dependency info)
- ✅ `README.md` (this file)

---

## 💻 **Usage Instructions**

### **Windows Command Prompt (CMD)**

#### **Option 1: Standard Version**
```cmd
cd C:\Repos\fakemail
python fake_email_sender.py
```

#### **Option 2: Windows-Optimized Version (Recommended for Windows)**
```cmd
cd C:\Repos\fakemail
python fake_email_sender_windows.py
```
*This version avoids getpass issues on Windows*

#### **Option 3: Advanced Version**
```cmd
```

#### **Option 4: Simple Example**
```cmd
python simple_example.py
```
*⚠️ Edit `simple_example.py` first to add your credentials!*

### **Windows PowerShell**

Same commands as CMD:
```powershell
cd C:\Repos\fakemail
python fake_email_sender_windows.py
```

### **Linux/macOS Terminal**

```bash
cd /path/to/fakemail
python3 fake_email_sender.py
```

### **Interactive Mode Workflow**

1. **Run the program**:
   ```cmd
   python fake_email_sender_windows.py
   ```

2. **Follow the prompts**:
   ```
   Enter your real Gmail address: yourrealmail@gmail.com
   Enter your Gmail password (or App Password): [paste your 16-char app password]
   Enter recipient email address: recipient@example.com
   Enter fake sender email: support@dummycompany.com
   Enter email subject: Test Email
   Enter email message: [type your message, press Enter twice when done]
   Enter path to attachment file: [optional, press Enter to skip]
   ```

3. **Wait for confirmation**:
   ```
   ✅ Email sent successfully!
   ```

---

## 📁 **Project Files Description**

| File | Description | Recommended For |
|------|-------------|-----------------|
| `fake_email_sender.py` | Main program with fallback for getpass | All platforms |
| `fake_email_sender_windows.py` | Windows-optimized (no getpass issues) | **Windows users** |
| `advanced_fake_email_sender.py` | Advanced version with extra headers | Testing/development |
| `simple_example.py` | Minimal example code | Learning/reference |
| `requirements.txt` | Dependency information | Reference only |
| `README.md` | Complete documentation | All users |

---

## 🔧 **How It Works**

### **Technical Process**

1. **Connection**: Program connects to Gmail SMTP server (`smtp.gmail.com:587`)
2. **Authentication**: Logs in with your real Gmail credentials
3. **Message Creation**: Builds email with fake sender in headers
4. **Sending**: Sends email through Gmail's servers
5. **Display**: Recipient's email client processes headers

### **Email Headers Used**

The program sets these headers:
- `From`: Fake sender address
- `Reply-To`: Fake sender address
- `Return-Path`: Fake sender address
- `Sender`: Fake sender address
- `X-Sender`: Fake sender address (custom header)

### **Limitations**

- ✅ **Gmail inbox view will show real sender** (security feature)
- ✅ **Email headers will contain fake sender** (checkable)
- ✅ **Reply-To may work** in some email clients
- ✅ **Real sender always traceable** through email headers
- ✅ **SPF/DKIM/DMARC records** may cause rejection

---

## 🐛 **Troubleshooting**

### **Problem: Password Input Freezes**

**Windows CMD Issue:**
```cmd
# Use Windows-optimized version instead
python fake_email_sender_windows.py
```

**Solution**: The Windows version uses regular input instead of getpass.

### **Problem: Authentication Failed**

**Error**: `SMTPAuthenticationError`

**Solutions**:
1. ✅ Make sure you're using **App Password**, not regular password
2. ✅ Verify 2-Factor Authentication is enabled
3. ✅ Check that App Password is correct (16 characters)
4. ✅ Ensure Gmail address is typed correctly

### **Problem: Email Shows Real Sender**

**Expected Behavior:**
- This is normal! Gmail shows real sender for security
- Fake sender appears in headers (invisible to most users)
- This is a security feature, not a bug

**What You Can Do**:
- Check email headers (View → Show Original in Gmail)
- Test with different email providers
- Some email clients may show fake sender

### **Problem: Connection Refused**

**Error**: `Connection refused` or `Timeout`

**Solutions**:
1. ✅ Check internet connection
2. ✅ Verify firewall isn't blocking port 587
3. ✅ Some networks block SMTP (try different network)
4. ✅ Check if antivirus is blocking the connection

### **Problem: Email Goes to Spam**

**Why**:
- Fake sender addresses trigger spam filters
- Missing SPF/DKIM records
- Suspicious content

**Solutions**:
- Use real sender for legitimate emails
- Add recipient to contacts first
- Check spam folder

### **Problem: Module Not Found**

**Error**: `ModuleNotFoundError`

**Solution**:
```cmd
# Python not in PATH or wrong version
python --version
# Should show Python 3.6+

# Try:
py fake_email_sender_windows.py
# or
python3 fake_email_sender_windows.py
```

---

## 📝 **Examples**

### **Example 1: Basic Usage**

```cmd
C:\Repos\fakemail> python fake_email_sender_windows.py

=== Fake Email Sender (Windows Compatible) ===
Enter your real Gmail address: john@gmail.com
Enter your Gmail password: xxxx xxxx xxxx xxxx
Enter recipient email address: test@example.com
Enter fake sender email: noreply@company.com
Enter email subject: Test Email
Enter email message: This is a test.
[Press Enter twice]
```

### **Example 2: Using Simple Example**

1. Open `simple_example.py` in text editor
2. Replace credentials:
   ```python
   real_email = "yourrealmail@gmail.com"
   password = "your_app_password"
   to_email = "receiver@example.com"
   fake_sender = "support@dummycompany.com"
   ```
3. Run:
   ```cmd
   python simple_example.py
   ```

---

## 🔒 **Security Best Practices**

1. ✅ **Never share your App Password**
2. ✅ **Delete App Password** if compromised
3. ✅ **Use strong passwords** for your Gmail account
4. ✅ **Enable 2FA** (mandatory for this tool)
5. ✅ **Review sent emails** regularly
6. ✅ **Only test with your own emails** or with explicit permission

---

## 📚 **Additional Information**

### **Email Headers Explained**

When recipient checks email headers:
- `From`: What sender appears as
- `Return-Path`: Where bounces go
- `Reply-To`: Default reply address
- `Received`: Shows routing through Gmail

### **Gmail Security Features**

Gmail implements:
- SPF (Sender Policy Framework)
- DKIM (DomainKeys Identified Mail)
- DMARC (Domain-based Message Authentication)

These verify email authenticity and may override fake headers.

---

## ⚖️ **Legal Disclaimer**

**BY USING THIS SOFTWARE, YOU AGREE TO:**

1. **Use it only for legal, authorized purposes**
2. **Not impersonate real entities or individuals**
3. **Obtain consent before sending test emails**
4. **Comply with all applicable laws in your jurisdiction**
5. **Accept full legal responsibility for your actions**

**THE DEVELOPERS/AUTHORS:**
- Provide no warranty or guarantee
- Are not responsible for misuse
- Do not condone illegal activities
- Provide this tool for educational purposes only

**YOU ARE SOLELY RESPONSIBLE FOR:**
- Compliance with local laws
- Obtaining necessary permissions
- Ethical use of this software
- Any consequences of misuse

---

## 📞 **Support & Contributing**

### **Common Questions**

**Q: Why doesn't Gmail show the fake sender?**  
A: Security feature - Gmail shows authenticated sender to prevent spoofing.

**Q: Is this illegal?**  
A: It depends on jurisdiction and use case. Misuse (phishing, fraud) is illegal everywhere.

**Q: Can I use this anonymously?**  
A: No - your real email is always traceable through headers.

**Q: Does this work with other email providers?**  
A: The code is for Gmail. You'd need to modify SMTP settings for others.

---

## 📄 **License**

This project is provided as-is for educational purposes. Use at your own risk.

---

## 🎓 **Learning Resources**

- [Gmail SMTP Documentation](https://support.google.com/a/answer/176600)
- [Email Headers Explained](https://www.lifewire.com/what-are-email-headers-1171105)
- [Python smtplib Documentation](https://docs.python.org/3/library/smtplib.html)
- [Email Security Best Practices](https://www.rfc-editor.org/rfc/rfc7208)

---

## ⚠️ **Final Warning**

**THINK BEFORE YOU USE THIS TOOL**

- Are you using it for legitimate purposes?
- Do you have permission from recipients?
- Are you complying with local laws?
- Are you aware of the risks?

**If the answer to any question is "NO" - DO NOT USE THIS TOOL**

---

**Last Updated**: 2025  
**Version**: 1.0  
**Python Compatibility**: 3.6+