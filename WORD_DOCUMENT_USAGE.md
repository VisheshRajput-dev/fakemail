# Using Word Documents with Fake Email Sender

## ✅ **New Feature: Word Document Support**

You can now use Word documents (.docx files) directly as email content! This is perfect for professional emails with tables, formatting, and complex layouts.

## 📋 **How It Works**

1. **Create your email content in Word** - Use all the formatting, tables, images, etc.
2. **Save as .docx file** - Regular Word document format
3. **Run the script** - Choose HTML email → Option 3 for Word document
4. **The script automatically converts** - Word content becomes HTML email

## 🛠️ **Setup**

First, install the required library:
```bash
pip install mammoth
```

## 📝 **Usage Steps**

When you run `fake_email_sender_windows.py`:

```
Send as HTML email? (y/n, allows tables and formatting): y

Choose content source:
1. Type HTML content manually
2. Read from HTML file
3. Convert Word document (.docx) to HTML
Enter choice (1-3): 3
Enter path to Word document (.docx): my_email.docx
```

## 🎨 **Word Document Tips**

### **Tables**
- Word tables convert perfectly to HTML tables
- Formatting, borders, and colors are preserved
- Your employee table will look professional!

### **Formatting**
- **Bold, italic, underline** - All preserved
- **Colors and fonts** - Converted to web-safe equivalents
- **Lists** - Bulleted and numbered lists work
- **Images** - Embedded images are included

### **Best Practices**
- Use clear headings and structure
- Keep tables simple and readable
- Test with a sample email first
- Save frequently while editing

## 📄 **Example Word Document Structure**

```
Subject: Employee Confirmation Letter

Dear [Recipient],

[Introduction paragraph]

[Table with employee details]

[Closing paragraph]

Best regards,
[Your Name]
[Contact Information]
```

## 🔄 **What Gets Converted**

| Word Feature | HTML Result |
|-------------|-------------|
| Tables | HTML tables with styling |
| Bold/Italic | `<strong>`, `<em>` tags |
| Lists | `<ul>`, `<ol>` tags |
| Headings | `<h1>`, `<h2>`, etc. |
| Colors | CSS styling |
| Images | Embedded in email |

## ⚠️ **Limitations**

- Complex layouts might need minor adjustments
- Some very advanced Word features may not convert perfectly
- Very large documents (>10MB) might be slow to convert

## 🚀 **Quick Start**

1. Create your email in Word with tables and formatting
2. Save as `.docx` file
3. Install mammoth: `pip install mammoth`
4. Run the script and choose option 3
5. Send professional HTML emails with tables!

This is much easier than manually writing HTML code!
