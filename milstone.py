# problem is --->>>  The game of lucky cards.

# We know that a standard deck of 52 cards is grouped into four suites Club, Diamond, Heart, and
# Spade, each containing 13 cards:
# Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, and King. Some of these cards are considered lucky. Our
# task is to read a card as input and output if the card is lucky or not.
# The predefined set of lucky cards is as follows:
# ● Ace of Spade
# ● Any Heart
# ● Queen of Diamond
# ● King of Diamond
# ● Any 7
# The corresponding program will have a list of conditions separated by or. Each condition can then
# take
# care of one category of lucky cards. A sample run of such a program can be as follows.
# Enter your card: 7 of Heart
# Lucky you!
# Enter your card: Queen of Spade
# Better luck next time.
# Enter your card: 8 of Spade
# Better luck next time.
# Enter your card: Ace of Spade
# Lucky you!

# ---->>>>> here i am writting code for this problem
# Define a function to check if a card is lucky
def is_lucky(card):
    # Define a set of conditions for lucky cards
    
    # If the card is "Ace of Spade", it's lucky
    # If the card is "Queen of Diamond", it's lucky
    # If the card is "King of Diamond", it's lucky
    # If the card starts with "7 of", it's lucky
    lucky_conditions = [
        "Ace of Spade",
        "Queen of Diamond",
        "King of Diamond",
        "7 of",
    ]

    # Check if the card matches any of the lucky conditions
    for condition in lucky_conditions:
        if condition in card:
            return True  # If it matches any condition, it's a lucky card

    # Check if it's a Heart card (any Heart is lucky)
    if " of Heart" in card:
        return True  # If it's any Heart card, it's lucky

    # If none of the conditions are met, it's not a lucky card
    return False

# Get the user's input for a card
user_card = input("Enter your card: ")

# Check if the card is lucky and provide a message accordingly
if is_lucky(user_card):
    print("Lucky you!")  # If it's a lucky card, you're lucky!
else:
    print("Better luck next time.")  # If it's not a lucky card, better luck next time.