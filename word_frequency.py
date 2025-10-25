#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def get_sentence():
    while True:
        sentence = input("Enter a valide sentence:")
    if is_sentence(sentence):
        return sentence
    else:
        print("Invalide input. A sentence must start with a capital letter and end with a punctuation (., !, or ?).")
def calculater_frequencies(sentence):
    if sentence[-1] in ['.', '?', '!']
        clean_sentence = sentence[:-1]
    else:
        clean_sentence = sentence
        
    words = []
    frequencies = []
    word_list = clean_sentence.lower().split()
    
    for word in word_list:
        if word in words:
            index = words.index(word)
            frequencies[index] += 1
        else:
            word.append(word)
            frequencies.append(1)
    return words, frequencies

def print_frequencies(words, frequencies):
    print("\n-Word Frequency Results-")
    for i in range(len(words)):
        print(f"'{word}': {frequencies}")
    print("")

def main():
    user_sentence = get_sentence()
    word_list, freq_list = calculater_frequencies(user_sentence)
    print_frequencies(word_list, freq_list)

if __name__=="__main__":
    main()
