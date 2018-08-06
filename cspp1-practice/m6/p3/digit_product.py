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
    n_p = int(input())
    while n_p > 0:
        if n_p > 0:
            rem_1 = n_p%10
            n_p = n_p//10
        if n_p > 0:
            rem_2 = n_p%10
            n_p = n_p//10
        if n_p > 0:
            rem_3 = n_p%10
            n_p = n_p//10
            p_n = rem_1*rem_2*rem_3
    print(p_n)
main()



