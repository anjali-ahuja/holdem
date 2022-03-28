# Holdem: What cards do you need to win?

This is a python script that outputs the two cards you need to win given the first three community and everyone's hand.

There are three main components to this:

1. Ingesting and organising the card data, setting up the game
2. Detecting flushes, straights, four-pairs to create a scoring function
3. Applying the scoring function to all players for all possible combinations
