
To Build Docker:

build:
    - docker build -t po-parser .
run:
    docker run -it po-parser
run interactive shell:
    docker run -it po-parser /bin/bash




DOCUMENTATION REFERENCES


spaCy:
    Matcher: https://spacy.io/api/matcher#_title



What works:
    - coordinate parsing
    - block and text parsing using fitz
    - text searching (after parsing using spacy)

What didn't work:
    - Text parsing poor images
    