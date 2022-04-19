"""
File: anagram.py
Name: Hui-Hsuan Chung
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'              # Controls when to stop the loop
# Globals variables
anagm_lst = []


def main():
    """
    Search anagrams
    """
    global anagm_lst
    print('Welcome to StanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        word = input("Find anagrams for: ", )
        start = time.time()
        #########################################################
        if word == '-1':  # Type -1 to quit the searching problem
            break
        anagm_lst = []
        word_lst = list(word)
        dict_lst = read_dictionary(word_lst)  # Make a selected dictionary list based on the input word
        print('Searching...')  # Start to find anagrams
        anagrams = find_anagrams(word_lst, '', dict_lst)  # The anagrams result
        print(len(anagrams), 'anagrams:', anagrams)  # Show the anagrams
        #########################################################
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary(word_list, file=FILE):
    """
    Read the dictionary and pre-select those vocabularies that are anagram candidates
    :param word_list: input word list for which we search for anagrams
    :param file: the dictionary file
    :return: a dictionary of the vocabularies
    """
    vocabs = {}
    with open(file, 'r') as f:
        for line in f:
            vocabulary = line.split()[0]          # parse the vocabularies
            if len(vocabulary) == len(word_list):  # select the same length words
                if vocabulary[0] in word_list:  # select the opening letter that is in word
                    if vocabulary[-1] in word_list:  # # select the ending letter that is in word
                        if vocabulary[0] not in vocabs:  # Make a dictionary: {'a': [a-word], 'b': [b-word], ...}
                            vocabs[vocabulary[0]] = [vocabulary]
                        else:
                            vocabs[vocabulary[0]].append(vocabulary)
    return vocabs


def find_anagrams(in_word, current_s, dict_list):
    """
    :param in_word: input word list for which we search for anagrams
    :param current_s: string to store explored anagram
    :param dict_list: the list of dictionary vocabularies
    :return anagm_lst: a list of anagrams
    """
    # Base case: find out an anagram
    if len(current_s) == len(in_word):  # When there length of the word is equal to the input word
        print('Found:', current_s)
        anagm_lst.append(current_s)  # Collect the anagram
        print('Searching...')
    else:
        for index, char in enumerate(in_word):
            if current_s.count(char) >= in_word.count(char):
                pass
            elif in_word.count(char) > 1 and index > in_word.index(char):
                pass
            else:
                # Choose
                current_s += char
                # Explore
                if has_prefix(dict_list, current_s):
                    find_anagrams(in_word, current_s, dict_list)
                # Un-choose
                current_s = current_s[:-1]
    return anagm_lst


def has_prefix(dict_vocabs, sub_s):
    """
    With an input sub-string prefix, Check if it is in the dictionary vocabulary list
    :param dict_vocabs: the dictionary vocabularies (datatype: dict)
    :param sub_s: the sub-string to explore
    :return: True, when the prefix is found in a word in the dictionary list
    """
    for vocab in dict_vocabs[sub_s[0]]:
        if vocab.startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
