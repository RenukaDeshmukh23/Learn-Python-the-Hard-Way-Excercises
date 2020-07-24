def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sorts the words"""
    return sorted(words)

def print_first_word(words):
    """prints the first word"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """prints the last word"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """takes in full sentence & returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """prints first ans last word"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """sorts the words thwn prints first and last"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
