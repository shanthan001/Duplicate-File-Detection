# Duplicate File Finder

This Python script identifies and logs duplicate files within a specified directory. It uses file hashing and text extraction (for PDFs) to determine duplicates.

## Features

- **File Hashing**: Computes MD5 hash for files to identify duplicates.
- **PDF Text Extraction**: Extracts text from PDF files and hashes the text for comparison.
- **Similarity Check**: Compares text similarity using `difflib`.
- **Logging**: Logs duplicate files to a specified log file.

## Requirements

- Python 3.x
- `PyPDF2` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/duplicate-file-finder.git
    ```
2. Navigate to the project directory:
    ```sh
    cd duplicate-file-finder
    ```
3. Install the required packages:
    ```sh
    pip install PyPDF2
    ```

## Usage

1. Update the `directory_path` and `log_file_path` variables in the script with your desired paths.
2. Run the script:
    ```sh
    python duplicate_file_finder.py
    ```

## Example

```python
# Example usage
directory_path = r'\\fs10000\SHR-CS\ICM Payments\APPROVAL REQUIRED'
log_file_path = r'C:\Users\SYANTHA2\OneDrive - Province of Nova Scotia\Desktop\duplicates_log.txt'

duplicates = find_duplicates(directory_path)
log_duplicates_to_file(duplicates, log_file_path)

print(f"Duplicate files have been logged to {log_file_path}")
