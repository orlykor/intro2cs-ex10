#!/usr/bin/env python3
import random

EMPTY = 0
FIRST_PLACE = 0
HALF = 2
ONE_RIGHT = 1
ONE_LEFT = 1
MOVE_ONE = 1
LAST_CELL = 1

class WordTracker(object):
    """
    This class is used to track occurrences of words.
     The class uses a fixed list of words as its dictionary
     (note - 'dictionary' in this context is just a name and does
     not refer to the pythonic concept of dictionaries).
     The class maintains the occurrences of words in its
     dictionary as to be able to report if all dictionary's words
     were encountered.
    """

    def __init__(self, word_list):
        """
        Initiates a new WordTracker instance.
        :param word_list: The instance's dictionary.
        """
        self.original_list = list(word_list) 
        self.dictionary_words = self.original_list[:] #copy the list
        self.all_encountered_words = []
        self.quicksort(self.dictionary_words) #get a sorted list


    def __contains__(self, word):
        """
        Check if the input word in contained within dictionary.
         For a dictionary with n entries, this method guarantees a
         worst-case running time of O(n) by implementing a
         binary-search.
        :param word: The word to be examined if contained in the
        dictionary.
        :return: True if word is contained in the dictionary,
        False otherwise.
        """
        #look if the word is in the list:
        if self.binary_search(self.dictionary_words, word):
            return True
        else:
            False


    def encounter(self, word):
        """
        A "report" that the give word was encountered.
        The implementation changes the internal state of the object as
        to "remember" this encounter.
        :param word: The encountered word.
        :return: True if the given word is contained in the dictionary,
        False otherwise.
        """

        if self.__contains__(word): #check if the word is in the list of words
            #we make a list in a certain order
            self.encountered_words_sort(self.all_encountered_words, word)
            return True

        else:
            return False


    def encountered_words_sort(self, encounter_word, word):
        """
        put the given word in the right place in the list.
        if there is the same word, it only enters it once
        """
        if len(self.all_encountered_words) == EMPTY: #if the list is empty
            self.all_encountered_words.insert(FIRST_PLACE, word)

        bottom = FIRST_PLACE #beginning of the list
        top = len(encounter_word)-LAST_CELL

        while top >= bottom:
            middle = (top + bottom) // HALF
            #check if the word in the middle is larger or smaller then the
            #input word
            if encounter_word[middle] < word:
                bottom = middle + ONE_RIGHT #change the bottom
            elif encounter_word[middle] > word:
                top = middle - ONE_LEFT
            else:
                return
            # we check again now inorder to insert the word
        if encounter_word[middle] > word:
            self.all_encountered_words.insert(middle, word)
        if encounter_word[middle] < word:
            self.all_encountered_words.insert(middle + ONE_RIGHT, word)
        else:
            return

        return False


    def encountered_all(self):
        """
        Checks whether all the words in the dictionary were
        already "encountered".
        :return: True if for each word in the dictionary,
        the encounter function was called with this word;
        False otherwise.
        """

        # if the input list of words is as the same length as the list of
        #the encountered  words, then all the words have been encountered.
        if len(self.all_encountered_words) == len(self.dictionary_words):
            return True
        else:
            return False


    def reset(self):
        """
        Changes the internal representation of the instance such
        that it "forget" all past encounters. One implication of
        such forgetfulness is that for encountered_all function
        to return True, all the dictionaries' entries should be
        called with the encounter function (regardless of whether
        they were previously encountered ot not).
        """
        self.all_encountered_words = [] #reset it by making a new list.

    def binary_search(self, sorted_data, word):
        """returns the index of the word in the data,
           if it was found. None otherwise"""
        bottom = FIRST_PLACE #The first cell in the suspected range
        top = len(sorted_data)-LAST_CELL #the last cell

        while top >= bottom:
            middle = (top+bottom) // HALF
            #check if the word in the middle is larger or smaller then the
            #input word
            if sorted_data[middle] < word:
                bottom = middle + ONE_RIGHT
            elif sorted_data[middle] > word:
                top = middle - ONE_LEFT
            else:
                return True
        return False


    def quicksort(self, data):
        """quick-sorts a list """
        self._quicksort_helper(data, FIRST_PLACE, len(data))
        return data

    def swap(self, data, ind1, ind2):
        """swaps two items in a list"""
        data[ind1], data[ind2] = data[ind2], data[ind1]


    def partition(self, data, start, end):
        """partitions the list (from start to end) around
        a randomly selected pivot"""
        #assumes start<end
        #select a random pivot, place it in the last index

        pivot_ind = random.randrange(start, end)
        pivot_val = data[pivot_ind]
        self.swap(data, pivot_ind, end-ONE_LEFT)
        pivot_ind = end-ONE_LEFT
        end -= ONE_LEFT

        while start < end:
            #check if the chosen item is larger or smaller then the
            #one in the pivot
            if(data[start]) < pivot_val:
                start += ONE_RIGHT
            elif(data[end-ONE_LEFT]) >= pivot_val:
                end -= ONE_LEFT
            else:
                self.swap(data, start, end-ONE_LEFT)
                start += ONE_RIGHT
                end -= ONE_LEFT

        #swap pivot into place.
        self.swap(data, pivot_ind, start)
        return start


    def _quicksort_helper(self, data, start, end):
        """A helper fucntion for quick-sort's recursion."""
        #start is the first index to sort,
        #end is the index _after_ the last one
        if start < end-ONE_LEFT:
            pivot_index = self.partition(data, start, end)
            self._quicksort_helper(data, start, pivot_index)
            self._quicksort_helper(data, pivot_index + MOVE_ONE, end)






