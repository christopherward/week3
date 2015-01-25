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
# - If computer score is between 17 and 20, winner is determined by score
# - If it's a tie, nobody wins.

# Grading:
# - 5 points for allowing a human user to play their complete hand
# - 5 points for allowing the computer to play its hand

# (Optional) Extras
# [You don't get extra credit for these, but they're fun.]
# - 1. Aces should count as 1 if counting as 11 would have made the score > 21
# - 2. Initally, human and dealer both get two cards; one dealer card is face up
# - 3. Allow the user to play as many games as they want
# - 4. Dealing cards to the computer should have a dramatic, 4-second delay

# Here's the psuedocode we wrote on the board in class:

## Get a deck of cards
import random
def gen_deck():
    suits = "\u2663 \u2665 \u2666 \u2660".split()
    values = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

    global deck
    deck = []
    for suit in suits:
        for face in values:
            deck.append(face+suit)

    random.shuffle(deck)

## Deal the first two cards to user
def deal_two(deck):
    playerhand.append(deck[0])
    playerhand.append(deck[1])
    dealerhand.append(deck[2])
    dealerhand.append(deck[3])
    deck.pop(0)
    deck.pop(0)
    deck.pop(0)
    deck.pop(0)
    print("\nYour cards: ", playerhand[0], playerhand[1])
    print("\nThe dealer's cards: XX",dealerhand[1])

def deal_one_player(deck):
    playerhand.append(deck[0])
    deck.pop(0)

def deal_one_dealer(deck):
    dealerhand.append(deck[0])
    deck.pop(0)

def count_cards(hand):
    total = 0
    for card in hand:
        if card[0] == 'A':
            total += 11
        elif card[0] in ['J','Q','K'] or card[0:2] == '10':
            total += 10
        else:
            total += int(card[0])
    return total

## User can choose to take cards as long as score < 21
def play():
    gen_deck()
    global playerhand
    global dealerhand
    global player_sum
    global dealer_sum
    playerhand = []
    dealerhand = []
    player_sum = 0
    dealer_sum = 0

    deal_two(deck)

    another_card = ""
    another_game = 'y'
    while another_game.lower() != 'n':
        while another_card.lower() != "n" and count_cards(playerhand) <= 21:
            another_card = input("\nWould you like another card? (y/n) ")
            if another_card.lower() == 'y':
                deal_one_player(deck)
                print("\nYour cards: ", end="")
                for i in playerhand:
                    print(i + " ", end="")
                print("\nYour total:", count_cards(playerhand))

        if count_cards(playerhand) > 21:
            print("\nYou went over. Dealer wins.")
        elif count_cards(dealerhand) < 17:
            while count_cards(dealerhand) < 17:
                deal_one_dealer(deck)
                
        print("\nDealer's cards: ", end="")
        for i in dealerhand:
            print(i + " ", end="")
        print("\nDealer's total:", count_cards(dealerhand))
        if count_cards(dealerhand) == 21:
            print("\nDealer wins.")
        elif count_cards(dealerhand) > 21:
            print("\nDealer went over. You win.")
        elif count_cards(dealerhand) >= 17 and count_cards(dealerhand) <= 20:
            if count_cards(playerhand) > count_cards(dealerhand):
                print("\nYou win.")
            elif count_cards(playerhand) < count_cards(dealerhand):
                print("\nDealer wins.")
            elif count_cards(playerhand) == count_cards(dealerhand):
                print("\nIt's a tie!")
        another_game = input("\nWould you like to play again? (y/n) ")
        if another_game.lower() == 'y':
            play()
play()
                

## If user goes over 21, game is over.

## If user reaches 21, game is over.

## If user stands with less than 21, then it's the dealer's turn:

##    Computer takes two cards
##    Computer must take more cards while computer score < 17
##    If computer score reached 21, computer wins.
##    If computer score goes over 21, computer loses.
##    If computer score is 17 to 20, winner is determined by higher score.
