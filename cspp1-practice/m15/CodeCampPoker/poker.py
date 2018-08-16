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
    # # hand = ['2D', '3S', '5S', '4C', '6D']
    # hand_cards = []
    # for c, s in hand:
    #     hand_cards.append(c)

    # face_values = '--23456789TJQKA'

    # updated_hand_cards = []

    # for each_val in hand_cards:
    #     updated_hand_cards.append(face_values.index(each_val))

    # print(updated_hand_cards)
    # # hand = ['2D', '3S', '5S', '4C', '6D']

    card_values = sorted(get_onlyfacevalues(hand))
    if card_values == [2, 3, 4, 5, 14]:
        card_values = [1, 2, 3, 4, 5]
    card_values = set(card_values)
    return len(card_values) == 5 and (max(card_values) - min (card_values) == 4)

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    # cards_suit_list = []
    # for c, s in hand:
    #     cards_suit_list.append(s)

    # cards_suit = set(cards_suit_list)

    # return len(cards_suit) == 1
#
    suit_set = set(get_onlysuitvalues(hand))
    return len(suit_set) == 1

def is_foudofkind(hand):
    """
        Four of a kind
    """
    face_set = set(get_onlyfacevalues(hand))
    return len(face_set) == 2

def is_fullhouse(hand):
    """
        Full House
    """
    face_set = set(get_onlyfacevalues(hand))

    set_tolist = list(face_set)

    if len(face_set) == 2:
        freq_dict = get_frequencydict(hand)
        two_count = 0
        three_count = 0
        for each_face in set_tolist:
            if freq_dict[each_face] == 3:
                three_count += 1
            elif freq_dict[each_face] == 2:
                two_count += 1

        if two_count != 2 and three_count != 3:
            return False

        return True

    return False

def is_threeofkind(hand):
    """
        Three of a Kind
    """
    face_set = set(get_onlyfacevalues(hand))
    return len(face_set) == 3

def is_twopair(hand):
    """
        Two of a Kind
    """
    face_set = set(get_onlyfacevalues(hand))

    set_tolist = list(face_set)
    if len(face_set) == 3:
        freq_dict = get_frequencydict(hand)
        two_count = 0
        one_count = 0
        for each_face in set_tolist:
            if freq_dict[each_face] == 2:
                two_count += 1
            elif freq_dict[each_face] == 1:
                one_count += 1

        if two_count != 2 and one_count != 1:
            return False

        return True

    return False

def is_onepair(hand):
    """
        One of a Kind
    """
    face_set = set(get_onlyfacevalues(hand))
    return len(face_set) == 4

def is_highcard(hand):
    """
        High Cards
    """
    face_set = set(get_onlyfacevalues(hand))
    return len(face_set) == 5

def generate_rank(hand, n, sorted = None):
    freq_dict = get_frequencydict(sorted(get_onlyfacevalues(hand)))
    onepair_face = 0
    for each_face in freq_dict:
        if freq_dict[each_face] == n:
            onepair_face = 1/100 * int(each_face)
            break
    return onepair_face

def get_frequencydict(hand):
    """
        Generate Dictionary with frequencies.
    """
    freq_dict = {}
    for each_card in hand:
        if each_card not in freq_dict:
            freq_dict[each_card] = 1
        else:
            freq_dict[each_card] += 1

    return freq_dict

def get_onlyfacevalues(hand):
    """
        Getting only Face Values
    """
    face_values = []
    for each_card in hand:
        face_values.append('--23456789TJQKA'.index(each_card[0]))

    return face_values

def get_onlysuitvalues(hand):
    """
        Getting only Suit Values
    """
    suit_values = []
    for each_card in hand:
        suit_values.append(each_card[1])

    return suit_values

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
    # Each card is coded as a 2 character string. Example King of Hearts is KH
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
    # get_frequencydict(hand)

    if is_straight(hand) and is_flush(hand):
        face_values = get_onlyfacevalues(hand)
        totalstraight_face = sum(face_values) / 100
        return 9 + totalstraight_face
    if is_foudofkind(hand):
        return 8 + generate_rank(hand, 4)
    if is_fullhouse(hand):
        return 7 + generate_rank(hand, 3) + generate_rank(hand, 2)
    if is_flush(hand):
        return 6
    if is_straight(hand):
        return 5
    if is_threeofkind(hand):
        return 4 + generate_rank(hand, 3)
    if is_twopair(hand):
        return 3
        # + generate_rank(hand, 2) + generate_rank(hand, 2, True)
    if is_onepair(hand):
        return 2 + generate_rank(hand, 2)
    if is_highcard(hand):
        card_facevalues = get_onlyfacevalues(hand)
        highcard_face = 0
        if 14 in card_facevalues:
            highcard_face = 1/100 * 14
        return 1 + highcard_face
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
