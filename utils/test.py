from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\AAtwal\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

image = Image.open(r"C:\Users\AAtwal\my_work\Python_Projects\read-impge-text\Capture19May.png")  # Use a known good image
text = pytesseract.image_to_string(image)
print(text)

