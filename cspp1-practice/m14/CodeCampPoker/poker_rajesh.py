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
    if all([True if each_card_value in '2345A' else False for each_card_value, s in hand]):
        return True

    card_values = set(['--23456789TJQKA'.index(each_card_value) for each_card_value in hand])
    return len(card_values) == 5 and (max(card_values) - min (card_values) == 4)

    # card_value_list = []
    # for each_card in hand:
    #     only_number = each_card[0]
    #     if only_number == 'T':
    #         card_value_list.append(10)
    #     elif only_number == 'J':
    #         card_value_list.append(11)
    #     elif only_number == 'Q':
    #         card_value_list.append(12)
    #     elif only_number == 'K':
    #         card_value_list.append(13)
    #     elif only_number == 'A':
    #         card_value_list.append(14)
    #     else:
    #         card_value_list.append(int(only_number))

    # # Sorting the list in accending order
    # card_value_list.sort()
    # iterate_i = 0

    # # Checking if difference of last and first element in list 5
    # if card_value_list[len(card_value_list)-1] - card_value_list[0] > 5:
    #     return False

    # # Checking if cards are in order
    # while iterate_i < len(card_value_list)-1:
    #     iterate_j = iterate_i + 1
    #     if card_value_list[iterate_i] > card_value_list[iterate_j]:
    #         return False
    #     iterate_i += 1

    # return True



def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''

    suit_set = set()
    for each_card in hand:
        suit_set.add(each_card[1])

    return len(suit_set) == 1

    # # Empty suit List
    # card_suit_list = []

    # # Appending only suits to empty suit list
    # for each_card in hand:
    #     card_suit_list.append(each_card[1])

    # iterate_i = 0

    # # Getting suit of first card from suit list
    # check_copy = card_suit_list[iterate_i]

    # # Checking if all cards have same suit
    # while iterate_i < len(card_suit_list)-2:
    #     iterate_i += 1
    #     iterate_j = iterate_i + 1
    #     if card_suit_list[iterate_i]  != card_suit_list[iterate_j]:
    #         return False

    # return True

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
    # is_flush(hand)

    if is_straight(hand) and is_flush(hand):
        return 3
    elif is_flush(hand):
        return 2
    elif is_straight(hand):
        return 1
    else:
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
