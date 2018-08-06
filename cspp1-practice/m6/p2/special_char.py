'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    s = str(input())
    z = ""
    for n in s:
        if n == "!" or n == "@" or n == "#" or n == "$" or n == "%" or n == "^" or n == "&" or n == "*":
             z+=" "
        else:
            z+=n
    print(z)
main()
