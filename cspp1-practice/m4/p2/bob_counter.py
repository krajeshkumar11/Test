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
		pos = newst.find(char) 
		if(pos != -1):
			if((pos+len(char) <= len(s)) and newst[pos:pos+3] == char):
				count = count + 1

	print(count)


if __name__== "__main__":
	main()
