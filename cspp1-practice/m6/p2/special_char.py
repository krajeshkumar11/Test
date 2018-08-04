'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    result = ''
    for char in str_input:
        if char == '!' or char == '@' or char == '#' or char == '$' or char == '%' or char == '^' or char == '&' or char == '*':
            result = result + ' '
        else:
            result = result + char
    print result


if __name__ == "__main__":
    main()
