# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Install Tesseract OCR and the language data files
RUN apt-get update && \
    apt-get install -y tesseract-ocr && \
    apt-get install -y tesseract-ocr-eng

# Copy the current directory contents into the container at /app
COPY . /app

# Create a virtual environment
RUN python -m venv venv;

# Install dependencies in the virtual environment
RUN venv/bin/pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Install Python packages
RUN pip install pymupdf pytesseract pillow

# Set the Tesseract command path and TESSDATA_PREFIX
ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata
ENV PATH="/usr/bin/tesseract:${PATH}"

# Activate the virtual environment and run the main file
CMD ["python", "main.py"]
