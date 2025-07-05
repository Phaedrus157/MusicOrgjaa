import os

# 🔍 Folder to scan
music_root = r'D:\MUSICbox'

# 🧹 Extensions to target for stripping
extensions_to_strip = {'.jpg', '.ini', '.db'}

# 📋 Storage for removed file paths
files_removed = []

print(f"\n🧨 Strip Mode: Removing unwanted files from {music_root}\n")

for dirpath, _, filenames in os.walk(music_root):
    for file in filenames:
        ext = os.path.splitext(file)[1].lower()
        if ext in extensions_to_strip:
            full_path = os.path.join(dirpath, file)
            try:
                os.remove(full_path)
                files_removed.append(full_path)
                print(f"🗑️ Deleted: {full_path}")
            except Exception as e:
                print(f"❌ Error deleting {full_path}: {e}")

# 📊 Summary
if files_removed:
    print(f"\n✅ {len(files_removed)} file(s) successfully removed.")
else:
    print("✅ No matching files found. Clean as a whistle!")

print("\n⚠️ Changes were made — this was a live strip.\n")
