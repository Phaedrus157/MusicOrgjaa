import os
import sys

# 📍 Target directory – from CLI or default to MUSICbox
music_root = sys.argv[1] if len(sys.argv) > 1 else r'C:\Users\Public\Music'

# 🧹 Extensions to preview for stripping (non-audio clutter)
extensions_to_strip = {'.jpg', '.ini', '.db'}

# 📊 Tracking counters
folder_count = 0
file_count = 0
empty_folder_count = 0
files_matching = []

print(f"\n🔍 Dry Run: Scanning for junk files in {music_root}\n")

# 🚶 Walk through directory tree
for dirpath, dirnames, filenames in os.walk(music_root):
    if dirpath != music_root:
        folder_count += 1
    file_count += len(filenames)

    if not filenames and not dirnames:
        empty_folder_count += 1

    for file in filenames:
        ext = os.path.splitext(file)[1].lower()
        if ext in extensions_to_strip:
            full_path = os.path.join(dirpath, file)
            files_matching.append(full_path)

# 🗂️ Report matched files
if files_matching:
    print("🗑️ Files that would be removed:")
    for path in files_matching:
        print(f"  {path}")
else:
    print("✅ No matching files found. Clean as a whistle!")

# 📊 Summary Output
print(f"\n📁 Folder count (excluding root): {folder_count}")
print(f"🎵 Total file count: {file_count}")
print(f"🕳️ Empty folders: {empty_folder_count}")
print(f"\n🧹 {len(files_matching)} file(s) matched purge criteria.")
print("\n✅ Dry scan complete. No files were removed.\n")
