def get_num_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return f"{num_words} words found in the document"
