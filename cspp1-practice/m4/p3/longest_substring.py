'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.'''

def main():
    s = raw_input()
	# the input string is in s
	# remove pass and start your code here
	# s1 = 'abcabcd'
    s1 = s

    start = 0
    end = 0
    count = 0
    x = 0
    tempx = x
    flag = 0
    while x < (len(s1)-1):
        y = x + 1
        # print(str(x) + " " + str(y) + ' comparison between: ' + s1[x] + " < " + s1[y])
        if(s1[x] > s1[y]):
            flag = 1
            # print(False)
        # else:
            # print(True)

            # print(str(y) + " " + str((len(s1)-1)))
        if (y == (len(s1) - 1)):
            y += 1
        # print(str(y))
        # print(str(x) + " " + str((len(s1)-2)) + " " + str(count) + " " + str(y-tempx))
        if (x == (len(s1)-2) and count < (y-tempx)):
            flag = 1

        if flag == 1:
            # print("X is: " +  str(y-tempx))
            if count < (y-tempx):
                start = tempx
                end = y
                count = end - start

            tempx = x + 1
            flag = 0
            # print(str(tempx) + " " + str(flag))

        x = x + 1
    print(s1[start:end])


if __name__== "__main__":
	main()
