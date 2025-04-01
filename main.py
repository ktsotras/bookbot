from stats import get_num_words
from stats import get_num_chars

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    print(get_num_words(get_book_text("books/frankenstein.txt")))
    print(get_num_chars(get_book_text("books/frankenstein.txt")))

main()