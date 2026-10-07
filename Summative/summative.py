"""
Author: Teske Alrich
Date: October 1st 2026
Sources: https://chatgpt.com/s/t_6ac64e7ac3948191b1bb6466c0947804 - I had used chatgpt to help me determine as to why my "words.txt" text file wasn't properly aligning with my work on this file.
         I also had used numerous sources from brightspace to help me refresh my memory of functions in python.
"""

import os


def load_words(file_path):
    """Loads words from a text file into a list.

    Args:
        file_path: The path to the text file.

    Returns:
        A list of lowercased strings, where each string is a word from the
        file.
        Returns an empty list if the file cannot be found.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            
            words = [
                line.strip().lower() for line in file if line.strip()
            ]

        print(f"\nCurrently have {len(words)} words in memory.\n")
        return words

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        print(f"Current Working Directory: {os.getcwd()}")
        print(
            f"Please ensure '{file_path}' is saved in the directory shown above."
        )
        return []


# 1. Palindrome
def is_palindrome(s):
    """Returns a boolean value corresponding to whether the String s is a

    palindrome or not.
    """
    clean_s = s.strip().lower() #lowercasing all words
    return clean_s == clean_s[::-1] #make the words backwards


# 2. Anagram
def is_anagram(original, s):
    """Returns a boolean value corresponding to whether the String s is an

    anagram or not.
    """
    clean_orig = original.strip().lower() #lowercase and removes spaces
    clean_s = s.strip().lower() 
    return sorted(clean_orig) == sorted(clean_s) #Finds anagrams


# 3. Find palindromes
def find_palindromes(word_list):
    """Finds all palindromes in a list of strings and displays them in the

    terminal.
    """
    if not word_list:
        print("\nWord list is empty. Load a valid file first.")
        return

    palindromes = [word for word in word_list if is_palindrome(word)]

    print("\nPalindromes:")
    for word in palindromes:
        print(word)

    print(f"\nFound {len(palindromes)} palindromes.")


# 4. Find anagrams
def find_anagrams(word_list, target):
    """Finds all anagrams in a list of strings and displays them in the

    terminal.
    """
    if not word_list:
        print("\nWord list is empty. Load a valid file first.")
        return

    anagrams = [word for word in word_list if is_anagram(target, word)]

    print(f"\nAnagrams of '{target}':")
    for word in anagrams:
        print(word)

    print(f"\nFound {len(anagrams)} anagrams.")


# 5. Filter by length
def filter_by_length(word_list, length):
    """Returns a new list of strings after filtering items matching the target

    length.
    """
    return [word for word in word_list if len(word) == length]


# Main program

def main():
    """The main function to run the word analysis application."""
    word_list = load_words("words.txt")

    while True:
        print("\n===== WORD ANALYSIS MENU =====")
        print("1. Find palindromes")
        print("2. Find anagrams")
        print("3. Filter words by length")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            find_palindromes(word_list)

        elif choice == "2":
            target = input("Enter a word to find anagrams for: ")
            find_anagrams(word_list, target)

        elif choice == "3":
            try:
                length = int(input("Enter the desired word length: "))
                filtered_words = filter_by_length(word_list, length)

                print(f"\nWords with {length} letters:")
                for word in filtered_words:
                    print(word)

                print(f"\nFound {len(filtered_words)} words.")
            except ValueError:
                print("Error: Please enter a valid integer for word length.")

        elif choice == "4":
            print("Bye! Have a nice day :)")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4!")


if __name__ == "__main__":
    main()