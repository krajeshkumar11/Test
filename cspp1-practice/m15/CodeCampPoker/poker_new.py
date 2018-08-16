'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''

def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    face_values = get_onlyfacevalues(hand)
    # 2, 3, 4, 5, 6
    # 10, 11, 12, 13, 14
    face_set = set(sorted(face_values))
    if face_set == {2, 3, 4, 5, 14}:
        face_set = {1, 2, 3, 4, 5}

    return len(face_set) == 5 and max(face_set) - min(face_set) == 4

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    suits_set = set()
    for c, s in hand:
        suits_set.add(s)

    return len(suits_set) == 1

def is_fourofakind(hand):

    face_values = get_onlyfacevalues(hand)

    for each_face in face_values:
        if face_values.count(each_face) == 4:
            return True

    return False

def is_fullhouse(hand):
    face_values = get_onlyfacevalues(hand)

    if (face_values.count(face_values[0]) == 3 and face_values.count(face_values[len(face_values)-1]) == 2) or (face_values.count(face_values[0]) == 2 and face_values.count(face_values[len(face_values)-1]) == 3):
        return True

    return False

def is_threeofakind(hand):
    face_list = get_onlyfacevalues(hand)

    if len(set(face_list)) == 3:
        for each_face in face_list:
            if face_list.count(each_face) == 3:
                return True

    return False

def is_twopair(hand):
    face_list = get_onlyfacevalues(hand)
    if len(set(face_list)) == 3:
        count = 0
        for each_face in set(face_list):
            if face_list.count(each_face) == 2:
                count += 1
        if count == 2:
            return True

    return False

def is_onepair(hand):
    face_list = get_onlyfacevalues(hand)
    if len(set(face_list)) == 4:
        count = 0
        for each_face in set(face_list):
            if face_list.count(each_face) == 2:
                count += 1
        if count == 1:
            return True

    return False

def is_highcard(hand):
    return len(set(get_onlyfacevalues(hand))) == 5

def get_onlyfacevalues(hand):
    face_values = []
    index_str = '--23456789TJQKA'
    for c, s in hand:
        face_values.append(index_str.index(c))

    return sorted(face_values)

def get_handrank(hand, size):
    face_values = get_onlyfacevalues(hand)

    if size == 1:
        return 1/100 * max(face_values)

    for each_hand in face_values:
        if face_values.count(each_hand) == 2:
            return 1/100 * int(each_hand)

    return 0

def get_suitrank(hand):
    face_values = get_onlyfacevalues(hand)
    return 1/100 * sum(face_values)

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand


    # print(is_highcard(hand))

    if is_straight(hand) and is_flush(hand):
        return 9 +get_suitrank(hand)
    if is_fourofakind(hand):
        return 8
    if is_fullhouse(hand):
        return 7
    if is_flush(hand):
        return 6
    if is_straight(hand):
        return 5
    if is_threeofakind(hand):
        return 4
    if is_twopair(hand):
        return 3
    if is_onepair(hand):
        return 2 + get_handrank(hand, 2)
    if is_highcard(hand):
        return 1 + get_handrank(hand, 1)
    return 0

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
