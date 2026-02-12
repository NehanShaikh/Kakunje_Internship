import random

# 1. Generate a random number between 1 and 6 (dice roll)
dice = random.randint(1, 6)

# 2. Print the dice result
print("Dice Result:", dice)

# 3. Create a list of cards
cards = ["Ace", "King", "Queen", "Jack"]

# 4. Shuffle the cards randomly
random.shuffle(cards)
print("Shuffled Cards:", cards)

# 5. Generate and print one random card from the shuffled list
random_card = random.choice(cards)
print("Random Card:", random_card)
