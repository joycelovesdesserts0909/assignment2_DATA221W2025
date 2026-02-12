with open("sample-file.txt", "r") as f:
    # Read the entire file into a single string
    text = f.read()
    # Split the text into raw tokens based on whitespace
    words = text.split()
import string
cleaned_words = []
for w in words:
    # Convert to lowercase
    w = w.lower()
    # Remove punctuation characters from the start and end of the token
    w = w.strip(string.punctuation)
    cleaned_words.append(w)
final_words = []
for w in cleaned_words:
    # Count alphabetic characters to check if the token has at least 2 letters
    count = 0
    for char in w:
        if char.isalpha():
            count += 1
    # Keep only words with ≥ 2 alphabetic characters
    if count >= 2:
        final_words.append(w)
# Count word frequencies
counts = {}
for w in final_words:
    if w in counts:
        counts[w] += 1   # Increase count if word already exists
    else:
        counts[w] = 1    # Initialize count for new word
# Sort words by frequency (descending order)
sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
# Select the top 10 most frequent words
top_10 = sorted_counts[:10]
# Print the results in the required format
for word, count in top_10:
    print(f"{word} -> {count}")
