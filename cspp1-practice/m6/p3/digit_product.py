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
    int_input1 = int_input
    if int_input < 0:
        int_input1 = -int_input1
    product = 1
    string_input = str(int_input1)
    for i in string_input:
        product = product * int(i)
    if int_input < 0 and product != 0:
        print("-" + str(product))
    else:
        print(product)
if __name__ == "__main__":
    main()
