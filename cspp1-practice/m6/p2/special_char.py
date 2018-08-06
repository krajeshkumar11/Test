'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    s_str = input()
    z_str = ""
    for char in s_str:
        if char in "!@#$%^&*":
            z_str += " "
        else:
            z_str += char
    print(z_str)
if __name__ == "__main__":
    main()
