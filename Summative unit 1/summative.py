"""
Author: Teske Alrich
Date: October 1st 2026
Sources: [Any sources you use]
"""

def load_words(file_path):
    """
    Loads words from a text file into a list.

    Args:
        file_path: The path to the text file.

    Returns:
        A list of strings, where each string is a word from the file.
        Returns an empty list if the file cannot be found.
    """
    try:
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file]

        print(f"\nCurrently have {len(words)} words in memory.\n")
        return words

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []


# 1. Palindrome
def is_palindrome(s):
    """
    Returns a boolean value corresponding to whether the String s
    is a palindrome or not.

    Args:
        s: String to be tested

    Returns:
        boolean
    """
    return s == s[::-1]


# 2. Anagram
def is_anagram(original, s):
    """
    Returns a boolean value corresponding to whether the String s
    is an anagram or not.

    Args:
        original: String that is to be compared against
        s: String to be tested as a potential anagram of original

    Returns:
        boolean
    """
    return sorted(original) == sorted(s)


# 3. Find palindromes
def find_palindromes(word_list):
    """
    Finds all palindromes in a list of strings and displays them
    in the terminal.

    Args:
        word_list: A list of strings
    """
    palindromes = []

    for word in word_list:
        if is_palindrome(word):
            palindromes.append(word)

    print("\nPalindromes:")
    for word in palindromes:
        print(word)

    print(f"\nFound {len(palindromes)} palindromes.")


# 4. Find anagrams
def find_anagrams(word_list, target):
    """
    Finds all anagrams in a list of strings and displays them
    in the terminal.

    Args:
        word_list: A list of strings
        target: Target string for potential anagrams to be compared with
    """
    anagrams = []

    for word in word_list:
        if is_anagram(target, word):
            anagrams.append(word)

    print(f"\nAnagrams of '{target}':")

    for word in anagrams:
        print(word)

    print(f"\nFound {len(anagrams)} anagrams.")


# 5. Filter by length
def filter_by_length(word_list, length):
    """
    Returns a new list of strings after going through each item
    of the original list to find any that are the same as the
    provided length.

    Args:
        word_list: A list of strings
        length: The target length of the words to keep

    Returns:
        A new list of strings
    """
    filtered_words = []

    for word in word_list:
        if len(word) == length:
            filtered_words.append(word)

    return filtered_words


# Main program
def main():
    """
    The main function to run the word analysis application.
    """

    word_list = load_words("words.txt")

    while True:
        print("\n===== WORD ANALYSIS MENU =====")
        print("1. Find palindromes")
        print("2. Find anagrams")
        print("3. Filter words by length")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            find_palindromes(word_list)

        elif choice == "2":
            target = input("Enter a word to find anagrams for: ")
            find_anagrams(word_list, target)

        elif choice == "3":
            length = int(input("Enter the desired word length: "))
            filtered_words = filter_by_length(word_list, length)

            print(f"\nWords with {length} letters:")

            for word in filtered_words:
                print(word)

            print(f"\nFound {len(filtered_words)} words.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
