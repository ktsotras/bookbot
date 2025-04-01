from stats import get_num_words, get_chars_dict, sorted_word_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    num_words = get_num_words(text)
    dict = get_chars_dict(text)
    sorted_dict = sorted_word_list(dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char in sorted_dict:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["count"]}")

    print("============= END ===============")

main()