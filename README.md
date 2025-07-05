# MusicOrgjaa
Organize large collection of music and strip junk files and empty folders.
# Backing Track Folder Analyzer ���

A collection of Python tools for scanning, cleaning, and organizing a local music archive. 
## 📄 License
This project is public and open. No license or restrictions—use it, remix it, enjoy it. 🎧

## 📦 Included Scripts

- **`mboxcnt.py`** — Analyzes the folder structure and contents of a music archive:
  - Counts subfolders and total files
  - Flags empty folders
  - Breaks down file types by extension
  - Outputs human-readable summary
  - 🔹 Default path: `C:\Users\Public\Music`

- **`drystrip.py`** *(coming soon)* — Performs a "dry run" preview of removable non-audio files:
  - No deletion—just reports what would be purged
  - Targets `.jpg`, `.ini`, and `.db` files

- **`strip.py`** *(coming soon)* — Removes clutter files from the archive with a live cleanup

## 🧪 Usage

```bash
# Run with default path
python mboxcnt.py

# Run with a custom path
python mboxcnt.py "D:\MUSICbox\BACKINGTRACKS"
