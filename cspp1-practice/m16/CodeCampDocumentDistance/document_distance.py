'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math

def clean_up(data):
    """
        Compute to remove non srings from given string and return list.
    """
    data_list = data.lower().split(" ")
    updated_data_list = []
    # print(data_list)
    for each_word in data_list:
        # each_word_list = each_word.split("'")
        updated_data_list.append(re.sub("[^a-z']+", "", each_word.strip()))
    # print(updated_data_list)
    return updated_data_list

def remove_stop_words(words_list):
    """
        Compute to remove stop words from given word list.
    """
    stop_words = load_stopwords("stopwords.txt")
    temp_words_list = sorted(words_list[:])
    # print(temp_words_list)
    for each_word in temp_words_list:
        if each_word in stop_words:
            # print(each_word, "DELETED")
            words_list.remove(each_word)
    # print(words_list)
    return words_list

def get_words_frequency(words_list1, words_list2):
    """
        Compute word frequency from given word lists.
    """
    # print(len(words_list1), len(words_list2))
    word_frequency = {}
    for each_word in words_list1:
        if each_word not in word_frequency:
            # print(each_word)
            word_frequency[each_word] = [1, 0]
        else:
            frequency_list = word_frequency[each_word]
            frequency_list[0] += 1
            word_frequency[each_word] = frequency_list

    for each_word in words_list2:
        if each_word not in word_frequency:
            # print(each_word)
            word_frequency[each_word] = [0, 1]
        else:
            frequency_list = word_frequency[each_word]
            frequency_list[1] += 1
            word_frequency[each_word] = frequency_list
    # print(len(word_frequency.keys()), "LENGTH")
    return word_frequency

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    list_one = clean_up(dict1)
    list_one = remove_stop_words(list_one)
    # print(list_one)
    list_two = clean_up(dict2)
    list_two = remove_stop_words(list_two)
    # print(list_two)

    word_frequency = get_words_frequency(list_one, list_two)
    numerator_product = []
    for each in word_frequency:
        each_word_freq = word_frequency[each]
        # print(each_word_freq)
        numerator_product.append(each_word_freq[0] * each_word_freq[1])

    # print(numerator_product)
    numerator = sum(numerator_product)
    # print(numerator)
    denominator_square1 = []
    denominator_square2 = []

    for each in word_frequency:
        each_word_freq = word_frequency[each]

        denominator_square1.append(each_word_freq[0]**2)
        denominator_square2.append(each_word_freq[1]**2)

    denominator = int(math.sqrt(sum(denominator_square1)) * math.sqrt(sum(denominator_square2)))
    # print(denominator)

    return float(numerator/denominator)


def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
