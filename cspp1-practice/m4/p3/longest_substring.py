'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem maj be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.'''

def main():
    s = raw_input()
	# the input string is in s
	# remove pass and start your code here
	# s1 = 'abcabcd'
    # s1 = s

    start = 0
    end = 0
    count = 0
    i = 0
    tempi = i
    flag = 0
    while i < (len(s)-1):
        j = i + 1
        # print(str(i) + " " + str(j) + ' comparison between: ' + s[i] + " < " + s[j])
        if(s[i] > s[j]):
            flag = 1
            # print(False)
        # else:
            # print(True)

            # print(str(j) + " " + str((len(s)-1)))
        if (j == (len(s) - 1)):
            j += 1
        # print(str(j))
        # print(str(i) + " " + str((len(s)-2)) + " " + str(count) + " " + str(j-tempx))
        if (i == (len(s)-2) and count < (j-tempx)):
            flag = 1

        if flag == 1:
            # print("i is: " +  str(j-tempx))
            if count < (j-tempx):
                start = tempx
                end = j
                count = end - start

            tempi = i + 1
            flag = 0
            # print(str(tempx) + " " + str(flag))

        i = i + 1
    print(s[start:end])


if __name__== "__main__":
	main()
