## Overview
This repository is a Text Analysis Tool that processes and analyzes the content of a text file, providing various metrics and insights. It is structured with functions that handle specific tasks related to text processing, including counting lines, words, and unique words, finding the most common and longest words, and calculating average word lengths. These functions are modular and reusable, making the code versatile for various text-analysis applications.

## Key Functionalities Implemented
File Reading: A function to open and read the content of a text file (read_file).

Line and Word Counting:
- Line Count: Counts the number of lines in the text (count_lines).
- Word Count: Calculates the total number of words (count_words).

Word Frequency Analysis:
- Most Common Word: Identifies the most frequently used word and its count (most_common_word).
- Unique Word Count: Counts the number of unique words (count_unique_words).
- Longest Word: Finds the longest word in the text (longest_word).
- Specific Word Count: Intended to count occurrences of a specific word, though it requires debugging to function correctly.

Text Metrics:
- Average Word Length: Calculates the average length of words in the text (average_word_length).
- Percentage of Long Words: Calculates the percentage of words that are longer than the average word length (percentage_of_long_words).
- Main Analysis Function: A analyze_text function that integrates the core features, providing an overview of the text's structure and key details.
