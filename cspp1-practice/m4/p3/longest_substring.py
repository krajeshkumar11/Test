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
    S = input()
	# the input string is in s
	# remove pass and start your code here
	# s1 = 'abcabcd'
    # s1 = s

    START = 0
    END = 0
    COUNT = 0
    I = 0
    TEMPI = I
    FLAG = 0
    while I < (len(S)-1):
        J = I + 1
        # print(str(i) + " " + str(j) + ' comparison between: ' + s[i] + " < " + s[j])
        if(S[I] > S[J]):
            FLAG = 1
            # print(False)
        # else:
            # print(True)

            # print(str(j) + " " + str((len(s)-1)))
        if (J == (len(S) - 1)):
            J += 1
        # print(str(j))
        # print(str(i) + " " + str((len(s)-2)) + " " + str(count) + " " + str(j-tempi))
        if (I == (len(S)-2) and COUNT < (J-TEMPI)):
            FLAG = 1

        if FLAG == 1:
            # print("i is: " +  str(j-tempi))
            if COUNT < (J-TEMPI):
                START = TEMPI
                END = j
                COUNT = END - START

            TEMPI = I + 1
            FLAG = 0
            # print(str(tempi) + " " + str(flag))

        I = i + 1
    print(S[START:END])


if __name__== "__main__":
	main()
