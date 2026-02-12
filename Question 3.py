near_duplicates = {}
with open("sample-file.txt", "r", encoding="utf-8") as f:
    for line_num, original_line in enumerate(f, 1):
        # Convert the line to lowercase for normalization
        line_lowered = original_line.lower()
        # Build a normalized version of the line (clean_key)
        # We remove ALL whitespace and punctuation by keeping only alphanumeric characters.
        clean_key = ""
        for char in line_lowered:
            if char.isalnum():  # keep only letters and digits
                clean_key += char
        # Group lines by their normalized key.
        # If two lines normalize to the same clean_key, they are near-duplicates.
        if clean_key in near_duplicates:
            # Add this line (line number + original text) into the existing group
            near_duplicates[clean_key].append((line_num, original_line))
        else:
            # Create a new group with this line as the first entry
            near_duplicates[clean_key] = [(line_num, original_line)]
# Collect all groups that contain more than one line → these are near-duplicate sets
all_sets = []
for clean_key, lines_list in near_duplicates.items():
    if len(lines_list) > 1:
        all_sets.append(lines_list)
# Take only the first two sets to print, as required
first_two_sets = all_sets[:2]
# Print total number of near-duplicate groups found
print(f"Number of near-duplicate sets: {len(all_sets)}")
# Print the first two near-duplicate sets
for i, line_set in enumerate(first_two_sets, 1):
    print(f"\nSet {i}:")
    for line_num, original_text in line_set:
        # Remove trailing newline when printing the original line
        print(f"Line {line_num}: {original_text.strip()}")
