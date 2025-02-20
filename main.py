from classes.pattern import ElPaso_pattern
from classes.spacy import get_lines
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import cv2
import numpy as np


### TESTING APPLIED ###
# # Path to the PDF file

# doc = fitz.open(pdf_path)  # example document


#  PARSED APPLIED BUT NOT ACCURATE

# file_path = "Applied.pdf"
# document = fitz.open(file_path)


# file_path = "Applied.pdf"
# pages = convert_from_path(file_path)

# for page_number, page in enumerate(pages):
#     page.save(f'page_{page_number}.jpg', 'JPEG')

# extracted_text = ""
# for i in range(len(pages)):
#     img = Image.open(f'page_{i}.jpg')
#     text = pytesseract.image_to_string(img)
#     extracted_text += text + "\n"

# print(extracted_text)



### USED TO PARSE AND CLEAN UP POOR QUALITY APPLIED PDF ###

# Convert PDF to images
file_path = "applied3.pdf"
pages = convert_from_path(file_path)
images = []
for page_number, page in enumerate(pages):
    img = np.array(page)
    images.append(img)

# Preprocess the images and perform OCR
extracted_text = ""
for i, img in enumerate(images):
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply thresholding
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # Denoise the image
    denoised = cv2.fastNlMeansDenoising(thresh, None, 30, 7, 21)

    # Save the preprocessed image for debugging (optional)
    cv2.imwrite(f'preprocessed_page_{i}.jpg', denoised)

    # Perform OCR on the preprocessed image
    text = pytesseract.image_to_string(denoised)
    extracted_text += text + "\n"

print(extracted_text)














### COORDINATE PARSING ###
# coordinates = [
#     {
#         "name":"page key",
#         "x0":536.1599731445312,
#         "y0":27.095924377441406,
#         "x1":557.8927612304688,
#         "y1":36.01108169555664,
#     },
#     {
#         "name":"page value",
#         "x0":583.56005859375,
#         "y0":26.843753814697266,
#         "x1":587.9896850585938,
#         "y1":35.87580490112305,
#     },
# ]

# for coordinates in coordinates:
#     rect = fitz.Rect(coordinates["x0"], coordinates["y0"], coordinates["x1"], coordinates["y1"])
#     word = page.get_text("text", clip=rect)  # extract sorted words
#     print(coordinates["name"]+":", word.lstrip().rstrip(), " end")



### USING spaCy TO PARSE LINES OF ELPASO ###
# pdf_document = fitz.open("ElPaso.pdf")

# # Extract and process each page
# for page_number in range(len(pdf_document)):
#     page = pdf_document.load_page(page_number)
#     text = page.get_text("text")

#     # Process text with spaCy to extract item lines
#     item_lines = get_lines(text, ElPaso_pattern)
#     print("item_lines: ", item_lines)
#     # print(f'Page {page_number + 1} Item Lines:')
#     # for item in item_lines:
#     #     print(f'Text: {item[0]}, Label: {item[1]}')
#     # print('-' * 80)









# THIS WORKS FOR MOTION!!!
#  This would return a string with spaces just like we get from ElPaso

# # file_path = "Motion.pdf"
# file_path = 'Applied.pdf'
# document = fitz.open(file_path)

# text_blocks = []
# for page in document:
#     blocks = page.get_text("blocks")
#     for block in blocks:
#         print(block)
#         text_blocks.append(block[4])
# print(text_blocks)

# full_text = "\n".join(text_blocks)
# print(full_text.replace("\n", " "))   