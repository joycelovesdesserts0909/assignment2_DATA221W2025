def find_lines_containing(filename, keyword):
    results = []  # Store matching lines
    # Open file for reading
    with open(filename, "r", encoding="utf-8") as f:
        # Go through each line (start counting from 1)
        for line_number, line_text in enumerate(f, 1):
            # Case-insensitive search
            if keyword.lower() in line_text.lower():
                # Save line number and stripped text
                results.append((line_number, line_text.strip()))
    return results
# Call the function
keyword_to_find = "lorem"
matches = find_lines_containing("sample-file.txt", keyword_to_find)
# Print total matches
print(f"Found {len(matches)} lines containing '{keyword_to_find}'.")
# Print up to first 3 matches
print("First 3 matching lines:")
for i in range(min(3, len(matches))):
    line_num, text = matches[i]
    print(f"Line {line_num}: {text}")
