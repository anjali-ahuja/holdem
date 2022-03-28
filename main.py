import csv

def generate_card_pool():

    card_pool = set()

    for suit in [("S",4), ("H", 3), ("D", 2), ("C", 1)]:
        for rank in [("a",14), ("2",2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9), ("10", 10), ("j", 11), ("q", 12), ("k", 13)]: 
            card = suit[0]+rank[0]
            rank_value = rank[1]
            suit_vale = suit[1]

def read_game_csv(players_csv_file, the_winner):
    """
    function read_game_csv reads the given csv and extracts the cards for all players

    returns: 2-tuple (cards of the winner, cards of other players)
    param1 players_csv_file: location of the CSV file with the hands of all players
    param2 the_winner: name of the player we want to make the winner
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

    return (winner_cards, other_cards)


def make_the_winner(players_csv_file, first_three_community_cards, the_winner):

    """
    function make_the_winner finds the two cards needed for a given player to become the winner

    returns: array of two cards
    param1 players_csv_file: location of the CSV file with the hands of all players
    param2 first_three_community_cards: self-explainatory
    param3 the_winner: name of the player we want to make the winner
    """

    print(read_game_csv(players_csv_file, the_winner))

    return


def main():
    print("Hello KPMG!")
    
    # change params here
    player_csv_file = 'tests\\test1.csv'
    first_three_community_cards = []
    the_winner = "David"

    make_the_winner(player_csv_file, first_three_community_cards, the_winner)

if __name__ == "__main__":
    main()


