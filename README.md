Prerequsite:

1. ✅ Solution: Install Poppler on Windows
Follow these steps:

1. Download Poppler for Windows
Go to: https://github.com/oschwartz10612/poppler-windows/releases/

Download the latest .zip under "Assets" (e.g., poppler-xx_xx_xx.zip)

2. Extract the ZIP
Extract it to a known location, e.g.:

makefile
Copy
Edit
C:\Program Files\poppler
3. Add bin to System PATH
Open Start → Environment Variables

Under System Variables, find Path, click Edit

Add:

makefile
Copy
Edit
C:\Program Files\poppler\bin
Adjust the path based on where you extracted it

4. Restart your IDE or terminal
Then rerun your script.

✅ Solution
🔧 Step 1: Install Tesseract OCR
Download the Windows installer from:
👉 https://github.com/tesseract-ocr/tesseract/releases

Choose the latest .exe installer — for example:

arduino
Copy
Edit
tesseract-ocr-w64-setup-5.3.3.20231005.exe
Install it to a simple path, e.g.:

makefile
Copy
Edit
C:\Program Files\Tesseract-OCR
🔧 Step 2: Add Tesseract to your User PATH
Open Environment Variables

Under User Variables, find and edit Path

Add this new entry:

makefile
Copy
Edit
C:\Program Files\Tesseract-OCR
Click OK on all windows

🔁 Step 3: Restart Terminal
Close and reopen VS Code / Command Prompt / PowerShell.

Test Tesseract is working:

bash
Copy
Edit
where tesseract
You should see:

makefile
Copy
Edit
C:\Program Files\Tesseract-OCR\tesseract.exe
✅ Step 4: (Optional) Tell pytesseract the exact path
If you still face issues, add this to your ocr_engine.py:

python
Copy
Edit
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
