############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import time
from art import logo
from replit import clear

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    index = cards.index(11)
    cards[index] = 1
  return sum(cards)

def compare(user_total, dealer_total):
  if user_total == 0:
    return "You win with a blackjack!"
  elif dealer_total == 0:
    return "Dealer wins with a blackjack!"
  elif user_total > 21:
    return "You went over. You lose."
  elif dealer_total > 21:
    return "Dealer went over. You win!"
  elif user_total == dealer_total:
    return "It's a draw!"
  elif user_total > dealer_total:
    return "You win!"
  else:
    return "Dealer wins!"

def start_game():
  """Starts a new game of blackjack."""
  print(logo)
  user_cards = []
  dealer_cards = []
  is_game_over = False
  didDealerDraw = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())

  user_total = calculate_score(user_cards)
  dealer_total = calculate_score(dealer_cards)

  print(f"Your cards: {user_cards}, current score: {user_total}")
  print(f"Dealer's first card: {dealer_cards[0]}")
  
  if user_total == 0 or dealer_total == 0 or user_total > 21:
    is_game_over = True
  
  while not is_game_over:
    user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_choice == "y":
      user_cards.append(deal_card())
      user_total = calculate_score(user_cards)
      
      print(f"\nYour cards: {user_cards}, current score: {user_total}")
      print(f"Dealer's first card: {dealer_cards[0]}")
      
      if user_total > 21:
        is_game_over = True
        break     
        
    else:
      is_game_over = True
      break

  while dealer_total != 0 and dealer_total < 17:
    dealer_cards.append(deal_card())
    dealer_total = calculate_score(dealer_cards)
    didDealerDraw = True

  if is_game_over:
    if didDealerDraw:
      print("\nDealer is drawing cards...")
      time.sleep(3)
      
    print(f"\nYour final hand: {user_cards}, final score: {user_total}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_total}\n")
    print(compare(user_total, dealer_total))

  while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    start_game()

  return print("\nThanks for playing the Blackjack Game!")

start_game()
  

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

