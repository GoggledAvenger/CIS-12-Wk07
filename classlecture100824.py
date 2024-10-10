# Week 7 - Iteration & Search - Lecture Notes
# see https://thartmanoftheredwoods.github.io/CIS-12/week_7py.html

def how_many_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        line_count = sum(1 for _ in file)
    print("Number of lines:", line_count)

# how_many_lines('resources/dracula.txt')
# how_many_lines('resources/princessofmars.txt')

# Practice Exercise: Write a function count_words(file_path)
# that reads each line, strips whitespace, and counts the total words.

def count_words(file_path):
    count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            line = line.strip()
            count += len(line.split(' '))
    return count

# print(count_words('resources/dracula.txt'))
# print(count_words('resources/princessofmars.txt'))

#more Pythonic way to code the same function:

def count_words_simplified(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return sum(len(line.strip().split(' ')) for line in file)

# print(count_words_simplified('resources/dracula.txt'))
# print(count_words_simplified('resources/princessofmars.txt'))

# Variable Updating

def cumulative_length_e_words(file_path):
    total_length = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if 'e' in word:
                total_length += len(word)
    return total_length

# print(cumulative_length_e_words('resources/dracula.txt'))
# print(cumulative_length_e_words('resources/princessofmars.txt'))

def count_vowel_words(file_path):
    count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if any(vowel in word for vowel in 'aeiou'):
                count += 1
    return count

# print(count_vowel_words('resources/dracula.txt'))
# print(count_vowel_words('resources/princessofmars.txt'))

# Practice Exercise: Refactor a function that checks if a word contains
# any vowels using in.

def does_have_vowel(word):
    if any(vowel in word for vowel in 'aeiou'):
        return True
    return False

# print(does_have_vowel('dracula'))
# print(does_have_vowel('crypt'))

# simplified
def does_have_vowel_simplified(word):
    return any(vowel in word for vowel in 'aeiou')

# print(does_have_vowel_simplified('dracula'))
# print(does_have_vowel_simplified('crypt'))

# Linear Search

def contains_any(word, letters):
    return any(letter in word for letter in letters.lower())

# print(contains_any('frankenstein', 'akgt'))

# Practice Exercise: Write a function to return all positions of a specified
# letter in a word.
'''
def where_letter_positions(word, char):
    for letter in word for letter in char.lower():
        return enumerate(len(word.split()))

print(where_letter_positions('elementary', 'e'))
'''
def letter_position(word, letter):
    letter = letter.lower()
    result = ''
    i = 0
    for l in word.lower():
        if l == letter:
            result += str(i) + ','
        i += 1
    return result.removesuffix(',').split(',')

# print(letter_position('elementary', 'e'))

# more Pythonic solution:

def letter_position_simplified(word, letter):
    letter = letter.lower()
    return [i for i, l in enumerate(word.lower()) if l == letter]

# print(letter_position_simplified('elementary', 'e'))

# Doctest and Testing Functions

def contains_any(word, letters):
    """Checks if a word uses any letters in a given set.

    >>> contains_any('banana', 'aeiou')
    True
    >>> contains_any('banana', 'xyz')
    False
    """
    return any(letter in word for letter in letters.lower())

# Practice Exercise: Write doctests for has_letter and run them.

def has_letter(word, char):
    """Checks if a word contains a specific letter.

    >>> has_letter('elementary', 'e')
    True
    >>> has_letter('elementary', 'h')
    False
    """
    return char.lower() in word.lower()

# Exercises

# Ex 1: Detect Palindromic Words: write a function is_palindromic(word) that returns
# True if a word reads the same backward

def reverse(word):
    rev_word = ''
    for i in range(len(word)-1, -1, -1):
        rev_word += word[i]
    return rev_word

def is_palindromic(word):
    return word.lower() == reverse(word.lower())

# print(is_palindromic('hello'))
# print(is_palindromic('kayak'))

def is_palindromic_efficient(word):
    s = 0
    e = len(word) - 1
    while s <= e:
        if word[s].lower != word[e].lower:
            return False
        s += 1
        e -= 1
    return True

# print(is_palindromic_efficient('hello'))
# print(is_palindromic_efficient('kayak'))

# Ex 2: Counting Words by Length: Write count_by_length (file_path, n) that counts the
# number of words with exactly n letters.

def count_by_length(file_path, n):
    pass                            # TODO: work on this

# Ex 3: Find Words with Specific Letter Patterns: Write find_words_with_pattern
# (file_path, pattern) to count words with a particular letter pattern.

def find_words_with_pattern(file_path, pattern):
    pass                            # TODO: work on this as well
