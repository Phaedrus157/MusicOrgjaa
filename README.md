# MusicOrgjaa
Organize large collection of music and strip junk files and empty folders.
# Backing Track Folder Analyzer ���

This Python script scans a root directory containing backing tracks to provide diagnostic metadata on folder and file structure. No files are modified during execution.

## Features
- Counts subfolders and files
- Identifies empty folders (no files or subdirectories)
- Tallies file types based on extensions
- Outputs summary statistics in human-friendly format

## Usage

Edit the path in the script to point to your music directory:

```python
music_root = r'D:\MUSICbox\BACKINGTRACKS'
python mboxcnt.py
