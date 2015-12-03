def break_words(stuff):
# this funciton will break up words for us
    words = stuff.split(' ')
    return words

def sort_words(words):
# sorts the words
    return sorted(words)

def print_first_word(words):
#prints the first word after popping it off
    words = words.pop(0)
    print words

def print_last_word(words):
#prints the last word after popping it off
    words = words.pop(-1)
    print words
    
def sort_sentence(sentence):
# Takes a full sentence as an argument, then returns sorted words
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
# prints the first and last words of the sentence
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
#Takes a sentence, sorts the words and then prints the first and last one.
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
    
