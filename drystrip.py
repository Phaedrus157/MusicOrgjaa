import os

# 🔍 Folder to scan
music_root = r'D:\MUSICbox'

# 🧹 Extensions to target for stripping
extensions_to_strip = {'.jpg', '.ini', '.db'}

# 📋 Storage for matching file paths
files_found = []

print(f"\n🔎 Dry scan: Listing files that would be removed from {music_root}\n")

for dirpath, _, filenames in os.walk(music_root):
    for file in filenames:
        ext = os.path.splitext(file)[1].lower()
        if ext in extensions_to_strip:
            full_path = os.path.join(dirpath, file)
            files_found.append(full_path)

# 📊 Display results
if files_found:
    print("🗂️ Files marked for stripping:\n")
    for path in files_found:
        print(f"🗑️ {path}")
    print(f"\n✅ {len(files_found)} file(s) would be removed.")
else:
    print("✅ No matching files found. Clean as a whistle!")

print("\n🚫 This was a dry run. No files were deleted.\n")
