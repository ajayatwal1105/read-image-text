from utils.pdf_to_image import convert_pdf_to_images
from utils.ocr_engine import extract_text_from_images
import os

PDF_PATH = r"C:\Users\AAtwal\my_work\Python_Projects\read-impge-text\sample-data\All_American_Engineering_Company_6_1961.pdf"
OUTPUT_PATH = r"C:\Users\AAtwal\my_work\Python_Projects\read-impge-text\sample-data\output.txt"

# Step 1: Convert PDF to Images
images = convert_pdf_to_images(PDF_PATH)

#Step 2: Extract Text using OCR
text = extract_text_from_images(images)

# Step 3: Store Extracted Text
os.makedirs("output", exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Text successfully extracted to {OUTPUT_PATH}")