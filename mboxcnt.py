import os
import sys
from collections import Counter

# 📍 Use folder from command-line input or default to D:\MUSICbox
music_root = sys.argv[1] if len(sys.argv) > 1 else r'D:\MUSICbox'

folder_count = 0
file_count = 0
empty_folder_count = 0
extension_counter = Counter()

print(f"\n🎧 Scanning: {music_root}\n")

for dirpath, dirnames, filenames in os.walk(music_root):
    if dirpath != music_root:
        folder_count += 1
    file_count += len(filenames)

    if not filenames and not dirnames:
        empty_folder_count += 1

    for file in filenames:
        ext = os.path.splitext(file)[1].lower()
        extension_counter[ext if ext else '[no extension]'] += 1

# 📊 Summary Output
print("📁 Folder count (excluding root):", folder_count)
print("🎵 Total file count:", file_count)
print("🕳️ Empty folders:", empty_folder_count)

print("\n📂 File extension breakdown:")
for ext, count in sorted(extension_counter.items(), key=lambda x: (-x[1], x[0])):
    print(f"  {ext}: {count}")

print("\n✅ Scan complete. No files were changed.\n")
