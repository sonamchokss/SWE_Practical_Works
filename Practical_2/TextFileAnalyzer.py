# 1.Opening and Reading a Text File
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

content = read_file('sample.txt')
print(content[:150])  

# 2.Counting the Number of Lines
def count_lines(content):
    return len(content.split('\n'))

num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")

# 3.Counting Words
def count_words(content):
    return len(content.split())

num_words = count_words(content)
print(f"Number of words: {num_words}")

# 4.Finding the Most Common Word
from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")

# 5.Calculating Average Word Length
def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")

# 6.Combining Everything into a Main Function
def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")

analyze_text('sample.txt')

# Exercises
# 1.Counting the number of unique words
def count_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

text = read_file('sample.txt')
print("Number of unique words:", count_unique_words(text))

# 2.Adding a function to find the longest word
def longest_word(content):
    words = content.split()
    longest_word = set(words)
    longest_word_count = len(longest_word)
    return max(words, key=len)
print("Longest word:", longest_word(content))

# 3.Counting the occurrences of a specific word
def count_specific_word(word):
    words = word.split()
    count_specific_word = set(words)
    count_specific_word = (count_specific_word)
    return count

text = read_file('sample.txt')
print("Occurance of specific words:", count_specific_word(text))

# 4.Calculating the percentage
def percentage_of_long_words(text):
    words = text.split()
    if len(words) == 0:
        return 0.0
    average_length = sum(len(word) for word in words) / len(words)
    longer_words_count = sum(1 for word in words if len(word) > average_length)
    percentage = (longer_words_count / len(words)) * 100
    return percentage
text = read_file('sample.txt')
print(percentage_of_long_words(text))