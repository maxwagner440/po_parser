import fitz  # PyMuPDF
import pytesseract
from PIL import Image

# Path to the PDF file
pdf_path = 'ElPaso.pdf'

# Open the PDF file
pdf_document = fitz.open(pdf_path)

# Specify coordinates (x, y, width, height)
coordinates = (50, 100, 500, 200)

# Process each page
for page_number in range(len(pdf_document)):
    # Get the page
    page = pdf_document.load_page(page_number)
    
    # Convert PDF page to an image (pixmap)
    pix = page.get_pixmap()
    
    # Save the image
    image_path = f'page_{page_number + 1}.png'
    pix.save(image_path)
    
    # Open the image
    image = Image.open(image_path)
    
    # Crop the image to the specified coordinates
    cropped_image = image.crop(coordinates)
    
    # Use Tesseract to extract text from the cropped image
    text = pytesseract.image_to_string(cropped_image)
    
    # Print the extracted text
    print(f'Page {page_number + 1}:')
    print(text)
    print('-' * 80)
