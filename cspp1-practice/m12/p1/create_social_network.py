'''
    Assignment-1 Create Social Network
'''

def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''

    # remove the pass below and start writing your code
    # print(data)
    myDict = {}
    data_list = data.split("\n")
    for user in data_list:
        user_details = user.split(" follows ")
        user_friends_list = user_details[1].split(",")
        myDict[user_details[0]] = user_friends_list

    return myDict

def main():
    '''
        handling testcase input and printing output
    '''
    # string = 'John follows Bryant,Debra,Walter\nBryant follows Olive,Ollie,Freda,Mercedes\nMercedes follows Walter,Robin,Bryant\nOlive follows John,Ollie\nDebra follows Walter,Levi,Jennie,Robin\nWalter follows John,Levi,Bryant\nLevi follows Ollie,John,Walter\nOllie follows Mercedes,Freda,Bryant\nJennie follows Levi,John,Freda,Robin\nRobin follows Ollie\nFreda follows Olive,John,Debra'
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'

    print(create_social_network(string))

if __name__ == "__main__":
    main()
