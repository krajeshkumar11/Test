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
    str_output = ""
    array_check = ["!", "@", "#", "$", "%", "^", "&", "*"]
    temp_i = 0
    for i in range(len(str_input)):
        flag = 0
        if str_input[i] in array_check:
            str_output += str_input[temp_i:i] + " "
            flag = 1
        if flag == 1:
            temp_i = i + 1
    if len(str_output) != len(str_input):
        str_output += str_input[temp_i:]
    print(str_output)
if __name__ == "__main__":
    main()
