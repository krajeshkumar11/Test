'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the inputthe output is ab   cd
Output has three spaceswhich are to be replaced with these special characters
'''
def main():
    '''
    Read string from the inputstore it in variable str_input.
    '''
    str_input = input()
    result = ''
    for char in str_input:
        if checkbool(char):
            result = result + ' '
        else:
            result = result + char
    print(result)

def checkbool(char):
    '''
    Checking if given character is Special Character or not.
    '''
    special_character = '!@#$%^&*'
    return char in special_character

if __name__ == "__main__":
    main()
