def get_num_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return f"{num_words} words found in the document"

def get_num_chars(book_text):
    count = {}

    for char in book_text:
        char = char.lower()
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    return count