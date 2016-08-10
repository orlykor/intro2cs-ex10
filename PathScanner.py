import os
from WordExtractor import *
from WordTracker import  *

FIRST_PLACE = 0
EMPTY = 0
BEGINNING = 0
DEFAULT = 1

class PathIterator(object):
    """
    An iterator which iterates over all the directories and files
    in a given path (note - in the path only, not in the
    full depth). There is no importance to the order of iteration.
    """

    def __init__(self, path):
        """
        Initiate a new PathIterator instance.
        :param path: A string representing an absolute or relative path. 
        """
        self.path = path

    def __iter__(self):
        """
        Returns an iterator which iterates over the paths of files and folders
        in the given path(i.e - self)
        :return: An iterator which iterates over the path in the
        *source file*
        """
        #check if its a file or a directory
        if os.path.isfile(self.path):
            self.list_namefiles = []
        else:
            self.list_namefiles = os.listdir(self.path)

        return self


    def __next__(self):
        """
        Iterates over the files and folders in the given path .
        :return: A the files and folders paths.
        """
        #if the list of file is not empty
        if len(self.list_namefiles) > EMPTY:
            file_name = self.list_namefiles.pop(FIRST_PLACE) #put in the list
            #make a new joint path
            sub_path = os.path.join(self.path, file_name)
            return sub_path
        else:
            raise StopIteration




def path_iterator(path):
    """
    Returns an iterator to the current path's filed and directories.
    Note - the iterator class is not outlined in the original
     version of this file - but rather is should be designed
     and implemented by you.
    :param path: A (relative or an absolute) path to a directory.
    It can be assumed that the path is valid and that indeed it
    leads to a directory (and not to a file).
    :return: An iterator which returns all the files and directories
    in the *current* path (but not in the *full depth* of the path).
    """
    return PathIterator(path)



def print_tree(path, sep='  '):
    """
    Print the full hierarchical tree of the given path.
    Recursively print the full depth of the given path such that
    only the files and directory names should be printed (and not
    their full path), each in its own line preceded by a number
    of separators (indicated by the sep parameter) that correlates
    to the hierarchical depth relative to the given path parameter.
    :param path: A (relative or an absolute) path to a directory.
    It can be assumed that the path is valid and that indeed it
    leads to a directory (and not to a file).
    :param sep: A string separator which indicates the depth of
     current hierarchy.
    """
    depth = BEGINNING
    return print_tree_helper(path, depth, sep)


def print_tree_helper(path, depth, sep):
    """
    this is the Recursive func that goes deeply through the given path from
    class PathIterator. it prints the file or folder name with its depth path.
    """
    for i in path_iterator(path):
        file_name = os.path.basename(i) #take the name of the file
        print(sep * depth + file_name)
        if os.path.isdir(i): #check if its a directory
            #we want to go recursively through all the paths inside it
            print_tree_helper(i, depth + DEFAULT, sep)

    return None




def file_with_all_words(path, word_list):
    """
    Find a file in the full depth of the given path which contains
    all the words in word_list.
    Recursively go over  the files in the full depth of the given
    path. For each, check whether it contains all the words in
     word_list and if so return it.
    :param path: A (relative or an absolute) path to a directory.
    In the full path of this directory the search should take place.
    It can be assumed that the path is valid and that indeed it
    leads to a directory (and not to a file).
    :param word_list: A list of words (of strings). The search is for
    a file which contains this list of words.
    :return: The path to a single file which contains all the
    words in word_list if such exists, and None otherwise.
    If there exists more than one file which contains all the
    words in word_list in the full depth of the given path, just one
    of theses should be returned (does not matter which).
    """

    for new_path in path_iterator(path):

        if os.path.isfile(new_path): #if its a file
            chosen_file = WordExtractor(new_path) #get the words in the file
            #these are the words we want to check
            dictionary = WordTracker(word_list)
            for word in chosen_file:
                #check if a word from the dictionary is in the file
                dictionary.encounter(word)
            if dictionary.encountered_all():
                return new_path

        elif os.path.isdir(new_path): #check if its folder

            #we want to go recursively thorugh all the paths inside it
            file_with_all_words(new_path, word_list)

    return None



