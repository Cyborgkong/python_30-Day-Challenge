from collections import Counter
import string

with open("text files\sample.txt", "r") as file:
    content = file.read()
    
lines = content.splitlines()
words = content.translate(str.maketrans('', '', string.punctuation)).lower().split()

total_lines = len(lines)
total_words = len(words)
unique_words = set(words)
word_counts = Counter(words)
most_common_words = word_counts.most_common(5)

print(f'Total lines: {total_lines}')
print(f'Total words: {total_words}')
print(f'Unique words: {len(unique_words)}')
print(f'Top five most common words:')
for word, count in most_common_words:
    print(f'{word}: {count}')