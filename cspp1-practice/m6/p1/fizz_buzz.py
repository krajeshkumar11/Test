"""program to print nos from 1 to N"""

def main():
    n = int(input())
    """input from the user"""
    for i in range (1,n+1):
        if (i%3==0 and i%5==0):
            print("Fizz")
            print("Buzz")
        elif (i%3==0):
            print("Fizz")
        elif (i%5==0):
            print("Buzz")
        else:
            print(i)
main()
