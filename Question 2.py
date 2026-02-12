with open("sample-file.txt", "r") as f:
    # Read the whole file into a string
    text = f.read()
    # Split the text into raw tokens based on whitespace
    words = text.split()
import string
cleaned_words = []
for w in words:
    # Convert the word to lowercase
    w = w.lower()
    # Remove punctuation from the beginning and end of the word
    w = w.strip(string.punctuation)
    cleaned_words.append(w)
final_words = []
for w in cleaned_words:
    # Count how many alphabetic characters appear in the word
    count = 0
    for char in w:
        if char.isalpha():
            count += 1
    # Keep only words with at least 2 alphabetic characters
    if count >= 2:
        final_words.append(w)
# Dictionary to count bigram frequencies
counts = {}
# Loop through words and form bigrams (pairs of consecutive words)
for i in range(len(final_words) - 1):
    # Create a bigram by joining word i and word i+1
    bi = final_words[i] + " " + final_words[i + 1]
    # Update frequency count for each bigram
    if bi in counts:
        counts[bi] += 1
    else:
        counts[bi] = 1
# Sort bigrams by frequency in descending order
sorted_bigrams = sorted(counts.items(), key=lambda item: item[1], reverse=True)
# Take the top 5 most frequent bigrams
top_5 = sorted_bigrams[:5]
# Print the bigrams in the required format: "word1 word2 -> count"
for bigram, count in top_5:
    print(f"{bigram} -> {count}")
