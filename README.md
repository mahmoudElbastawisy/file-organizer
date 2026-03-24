# File Organizer

A Python-based automation script that organizes files within a directory by grouping them into folders based on file type.

---

## Overview

This project automates the process of sorting files inside a target folder.  
It scans all files, determines their type by extension, and moves them into categorized folders.

The script also ensures that existing files are not overwritten by safely renaming duplicates.

---

## Features

- Scans a target folder automatically  
- Creates category folders if they do not exist  
- Moves files into folders based on extension  
- Handles duplicate filenames safely  
- Supports multiple file type categories  

---

## Supported Categories

- Images  
- PDFs  
- Videos  
- Documents  
- Archives  
- Others  

---

## Project Structure

```
file-organizer/
├── main.py
└── README.md
```

---

## Installation

No external dependencies required.  
Runs with standard Python libraries.

---

## Usage

Run the script:

```bash
py main.py
```

---

## How It Works

1. Scans all files in the target directory  
2. Detects file type using extension  
3. Maps each file to a category  
4. Creates folders for each category if needed  
5. Moves files into their respective folders  
6. Renames files if duplicates exist to prevent overwriting  

---

## Example

Before:

```
/folder
├── photo.jpg
├── document.pdf
├── video.mp4
```

After:

```
/folder
├── Images/
│   └── photo.jpg
├── PDFs/
│   └── document.pdf
├── Videos/
│   └── video.mp4
```

---

## Tech Stack

- Python  
- pathlib  
- shutil  
