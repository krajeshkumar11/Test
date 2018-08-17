'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math

def clean_up(data):
    data = data.lower()
    data_list = data.split(" ")
    count = 0
    while count < len(data_list):
        data_list[count] = re.sub("[^a-z]","",data_list[count])
        count += 1

    return data_list

def remove_stop_words(word_list):
    stop_words = load_stopwords("stopwords.txt")

    temp_word_list = word_list[:]

    for each_word in temp_word_list:
        if each_word in stop_words:
            word_list.remove(each_word)

    return word_list

def get_frequencydictionary(word_list_1, word_list_2):
    freq_dict = {}

    for each_word in word_list_1:
        if each_word not in freq_dict:
            freq_dict[each_word] = [1, 0]
        else:
            freq_dict[each_word][0] += 1

    for each_word in word_list_2:
        if each_word not in freq_dict:
            freq_dict[each_word] = [0, 1]
        else:
            freq_dict[each_word][1] += 1

    return freq_dict

def compute_similarity(freq_dict):
    numerator = 0
    den_one = 0
    den_two = 0
    for each_word in freq_dict:
        freq_list = freq_dict[each_word]
        numerator += (freq_list[0] * freq_list[1])
        den_one += freq_list[0] ** 2
        den_two += freq_list[1] ** 2

    denominator = math.sqrt(den_one) * math.sqrt(den_two)

    return numerator/denominator

def similarity(d1, d2):
    '''
        Compute the document distance as given in the PDF
    '''

    d1_list = clean_up(d1)
    d2_list = clean_up(d2)

    d1_list = remove_stop_words(d1_list)
    d2_list = remove_stop_words(d2_list)

    freq_dict = get_frequencydictionary(d1_list, d2_list)

    return compute_similarity(freq_dict)

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
