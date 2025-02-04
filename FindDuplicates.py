import os
import hashlib
import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox
from tqdm import tqdm

# Function to get the MD5 hash of a file
def file_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() if page.extract_text() else ""
    return text

# Function to return file hash or extracted text hash (for PDFs)
def file_hash_or_text(filepath):
    try:
        return file_hash(filepath)
    except:
        if filepath.lower().endswith('.pdf'):
            text = extract_text_from_pdf(filepath)
            return hashlib.md5(text.encode()).hexdigest()
        else:
            raise ValueError("Unsupported file format")

# Function to find duplicates from selected files
def find_selected_duplicates(files):
    hashes = {}
    duplicates = []

    print(f"Processing {len(files)} selected files...\n")

    # Progress bar for processing
    for filepath in tqdm(files, desc="Checking files", unit="file"):
        try:
            filehash = file_hash_or_text(filepath)
            if filehash in hashes:
                duplicates.append((os.path.basename(filepath), os.path.basename(hashes[filehash])))
            else:
                hashes[filehash] = filepath
        except Exception as e:
            print(f"\nError processing {filepath}: {e}")

    return duplicates

# Function to log duplicates to a file
def log_duplicates_to_file(duplicates, log_file_path):
    with open(log_file_path, 'w') as log_file:
        for dup in duplicates:
            log_file.write(f"[{dup[0]}] is a duplicate of [{dup[1]}]\n")

# GUI function for file selection
def select_files():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    files = filedialog.askopenfilenames(title="Select Files to Check for Duplicates")
    
    if not files:
        messagebox.showinfo("No Files Selected", "Please select files to proceed.")
        return

    # Find duplicates
    duplicates = find_selected_duplicates(files)

    # Log duplicates
    log_file_path = r'C:\Users\SYANTHA2\OneDrive - Province of Nova Scotia\Desktop\duplicates_log.txt'
    log_duplicates_to_file(duplicates, log_file_path)

    # Show result
    if duplicates:
        messagebox.showinfo("Duplicate Check Completed", f"Duplicates found! Log saved at:\n{log_file_path}")
    else:
        messagebox.showinfo("No Duplicates", "No duplicate files found.")

# Run GUI
if __name__ == "__main__":
    select_files()
