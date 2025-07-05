import os

music_root = r'D:\MUSICbox'

print(f"\n🎯 Searching for .flac files in: {music_root}\n")

flac_files = []

for dirpath, _, filenames in os.walk(music_root):
    for file in filenames:
        if file.lower().endswith('.flac'):
            full_path = os.path.join(dirpath, file)
            flac_files.append(full_path)

# 🗂️ Output results
if flac_files:
    print(f"🎵 Found {len(flac_files)} .flac file(s):\n")
    for path in flac_files:
        print(f"  {path}")
else:
    print("🚫 No .flac files found.")

print("\n✅ Scan complete.\n")
