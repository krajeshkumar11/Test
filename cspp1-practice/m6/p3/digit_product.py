'''
Given a  number int_input, find the product of all the digits
example:
	input: 123
	output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    sign = ''
    product = 1
    if int_input < 0:
        sign = '-'
        int_input = int_input * -1

    if int_input > 0:
        while int_input > 0:
            rem = int_input%10
            product = product * rem
            int_input = int_input//10
        print sign + str(product)
    else:
        print int_input

if __name__ == "__main__":
    main()
