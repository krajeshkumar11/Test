'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    int_input = int(input())
    str_i = str(int_input)
    product = 1
    for i in str_i:
        product = product * int(i)
    print(product)
if __name__ == "__main__":
    main()
