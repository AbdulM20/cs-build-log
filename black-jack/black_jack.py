"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    # Here I learned to use in for groups
    # simple conditional that says if a card is part of a certain group return the above associated values
    if card in ('J','Q','K'):
        return 10
    elif card  == 'A':
        return 1
    else:
        return int(card)

    pass


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    # This conditional returns the value of the highest card unless they are the same
    # in which case it returns a tuple of the 2 equal cards
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    elif value_of_card(card_one) < value_of_card(card_two):
        return card_two
    else:
        return (card_one,card_two)

    pass


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    # The ace card here is different from the first function where it is mentioned
    # It can either be a value of 1 or 11
    # If the values of card one and two sum to be less than 9 then the next card is 11 else it's 1
    # I chose to do it with helper logic
    # Initially ace is set to 1
    # I need ace to be 11 in this case so that when summed an accurate value is produced for comparison
    # if the value is less than or equal to 9 then the next ace returns a 11 else a 1

    value_one = 11 if card_one == 'A' else value_of_card(card_one)
    value_two = 11 if card_two == 'A' else value_of_card(card_two)

    if value_one + value_two <= 9:
       return 11
    else:
        return 1

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    # Determine whether cards dealt are blackjack or not
    # 2 cards must add to 21 to be blackjack
    # Only an ace and a face card can = blackjack
    # Same override as in the last function
    # Add the two values and if they == 21 then return the boolean

    value_one = 11 if card_one == 'A' else value_of_card(card_one)
    value_two = 11 if card_two == 'A' else value_of_card(card_two)

    return value_one + value_two == 21


    pass


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    pass


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    pass
