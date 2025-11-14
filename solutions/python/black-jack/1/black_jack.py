"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


face_cards_ace = {'K': 10, 'Q': 10, 'J': 10, 'A': 1}
other_cards = {'10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

# return integer
def value_of_card(card) -> int:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card in face_cards_ace:
        return face_cards_ace[card]
    if card in other_cards:
        num_card = other_cards[card]
        return num_card
    
    return -1


v = value_of_card('K')


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if value_of_card(card_one) < value_of_card(card_two):
        return card_two
    elif value_of_card(card_one) > value_of_card(card_two):
        return card_one
    else:
        return (card_one, card_two)
        

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if card_one == 'A' or card_two == 'A':
        return 1

    two_card_value = value_of_card(card_one) + value_of_card(card_two)
    remainder = 21 - two_card_value

    if remainder < 11:
        return 1
    if remainder >= 11:
        return 11


value_of_ace('2', '5')


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """  
    if card_one == 'A' and card_two == 'A':
        return False
    if card_one in face_cards_ace and card_two == '10':
        return True
    if card_one == 'A' and card_two in face_cards_ace:
        return True
    if card_one == '10' and card_two == '10':
        return True
    if card_one == '10' and card_two in face_cards_ace:
        return True
    return False

is_blackjack('A', '10')


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    if card_one == card_two:
        return True
    if card_one in face_cards_ace and card_two in face_cards_ace:
        return True
    return False

can_split_pairs('A', 'Q')


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    if value_of_card(card_one) + value_of_card(card_two) == 9:
        return True
    if value_of_card(card_one) + value_of_card(card_two) == 10:
        return True
    if value_of_card(card_one) + value_of_card(card_two) == 11:
        return True
    return False


can_double_down('A', '9')
