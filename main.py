def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def count_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return f"{num_words} words found in the document"


def main():
    print(count_words(get_book_text("books/frankenstein.txt")))

main()
