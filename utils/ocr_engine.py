from PIL import Image
import pytesseract

# Optional: add this line if tesseract is not globally found
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\AAtwal\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def extract_text_from_images(images):
    text = ""
    for idx, image in enumerate(images):
        print(f"Processing page {idx + 1}...")
        if not isinstance(image, Image.Image):
            image = Image.fromarray(image)
        text += pytesseract.image_to_string(image)
    return text