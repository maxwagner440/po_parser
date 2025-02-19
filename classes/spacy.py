import spacy
import fitz
from spacy.matcher import Matcher

# Load pre-trained spaCy model (you may need to customize or train a model)
nlp = spacy.load("en_core_web_sm")

# Define function to process text with spaCy
# def process_text_with_spacy(text):
#     doc = nlp(text)
#     print("doc:", doc)
#     item_lines = []
#     for ent in doc.ents:
#         if ent.label_ in ["Item Code", "Vendor Number", "Unit"]:  # Customize based on your needs
#             item_lines.append((ent.text, ent.label_))
#     return item_lines


def get_lines(text, pattern):
    # Initialize the Matcher
    matcher = Matcher(nlp.vocab)

    # Add the pattern to the matcher
    matcher.add("ITEM_LINE", [pattern])
    # Remove line breaks
    new_text = text.replace("\n", " ")

    # Process a document
    doc = nlp(new_text)

    # Find matches
    matches = matcher(doc)

    print("matches:", matches)
    # Extract and print item lines
    for match_id, start, end in matches:
        span = doc[start:end]
        print("Item Line:", span.text)
