import string
book_to_read = "books/frankenstein.txt"

def display_character_count(alph):
    for char in alph:
        print(f"The {char} character was found {alph[char]} times")

def count_character_occur(book):
    alphabet = {char: 0 for char in string.ascii_lowercase}
    for char in book:
        char = char.lower()
        if char in alphabet:
            alphabet[char] += 1   
    display_character_count(alphabet)

def count_words(file_contents):
    words = file_contents.split()
    count = len(words)
    print(f"{count} words found in the document")
    

def main():
    with open(book_to_read) as file:
        file_contents = file.read()
        print(file_contents)
        print(f"--- Begin report of {book_to_read} ---")
        count_words(file_contents)
        count_character_occur(file_contents)
        
        print("--- End report ---")

main()