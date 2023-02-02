import random
# def game_play():
#     # Create a deck of cards
#     suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
#     ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
#     deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

#     # Shuffle the deck
#     random.shuffle(deck)
#     while True :
#     # Draw a card from the deck
#         if len(deck) <= 4 :
#             print("Refill deck")
#             deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
        
#         player_draw = [deck.pop() for _ in range(2)]

#         dealer_draw = [deck.pop() for _ in range(2)]
#         draw_more = input("Draw more ?")
#         extra_draw = deck.pop()



