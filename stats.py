def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_chars_dict(book_text):
    count = {}

    for char in book_text:
        char = char.lower()
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    return count

def sort_on(dict):
    return dict["count"]

def sorted_word_list(dict):
    lst = []
    for key in dict:
        lst.append({"char": key, "count": dict[key]})
    lst.sort(reverse=True, key=sort_on)
    return lst