from classes.pattern import ElPaso_pattern
from classes.spacy import get_lines
import fitz  # PyMuPDF
import pytesseract
from PIL import Image

### TESTING APPLIED ###
# # Path to the PDF file
pdf_path = 'Applied.pdf'

doc = fitz.open(pdf_path)  # example document
page = doc[0]  # first page
word = page.get_text("text")  # extract sorted words

print(word)

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