import os
from collections import Counter

# 📍 Target folder for analysis
music_root = r'D:\MUSICbox\BACKINGTRACKS'

folder_count = 0
file_count = 0
empty_folder_count = 0
extension_counter = Counter()

print(f"\n🎧 Scanning: {music_root}\n")

for dirpath, dirnames, filenames in os.walk(music_root):
    if dirpath != music_root:
        folder_count += 1
    file_count += len(filenames)

    # 🕳️ Check for empty folders (no files AND no subfolders)
    if not filenames and not dirnames:
        empty_folder_count += 1

    for file in filenames:
        ext = os.path.splitext(file)[1].lower()
        if ext:
            extension_counter[ext] += 1
        else:
            extension_counter['[no extension]'] += 1

# 📊 Diagnostic Summary
print("📁 Folder count (excluding root):", folder_count)
print("🎵 Total file count:", file_count)
print("🕳️ Empty folders:", empty_folder_count)

print("\n📂 File extension breakdown:")
for ext, count in sorted(extension_counter.items(), key=lambda x: (-x[1], x[0])):
    print(f"  {ext}: {count}")

print("\n✅ Scan complete. No files were changed.\n")