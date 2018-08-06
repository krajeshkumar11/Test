'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''
    Read number from the input, store it in variable num.
    '''
n = int(input())
i=0
for i in range(1,n+1,1):
    if(n%3==0 and n%5==0):
       print("fizz")
       print("buzz")
       break
    elif(n%3==0):
        print("fizz")
        break
    elif(n%5==0):
        print("Buzz")
        break
    else:
        print(i)


