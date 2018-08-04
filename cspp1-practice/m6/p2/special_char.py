'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the inputthe output is ab   cd
Output has three spaceswhich are to be replaced with these special characters
'''
def main():
    '''
    Read string from the inputstore it in variable str_input.
    '''
    str_input = raw_input()
    result = ''
    for char in str_input:
        if checkBool(char):
            result = result + ' '
        else:
            result = result + char
    print result

def checkBool(char):
    special_character = '!@#$%^&*'
    if char in special_character:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
