'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
	s = raw_input()
	# the input string is in s
	# remove pass and start your code here
	char = "bob"
	count = 0
	for index in range(len(s)):
		newst = s[index:len(s)]
		if(newst.find(char) != -1)
			count = count + 1

	print("Number of times bob occurs is: " + str(count))


if __name__== "__main__":
	main()
