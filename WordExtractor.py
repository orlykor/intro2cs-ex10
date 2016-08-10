#!/usr/bin/env python3

SIGN_EOF = ''
EMPTY = 0
FIRST_WORD = 0
class WordExtractor(object):
    """
    This class should be used to iterate over words contained in files.
     The class should maintain space complexity of O(1); i.e, regardless
     of the size of the iterated file, the memory requirements ofa class
     instance should be bounded by some constant.
     To comply with the space requirement, the implementation may assume
     that all words and lines in the iterated file are bounded by some
     constant, so it is allowed to read words or lines from the
     iterated file (but not all of them at once).
    """

    def __init__(self, filename):
        """
        Initiate a new WordExtractor instance whose *source file* is
        indicated by filename.
        :param filename: A string representing the path to the instance's
        *source file*
        """
        self.list_of_words = [] # i start the list of words
        self.file = filename
        self.f = open(filename,'r')

    def __iter__(self):
        """
        Returns an iterator which iterates over the words in the
        *source file* (i.e - self)
        :return: An iterator which iterates over the words in the
        *source file*
        """
        return self

    def __line__(self):
        #if it reached to the end of the file, and there no lines,
        # then stop the iteration
        line = self.f.readline() #here i have my line
        self.list_of_words = line.split() #here i have a list of the words

        if line == SIGN_EOF: # if i've reached to the end of the file
            return True

    def __next__(self):
        """
        Make a single word iteration over the source file.
        :return: A word from the file.
        """
        while len(self.list_of_words) == EMPTY: #empty lines
            if self.__line__():
                self.f.close()
                raise StopIteration

        word = self.list_of_words.pop(FIRST_WORD) #take a word out
        return word








