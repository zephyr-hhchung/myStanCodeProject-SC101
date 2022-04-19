"""
File: boggle.py
Name: Hui-Hsuan Chung
----------------------------------------
Play boggle by linking non-repeated neighboring letters to find out possible words
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
N_ROW = 4


def main():
    """

    """
    boggle_plane = []  # List to store the boggle letters
    word_lst = []  # List to store the appeared letters
    boggle_words = []  # List to store the boggle game results
    # Type the boggle letters row by row
    for index in range(1, N_ROW+1):
        letter_row = input(str(index) + " row of letters: ", )
        letter_lst = [letter.lower() for letter in letter_row.split()]
        # Check the input is properly handled
        if " " not in letter_row:
            print('Illegal input')  # delimiter is not space only
            break
        else:
            if len(letter_lst) != 4:
                print('Illegal input')  # input elements are not four items
                break
            else:
                if sum([len(ele) for ele in letter_lst]) != 4:
                    print('Illegal input')  # at least one element is not a single char
                    break
                else:
                    if sum([ele.isalpha() for ele in letter_lst]) != 4:
                        print('Illegal input')  # at least one element is not a alphabet
                        break
                    else:
                        boggle_plane.append(letter_lst)
        # Prepare a non-repeated letter list for generating pre-selected vocabularies in latter steps
        for ele in letter_lst:
            if ele not in word_lst:
                word_lst.append(ele)

    start = time.time()
    ####################
    # Make a selected dictionary list based on the input word
    dict_lst = read_dictionary(word_lst)

    # Start to scan the boggle plane for different starting letter using a nested loop
    for xi in range(len(boggle_plane)):
        for yi in range(len(boggle_plane[0])):
            used_items = []                       # Initialize an empty list to store the used letters
            start_letter = boggle_plane[xi][yi]   # Starting letter
            used_items.append((xi, yi))           # Mark the starting letter a used letter
            # Let's find words from the given starting letter
            play_boggle(xi, yi, boggle_plane, used_items, start_letter, dict_lst[start_letter], boggle_words)
    # Print results
    print(f"There are {len(boggle_words)} words in total.")  # Show the words
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary(word_list, file=FILE):
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    :param word_list: (list) a list of the letters of the boggle plane
    :param file: (str) the dictionary file path
    :return: (dict) dictionary vocabularies
    """
    vocabs = {}
    with open(file, 'r') as f:
        for line in f:
            vocabulary = line.split()[0]  # parse the vocabularies
            if 16 >= len(vocabulary) >= 4:  # select the words' length
                screen_vocab = 0
                # Check the elements of the parsed vocabulary
                for ele_vocab in vocabulary:
                    if ele_vocab in word_list:
                        screen_vocab += 1
                    else:
                        break
                # Add it to the dictionary if the word contains only the letters in word_list
                if screen_vocab == len(vocabulary):
                    if vocabulary[0] not in vocabs:  # Make a dictionary: {'a': [a-word], 'b': [b-word], ...}
                        vocabs[vocabulary[0]] = [vocabulary]
                    else:
                        vocabs[vocabulary[0]].append(vocabulary)
    return vocabs


def has_prefix(dict_vocabs, sub_s):
    """
    With an input sub-string prefix, Check if it is in the dictionary vocabulary list
    :param dict_vocabs: (dict) the dictionary vocabularies
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for vocab in dict_vocabs:
        if vocab.startswith(sub_s):
            return True


def play_boggle(index_x, index_y, boggle_array, unused_letters, current_s, dict_list, boggle_list):
    """
    :param index_x: (int) x position of the letter
    :param index_y: (int) y position of the letter
    :param boggle_array: (list) input letter arrays to play boggle
    :param unused_letters: (list) a list to store the explored letter position (x, y)
    :param current_s: (str) to store the explored boggle answer
    :param dict_list: (dict) the list of dictionary vocabularies
    :param boggle_list: (list) a list to store the boggle results
    """
    # Scan the surrounding 8 letters
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:  # Exclude the starting letter
                pass
            else:
                x = index_x + i
                y = index_y + j
                # Make sure the index range is within the boggle letter array
                if 0 <= x < 4 and 0 <= y < 4:
                    explore_letter = boggle_array[x][y]
                    # If the selected letter is not explored
                    if (x, y) not in unused_letters:
                        # Choose
                        unused_letters.append((x, y))
                        # If the sub-string is the prefix of a word in dict_list
                        if has_prefix(dict_list, current_s):
                            if current_s in dict_list:
                                # Base case: find a boggle word
                                find_word = current_s
                                if current_s not in boggle_list:
                                    boggle_list.append(find_word)
                                    print('Found:', find_word)
                            # Explore
                            new_current_s = current_s + explore_letter
                            play_boggle(x, y, boggle_array, unused_letters, new_current_s, dict_list, boggle_list)
                        # Un-choose
                        unused_letters.remove((x, y))


if __name__ == '__main__':
    main()
