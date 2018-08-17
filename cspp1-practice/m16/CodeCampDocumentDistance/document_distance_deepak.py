'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math

def tokenize(s):
	regex = re.compile('[^a-z]')
	return [regex.sub('', w.strip()) for w in s.lower().split(' ')]

def vectorize(dictionary, words, index):
	stop_words = load_stopwords('stopwords.txt')
	for w in words:
		if w not in stop_words and len(w) > 0:
			if w not in dictionary: dictionary[w] = [0,0]
			dictionary[w][index] += 1
	return dictionary

def compute_distance(dictionary):
	n = sum([k[0] * k[1] for k in dictionary.values()])
	d1 = math.sqrt(sum([k[0] ** 2 for k in dictionary.values()]))
	d2 = math.sqrt(sum([k[1] ** 2 for k in dictionary.values()]))
	return n/(d1*d2)

def similarity(d1, d2):
    '''
        Compute the document distance as given in the PDF
    '''
    dictionary = dict()
    dictionary = vectorize(dictionary, tokenize(d1), 0)
    dictionary = vectorize(dictionary, tokenize(d2), 1)
    # print(sorted(dictionary[""]))
    return compute_distance(dictionary)

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
