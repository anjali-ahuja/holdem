
import csv

# dict to store numeric values of ranks
rank_value = {"a": 14, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "j": 11, "q": 12, "k": 13 }

def is_flush(cards):
    """
    function is_flush checks if the given cards create a flush

    returns: boolean answer
    param1: a list of cards to check for flush
    """
    suit = cards[0][0]

    for card in cards:
        if card[0] != suit:
            return False

    return True

def is_straight(cards):
    """
    function is_flush checks if the given cards create a straight

    returns: boolean answer
    param1: a list of cards to check for straight
    """
    sorted_ranks = sorted([rank_value[card[1:]] for card in cards])

    prev = sorted_ranks[0]
    for rank in sorted_ranks[1:]:
        if rank != prev + 1:
            return False
        prev += 1

    return True

def is_full_house(cards):
    """
    function is_flush checks if the given cards create a full_house

    returns: boolean answer
    param1: a list of cards to check for a full_house
    """

    sorted_ranks = sorted([rank_value[card[1:]] for card in cards])

    # lazy return if the number of unique ranks is not 2
    if len((set(sorted_ranks))) != 2:
        return False
    
    # check if the repeated ranks occur 2 or 3 times
    prev = sorted_ranks[0]
    match_len = 1
    for rank in sorted_ranks[1:]:
        if rank == prev:
            match_len += 1
        else:
            if match_len == 2 or match_len == 3:
                return True

    return False

def is_four_pair(cards):
    """
    function is_flush checks if the given cards create a four_pair

    returns: boolean answer
    param1: a list of cards to check for a four_pair
    """

    sorted_ranks = sorted([rank_value[card[1:]] for card in cards])

    # lazy return if the number of unique ranks is not 2
    if len((set(sorted_ranks))) != 2:
        return False

    # check if the repeated ranks occur 1 or 4 times
    prev = sorted_ranks[0]
    match_len = 1
    for rank in sorted_ranks[1:]:
        if rank == prev:
            match_len += 1
        else:
            if match_len == 1 or match_len == 4:
                return True

    return False


def is_royal(cards):
    """
    function is_royal checks if the given STRAIGHT is royal

    returns: boolean answer
    param1: a list of cards(straight) is royal
    """   
    for card in cards:
        if card[1] == 'a':
            return True
        
    return False


def generate_card_pool():
    """
    function generate_card_pool enumerates all possible cards in the game

    returns: returns a list of all cards
    """

    card_pool = []

    for suit in "SHDC":
        for rank in ["a", "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k"]: 
            card = suit + rank
            card_pool.append(card)

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
        winner_cards = []
        other_cards = dict()

        for row in csv_reader:

            # store the winner's hand separately
            if row["Player"] == the_winner:
                winner_cards = [row["Card1"], row["Card2"]]

            else:
                other_cards[row["Player"]] = [row["Card1"], row["Card2"]]

            # remove these cards from the the card_pool
            card_pool.remove(row["Card1"])
            card_pool.remove(row["Card2"])

        

    return (winner_cards, other_cards, card_pool)


def make_the_winner(players_csv_file, first_three_community_cards, the_winner):

    """
    function make_the_winner finds the two cards needed for a given player to become the winner
    ASSUMES THERE HAS BEEN A CHECK FOR GAME ALREADY BEING WON BY ANOTHER PLAYER
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

    # remove community cards from card pools 
    for card in first_three_community_cards:
        card_pool.remove(card)
    
    # ASSUMES THERE HAS BEEN A CHECK FOR GAME ALREADY BEING WON BY ANOTHER PLAYER
    # (that no one already has a Spade Royal Flush)
    # assumes there is a chance for us to win

    # base combinations of hand cards and community cards
    base_combos = [winner_cards + first_three_community_cards]
    for card in first_three_community_cards:
        base_combos.append(winner_cards + [card])
        base_combos.append(winner_cards + [x for x in first_three_community_cards if x != card])

    

   

        

    return


def main():
    print("Hello Code Reviewer!")
    
    # change params here
    player_csv_file = 'tests\\test1.csv'
    first_three_community_cards = ['S10', 'Da', 'Cj']
    the_winner = "David"
    
    make_the_winner(player_csv_file, first_three_community_cards, the_winner)

    return
    

if __name__ == "__main__":
    main()


