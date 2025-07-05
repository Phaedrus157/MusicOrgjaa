import os
import sys
from collections import Counter

# 🎯 Scan Target
music_root = sys.argv[1] if len(sys.argv) > 1 else r'C:\Users\Public\Music'

# 📦 Tracking Totals
folder_count = 0
file_count = 0
empty_folders = []
extension_counter = Counter()

print(f"\n🎧 Scanning: {music_root}\n")

# 🚶 Directory Walk
for dirpath, dirnames, filenames in os.walk(music_root):
    if dirpath != music_root:
        folder_count += 1
    if not filenames and not dirnames:
        empty_folders.append(dirpath)
    file_count += len(filenames)
    for file in filenames:
        ext = os.path.splitext(file)[1].lower()
        extension_counter[ext] += 1

# 📊 Summary
print(f"📁 Folder count (excluding root): {folder_count}")
print(f"🎵 Total file count: {file_count}")
print(f"🕳️ Empty folders: {len(empty_folders)}\n")

print(f"📂 File extension breakdown:")
for ext, count in extension_counter.most_common():
    print(f"  {ext}: {count}")

print("\n✅ Scan complete. No files were changed.")
