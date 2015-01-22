# Game of Blackjack

# Simplified Rules (10 pts possible):
# - Human player gets the first two cards
# - Human player plays the rest of their hand
# - Then computer gets next two cards
# - Computer must take cards score  >= 17
# - Computer must stand when score >= 17
# - Aces always count as 11
# - Human player loses if their score is > 21
# - Computer loses if computer score is > 21
# - Human player wins immediately if their score is exactly 21
# - Computer wins immediately if their score is exactly 21
# - If computer score is betwen 17 and 20, winner is determined by score
# - If it's a tie, nobody wins.

# Grading:
# - 5 points for allowing a human user to play their complete hand
# - 5 points for allowing the computer to play its hand

# (Optional) Extras
# [You don't get extra credit for these, but they're fun.]
# - 1. Aces should count as 1 if counting as 11 would have made the score > 21
# - 2. Initally, human and dealer both get two cards; one dealer card is face up
# - 3. Allow the user to play as many games as they want
# - 4. Dealing cards to the cmputer should have a dramatic, 4-second delay

# Here's the psuedocode we wrote on the board in class:

## Get a deck of cards

## Shuffle the deck

## Deal the first two cards to user

## User can choose to take cards as long as score < 21

## If user goes over 21, game is over.

## If user reaches 21, game is over.

## If user stands with less than 21, then it's the dealer's turn:

##    Computer takes two cards
##    Computer must take more cards while computer score < 17
##    If computer score reached 21, computer wins.
##    If computer score goes over 21, computer loses.
##    If computer score is 17 to 20, winner is determined by higher score.
