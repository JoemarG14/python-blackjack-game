## Blackjack Game 🂡👑
Blackjack is a card game that pits the player against the dealer. This Python project replicates and implements the rules of the game.

# Instructions

The objective is to deal both user and computer a starting hand of 2 random card values. The game will only show the 2 cards on hand of the user, and will only show 1 card from the computer's hand. 
Then, the game will detect if the computer or user has a blackjack on the first 2 cards provided (ACE + FACE CARDS). 
If no blackjack on first cards, the computer will ask the user if they want to get another card or to pass.
```
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           

Your cards: [10, 11], current score: 0
Dealer's first card: 6

Dealer is drawing cards...

Your final hand: [10, 11], final score: 0
Dealer's final hand: [6, 10, 4], final score: 20

You win with a blackjack!
```

```

.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           

Your cards: [10, 9], current score: 19
Dealer's first card: 10
Type 'y' to get another card, type 'n' to pass: 
```

If the user decided to pass, the dealer will draw a card if their cards are below 17 or will just show the cards if it is greater than 17.
```
Dealer is drawing cards...

Your final hand: [3, 8], final score: 11
Dealer's final hand: [3, 8, 4, 4], final score: 19

Dealer wins!
```
```
Your final hand: [10, 9], final score: 19
Dealer's final hand: [10, 10], final score: 20

Dealer wins!
```

If the user decided to get another card, the new card will then be added to the 2 cards the user already have. This can be done multiple times until the user is satisfied with the total number they have. 
However, keep in mind that if the user's total number exceeds 21, they will automatically lose the round.
```
Type 'y' to get another card, type 'n' to pass: y

Your cards: [6, 6, 4], current score: 16
Dealer's first card: 11
Type 'y' to get another card, type 'n' to pass: y

Your cards: [6, 6, 4, 9], current score: 25
Dealer's first card: 11

Your final hand: [6, 6, 4, 9], final score: 25
Dealer's final hand: [11, 8], final score: 19

You went over. You lose.
```
```
Type 'y' to get another card, type 'n' to pass: n

Dealer is drawing cards...

Your final hand: [10, 10], final score: 20
Dealer's final hand: [4, 10, 5], final score: 19

You win!
```

> [!NOTE]  
> The deck is unlimited in size. 
> There are no jokers. 
> The Jack/Queen/King all count as 10.
> The the Ace can count as 11 or 1.
> The cards in the list have equal probability of being drawn.
> Cards are not removed from the deck as they are drawn.
