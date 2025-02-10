import os
import zipfile
import uuid
from pathlib import Path
import re
import shutil

def slugify(text):
    """Convert Chinese/special characters to safe filename."""
    # Generate a UUID for uniqueness
    unique_id = str(uuid.uuid4())[:8]
    # Keep only alphanumeric characters and replace others with dash
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text).strip('-')
    return f"{text}-{unique_id}" if text else unique_id

def decode_filename(filename):
    """Try different encodings to decode filename."""
    decoded_name = None
    encodings = ['utf-8', 'gbk', 'big5', 'shift-jis', 'cp437']
    
    # First try direct decoding
    for encoding in encodings:
        try:
            decoded_name = filename.encode('cp437').decode(encoding)
            if decoded_name and not all(ord(c) < 32 for c in decoded_name):
                return decoded_name
        except:
            continue
    
    # If all decodings fail, use the original name
    return filename

def safe_extract_zip(zip_path, extract_dir):
    """Extract ZIP file with proper encoding handling."""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Create mapping of original to safe filenames
            filename_mapping = {}
            
            for file_info in zip_ref.filelist:
                try:
                    # Decode filename
                    original_name = file_info.filename
                    decoded_name = decode_filename(original_name)
                    
                    # Generate safe filename
                    path_parts = Path(decoded_name).parts
                    safe_parts = [slugify(part) for part in path_parts]
                    safe_name = str(Path(*safe_parts))
                    
                    # Store mapping
                    filename_mapping[original_name] = safe_name
                    
                    # Extract with safe name
                    source = zip_ref.read(file_info)
                    target_path = Path(extract_dir) / safe_name
                    
                    # Create parent directories
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    # Write file
                    with open(target_path, 'wb') as f:
                        f.write(source)
                    
                    print(f"Successfully extracted: {safe_name}")
                    
                except Exception as e:
                    print(f"Error extracting {original_name}: {str(e)}")
                    continue
            
            # Save filename mapping for reference
            mapping_file = Path(extract_dir) / "filename_mapping.txt"
            with open(mapping_file, 'w', encoding='utf-8') as f:
                for orig, safe in filename_mapping.items():
                    f.write(f"{orig} -> {safe}\n")
            
    except Exception as e:
        print(f"Error processing ZIP file {zip_path}: {str(e)}")

def main():
    # Create extraction directory
    base_dir = Path("Notionfiles")
    extract_dir = base_dir / "extracted_utf8"
    extract_dir.mkdir(parents=True, exist_ok=True)
    
    # Process all ZIP files
    for file in base_dir.glob("*.zip"):
        if file.is_file():
            print(f"\nProcessing: {file}")
            safe_extract_zip(file, extract_dir)

if __name__ == "__main__":
    main() 