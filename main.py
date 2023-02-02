from card import *
import random
'''
Art card idea from https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards


'''
test_card_1 = Card('Diamonds', '4')
test_card_2 = Card('Clubs', 'Ace')
test_card_3 = Card('Spades', 'Jack')
test_card_4 = Card('Hearts', '10')

print(ascii_version_of_card(test_card_1, test_card_2, test_card_3, test_card_4))
print(ascii_version_of_hidden_card(test_card_1, test_card_2, test_card_3, test_card_4))
# welcome 
play = True
while play :
    welcome = input("\nWelcome to Casio, We have a BlackJack game for you do you wanna play.\nType 'Y' for yes , Type 'N' for No.\n").upper()


    # Bet
    money = 10000
    if welcome == 'Y' :
        while True:
            bet = (input(f"You have {money}$ how much you gonna bet.\n"))
            if bet.isalpha() :
                print("please type a number.\n")
                continue
            elif bet.isdigit and int(bet) < money :
                break
            elif bet.isdigit and int(bet) > money:
                print(f"\nYour bet is over your balance.")
                continue

    # create deck + random card output + no duplicate
    # ask for more card or not
    # reveal card and result
        game_play_(money , bet)

    elif welcome == 'N':
        play = False
    
    else :
        print("Please type 'Y' or 'N'. ")
# play agian
