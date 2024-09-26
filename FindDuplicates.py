import os
import hashlib
import PyPDF2
import difflib

def file_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extract_text()
    return text

def are_texts_similar(text1, text2, threshold=0.8):
    return difflib.SequenceMatcher(None, text1, text2).ratio() > threshold

def file_hash_or_text(filepath):
    try:
        # Try to hash the file
        return file_hash(filepath)
    except:
        # If hashing fails, extract text from PDF and hash the text
        if filepath.lower().endswith('.pdf'):
            text = extract_text_from_pdf(filepath)
            return hashlib.md5(text.encode()).hexdigest()
        else:
            raise ValueError("Unsupported file format")

def find_duplicates(directory):
    hashes = {}
    duplicates = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            filehash = file_hash_or_text(filepath)

            if filehash in hashes:
                duplicates.append((file, os.path.basename(hashes[filehash])))
            else:
                hashes[filehash] = filepath

    return duplicates

def log_duplicates_to_file(duplicates, log_file_path):
    with open(log_file_path, 'w') as log_file:
        for dup in duplicates:
            log_file.write(f"[{dup[0]}] is a duplicate of [{dup[1]}]\n")

# Example usage
directory_path = r'\\fs10000\SHR-CS\ICM Payments\APPROVAL REQUIRED'
log_file_path = r'C:\Users\SYANTHA2\OneDrive - Province of Nova Scotia\Desktop\duplicates_log.txt'

duplicates = find_duplicates(directory_path)
log_duplicates_to_file(duplicates, log_file_path)

print(f"Duplicate files have been logged to {log_file_path}")
