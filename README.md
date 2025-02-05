# Duplicate File Finder

## Overview
This Python script detects duplicate files in a specified directory by computing their hash values. For PDF files, it extracts text and compares hashes to identify duplicates. The script logs duplicate files to a specified log file.

## Features
- Uses **MD5 hashing** to detect duplicates.
- Extracts text from **PDF files** for more accurate duplicate detection.
- Utilizes **difflib** for similarity comparison.
- Provides **progress tracking** using `tqdm`.
- Logs detected duplicates to a file.

## Installation

Ensure you have Python installed. Then, install the required dependencies:

```sh
pip install PyPDF2 tqdm
```

## Usage

Modify the `directory_path` and `log_file_path` variables to specify the folder to scan and the output log file:

```python
# Example directory to scan
directory_path = r'path\to\your\directory'

# Output log file
log_file_path = r'path\to\log\file.txt'
```

Run the script:

```sh
python script.py
```

### Example Output

```
Processing files: 100%|█████████████████████| 50/50 [00:10<00:00, 5.00file/s]
Duplicate files have been logged to C:\Users\User\Desktop\duplicates_log.txt
```

## Functions

### `file_hash(filepath)`
Computes the **MD5 hash** of a given file.

### `extract_text_from_pdf(pdf_path)`
Extracts text from a PDF file.

### `are_texts_similar(text1, text2, threshold=0.8)`
Checks if two text strings are similar beyond a given threshold.

### `file_hash_or_text(filepath)`
Attempts to hash a file. If it’s a PDF, extracts and hashes the text instead.

### `find_duplicates(directory)`
Scans a directory and detects duplicate files based on hashes.

### `log_duplicates_to_file(duplicates, log_file_path)`
Logs duplicate file names to a text file.

## Author
[Syanthan Vullingala](https://github.com/shanthan001)
