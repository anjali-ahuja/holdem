import csv

def has_potential_flush(cards):
    """
    function has_potential_flush checks if in out of given cards, there are atleast 3 of the same suit

    returns: (suit of flush, a list of all cards that qualify for the flush)
    param1: a list of cards to check for flush
    """
    flush = []
    suits = dict()
    suit = ""

    for card in cards:
        if card[0] in suits.keys():
            suits[card[0]].append(card)
        else:
            suits[card[0]] = [card]
    
    max = 0
    for k,v in suits.items():
        if len(v) > max:
            max = len(v)
            suit = k

    if max >= 3:
        return (suit, suits[suit])
    return (None, [])


def generate_card_pool():
    """
    function generate_card_pool enumerates all possible cards in the game

    returns: a dictionary of all cards against their suit and rank value
    """

    card_pool = dict()

    for suit in [("S",4), ("H", 3), ("D", 2), ("C", 1)]:
        for rank in [("a",14), ("2",2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9), ("10", 10), ("j", 11), ("q", 12), ("k", 13)]: 
            card = suit[0] + rank[0]
            suit_value = suit[1]
            rank_value = rank[1]
            card_pool[card] = (suit_value, rank_value)

    return card_pool

def read_game_csv(players_csv_file, the_winner, card_pool):
    """
    function read_game_csv reads the given csv and extracts the cards for all players

    returns: 3-tuple (cards of the winner, cards of other players, remaining card pool)
    param1 players_csv_file: location of the CSV file with the hands of all players
    param2 the_winner: name of the player we want to make the winner
    param3 card_pool: cards that have not been dealt yet
    """

    # read the provided csv and extract data
    with open(players_csv_file, mode='r') as csv_file:

        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        winner_cards = []
        other_cards = dict()

        for row in csv_reader:

            # store the winner's hand separately
            if row["Player"] == the_winner:
                winner_cards = [row["Card1"], row["Card2"]]

            else:
                other_cards[row["Player"]] = [row["Card1"], row["Card2"]]

            # remove these cards from the the card_pool
            card_pool.pop(row["Card1"], None)
            card_pool.pop(row["Card2"], None)

    return (winner_cards, other_cards, card_pool)


def make_the_winner(players_csv_file, first_three_community_cards, the_winner):

    """
    function make_the_winner finds the two cards needed for a given player to become the winner
    ASSUMES THERE HAS BEEN A CHECK FOR GAME ALREADY BEING WON BY A PLAYER
    (that no one already has a Spade Royal Flush)

    returns: array of two cards
    param1 players_csv_file: location of the CSV file with the hands of all players
    param2 first_three_community_cards: self-explainatory
    param3 the_winner: name of the player we want to make the winner
    """

    # init card pool
    all_cards = generate_card_pool()
    card_pool = all_cards

    # read game csv
    winner_cards, other_cards, card_pool = read_game_csv(players_csv_file, the_winner, card_pool)

    # remove community cards from card pools and consider them as a part of everyone's hands
    for card in first_three_community_cards:
        card_pool.pop(card, None)
        winner_cards.append(card)
        for player in other_cards.keys():
            other_cards[player].append(card)
    
    # ASSUMES THERE HAS BEEN A CHECK FOR GAME ALREADY BEING WON BY A PLAYER
    # (that no one already has a Spade Royal Flush)

    return


def main():
    print("Hello Code Reviewer!")
    
    # change params here
    player_csv_file = 'tests\\test1.csv'
    first_three_community_cards = ['S10', 'D1', 'Cj']
    the_winner = "David"

    # make_the_winner(player_csv_file, first_three_community_cards, the_winner)
    print(has_potential_flush(['H2', 'S3', 'S4', 'D5', 'H6']))

if __name__ == "__main__":
    main()


