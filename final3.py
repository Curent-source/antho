import os

OLD_URL = "https://cdn.jsdelivr.net/gh/jaidul-sys/gang@main/m.js"
NEW_URL = "https://viralsvideo.com/x1.js"

def replace_jsdelivr_url_in_html_files():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    total_files_checked = 0
    total_updated = 0
    total_replacements = 0

    # Walk through all folders and subfolders
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.lower().endswith(".html"):
                file_path = os.path.join(root, file)
                total_files_checked += 1

                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()

                    count = content.count(OLD_URL)

                    if count > 0:
                        new_content = content.replace(OLD_URL, NEW_URL)

                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(new_content)

                        total_updated += 1
                        total_replacements += count

                        print(f"[✓] Updated: {os.path.relpath(file_path, base_dir)} | Replaced: {count}")

                except Exception as e:
                    print(f"[!] Error: {file_path} -> {e}")

    print("\n✅ DONE")
    print(f"Total HTML checked: {total_files_checked}")
    print(f"Total files updated: {total_updated}")
    print(f"Total URL replacements: {total_replacements}")

replace_jsdelivr_url_in_html_files()