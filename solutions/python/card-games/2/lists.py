"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    round_list_1 = [number, number + 1, number + 2,]
    
    return round_list_1


get_rounds(27)


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    combined_round_list = rounds_1 + rounds_2
    return combined_round_list


concatenate_rounds([27, 28, 29], [35, 36])


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    if number in list(rounds):
        return True
    return False


list_contains_round([27, 28, 29, 35, 36], 40)


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    hand_avg = sum(hand) / len(hand)
    return hand_avg


card_average([1])


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    approx_avg = (hand[0] + hand[-1]) / 2

    middle_card_index = len(hand) // 2
    
    median = hand[middle_card_index]
    
    hand_avg = sum(hand) / len(hand)

    if hand_avg in {approx_avg, median}:
        return True
    return False
        

approx_average_is_average([2, 3, 4, 8, 8])


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_step = hand[0: : 1]
    avg_of_even_step = sum(even_step) / len(even_step)

    odd_step = hand[0: : 2]
    avg_of_odd_step = sum(odd_step) / len(odd_step)

    if avg_of_even_step == avg_of_odd_step:
        return True
    return False


average_even_is_average_odd([1, 2, 3, 4])



def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2
        return hand
    return hand


maybe_double_last([5, 9, 11])
