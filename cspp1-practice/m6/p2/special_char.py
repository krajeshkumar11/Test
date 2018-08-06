'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
str_in = input()
str_p = ""
array = ["!","@","#","$","%","^","&","*"]
l_q = 0
for i in range(len(str_in)):
    flag = 0
    if str_in[i] in array:
        str_p += str_in[l_q:i] +  " "
        flag = 1
    if flag == 1:
        l_q = i+1
    if len(str_p) != len(str_in):
        str_p += str_in[l_q:]
print(str_p)
main()
