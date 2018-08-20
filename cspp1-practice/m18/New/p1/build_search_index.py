'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.
    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
import re

# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    stop_words = load_stopwords('stopwords.txt')
    text_lst = text.lower().split(" ")
    count = 0
    while count < len(text_lst):
        text_lst[count] = re.sub('[^a-z]','',text_lst[count])
        if text_lst[count] in stop_words:
            text_lst.remove(text_lst[count])
            count -= 1
        count += 1
    return text_lst


def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)
    search_index = {}
    # iterate through all the docs
    count = 0
    while count < len(docs):
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list
        each_lst = word_list(docs[count])
        # add or update the words of the doc to the search index
        new_count = 0
        while new_count < len(each_lst):
            if each_lst[new_count] not in search_index:
                search_index[each_lst[new_count]] = [(count, 1)]
            else:
                each_word_freq_list = search_index[each_lst[new_count]]
                flag = 0
                freq_tuple = (count, 1)

                freq_index = 0
                while  freq_index < len(each_word_freq_list):
                    freq_lst = list(each_word_freq_list[freq_index])
                    if freq_lst[0] == count:
                        freq_lst[1] += 1
                        each_word_freq_list[freq_index] = tuple(freq_lst)
                        flag = 1
                        break

                    freq_index += 1

                if flag == 0:
                    each_word_freq_list.append(freq_tuple)

                # search_index[each_lst[new_count]] = each_word_freq_list

            new_count += 1


        count += 1
    # return search index
    return search_index

# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1

    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
