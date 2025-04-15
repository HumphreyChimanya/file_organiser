def ai_classify_file_content(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read(1024)  # Only read first 1KB for speed
            content = content.lower()

            if "def " in content or "import " in content or "class " in content:
                return "Code"
            elif "name," in content and "email" in content:
                return "Spreadsheets"
            elif "error" in content or "debug" in content:
                return "Logs"
            elif "introduction" in content or "summary" in content:
                return "Documents"
            else:
                return "Others"
    except Exception as e:
        print(f"AI classification failed: {e}")
        return "Others"
