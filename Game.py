from time import sleep
from os import system
from Players import Player
from Hands import Hand
from Decks import Deck

players_list = []
deck = Deck()
dealer_hand = Hand()
dealer = Player('The dealer', [dealer_hand])

system('cls')
print('''
#######    #              #       ##########  #     #    ##########       #       ##########  #     #
#      #   #             # #      #           #    #              #      # #      #           #    #
#       #  #             # #      #           #   #               #      # #      #           #   #
#       #  #            #   #     #           #  #                #     #   #     #           #  #
#      #   #            #   #     #           # #                 #     #   #     #           # #
#     #    #           #     #    #           ##                  #    #     #    #           ##
#      #   #           #######    #           ##                  #    #######    #           ##
#       #  #          #       #   #           # #         #       #   #       #   #           # #
#       #  #          #       #   #           #  #        #       #   #       #   #           #  #
#      #   #         #         #  #           #   #       #       #  #         #  #           #   #
#######    ########  #         #  ##########  #    #      #########  #         #  ##########  #    #
 
 ----------------------------------------------------------------------------------------------------
 ''')

def create_player(name):

    Player.player_count += 1
    players_list.append(Player(name, [Hand()]))
    return players_list

def start_game():

    print('''Welcome to Standard Blackjack. Each player starts with $100 in their wallets.
The payout for a blackjack is 3:2. The payout for a successful insurance is 2:1.
Blackjacks by the player are only won if the dealer also doesn\'s show a blackjack.
By deafult, the game is be played with 5 decks of 52 cards.''')
    sleep(2.5)

    number_of_players = int(input('\nHow many players are we dealing with? '))

    print()
    count = number_of_players
    while count:
        for number in range(1, number_of_players + 1):
            sleep(0.5)
            name = input(f'What is the name of player {number}? ')
            create_player(name)
            count -= 1

    print()
    for player in players_list:
        sleep(0.5)
        bet = input(f'How much does {player.name} want to bet? ')
        player.place_bet(bet, 0)

    sleep(1)
    print('\nNow that\'s out of the way, the dealer will deal cards for each player and for himself.')
    sleep(2)

    dealing()


def dealing(split = False, person = None, i = None):

    if split == False:
        for player in players_list:
            for i in range(len(player.hands)):
                player.hands[i].get_card(deck)
                player.hands[i].get_card(deck)

    elif split == True:
        person.hands[i].get_card(deck)
        person.hands[i + 1].get_card(deck)

    if split == False:
        if len(dealer.hands[0].hand) == 0:
            dealer.hands[0].get_card(deck)
            dealer.hands[0].get_card(deck, hide = True)

    if split == True:
        print_dealing(split = True, person = person, i = i)
    elif split == False:
        print_dealing()


def print_dealing(split = False, debug = True, person = None, i = None):

    # system('cls')
    if split == False:

        for player in players_list:
            print(f'\nDealing for {player.name}.\n')
            sleep(1)
            for card in player.hands[0].hand:
                print(f'{card.card}')
                sleep(0.5)
            if player.hands[0].blackjack == True:
                print(f'{player.name} got a blackjack!')

    elif split == True:

        print(f'\nDealing for {person.name}\'s new hands.')
        sleep(1)
        
        print(f'\nFor hand {i + 1}:')
        sleep(0.5)
        print(f'{person.hands[i].hand[-1].card}')

        sleep(1)

        print(f'\nFor hand {i + 2}:')
        sleep(0.5)
        print(f'{person.hands[i + 1].hand[-1].card}')

    if split == False:

        print('\nDealing for the dealer.\n')
        sleep(0.5)
        for card in dealer.hands[0].hand:
            if card.hidden == False:
                sleep(0.5)
                print(f'{card.card}')
            if card.hidden == True:
                sleep(0.5)
                print('Hidden card')

    if debug == True:

        sleep(1)
        print()
        for player in players_list:
            for hand in player.hands:
                print(f'{player.name} hand', hand)
                for card in hand.hand:
                    print(card.card)
        
        for hand in dealer.hands:
            print(f'dealer hand', hand)
            for card in hand.hand:
                print(card.card)

    if split == False:
        sleep(1)
        print('\nNow that cards are dealt, the game will begin.')
        sleep(2)
    
    if split == False:
        first_turn()
    elif split == True:
        take_turn(person)


def print_hit(player, i, hand):

    description = f'\n{player.name} got a {player.hands[i].hand[-1].card}'

    if player.name != 'The dealer':
        description +=  f' on hand {player.hands.index(hand) + 1}.'
    else:
        description += '.'

    if player.hands[i].value == 21:
        description += '\nScored 21!'

    sleep(0.5)
    print(description)
    sleep(1)


def first_turn():

    for player in players_list:
        if player.hands[0].blackjack == True:
            pass
        else:
            take_turn(player)

    dealers_turn()


def take_turn(player):

    for hand in player.hands:
        if hand.played == False:
            # system('cls')
            i = player.hands.index(hand)
            print(f'\nWhat does {player.name} want to do with hand {player.hands.index(hand) + 1}?')
            sleep(0.5)
            print('1) Hit')
            sleep(0.1)
            print('2) Stay')
            sleep(0.1)
            if hand.first_choice == True:
                print('3) Double down')
                sleep(0.1)
                print('4) Split (not implemented)')
                sleep(0.1)
                print('5) Surrender')
                sleep(0.1)

            print('\nYou have the following cards in this hand:')
            for card in player.hands[i].hand:
                sleep(0.1)
                print(card.card)
            print(f'Totalling {hand.value} points.')

            opt = input('\n')
            if opt == '1':

                hand.get_card(deck)
                hand.first_choice = False

                if hand.bust == True:
                    print_hit(player, i, hand)
                    print('This hand is bust!')
                    sleep(1)
                    hand.played = True
                elif hand.value == 21:
                    print_hit(player, i, hand)
                    hand.played = True
                else:
                    print_hit(player, i, hand)
                    take_turn(player)

            elif opt == '2':

                sleep(0.5)
                print(f'\n{player.name} stays with hand {player.hands.index(hand) + 1} with {player.hands[i].value} points.')
                hand.played = True
                sleep(1)
                # system('cls')

            elif opt == '3' and hand.first_choice == True:

                sleep(0.5)
                temp = hand.bet
                player.double_down(hand)
                print(f'\n{player.name} doubled their bet from ${temp} to ${hand.bet}.')
                hand.get_card(deck)

                if hand.bust == True:
                    print_hit(player, i, hand)
                    print('This hand is bust!')
                    sleep(1)
                    hand.played = True
                elif hand.value == 21:
                    print_hit(player, i, hand)
                    hand.played = True
                else:
                    print_hit(player, i, hand)
                    hand.played = True

            elif opt == '4' and hand.first_choice == True:
                
                if hand.split_possible == True:
                    sleep(0.5)
                    print(f'\n{player.name} chose to split hand {player.hands.index(hand) + 1}. Their bet of ${hand.bet} will be mirrored onto the new hand.')
                    sleep(1)

                    player.split(hand)
                    i = player.hands.index(hand) + 1
                    bet = hand.bet
                    player.place_bet(bet , i)

                    dealing(split = True, person = player, i = player.hands.index(hand))

                else:
                    sleep(0.5)
                    print(f'\nThis can\'t be split. Only hands with two cards of the same value can be split.')
                    sleep(1)

            elif opt == '5' and hand.first_choice == True:
                
                player.sur(hand)

                sleep(0.5)
                print(f'{player.name} chose to surrender this hand.')
                hand.played = True
                sleep(1)

            else:
                print('\nI\'s sorry, I didn\'t understand that. Say again?')
                take_turn(player)


def dealers_turn():

    sleep(1)
    print(f'\nIt\'s the dealer\'s turn now.')
    sleep(1)
    print(f'\n{dealer.name}\'s hidden card is a {dealer.hands[0].hand[-1].card}.')

    if dealer.hands[0].blackjack == True:
        sleep(0.5)
        print(f'{dealer.name} has a blackjack!')

    hands_number = 0
    bust_hands = 0
    for player in players_list:
        for hand in player.hands:
            hands_number += 1
            if hand.bust == True:
                bust_hands += 1

    blackjack_number = 0
    for player in players_list:
        for hand in player.hands:
            if hand.blackjack == True:
                blackjack_number += 1

    if bust_hands == hands_number:
        print_end_turn(players_bust = True)

    elif blackjack_number == hands_number:
        if dealer.hands[0].blackjack == True:
            print_end_turn(players_blackjack = True, dealer_blackjack = True)
    
    elif dealer.hands[0].blackjack == True:
        print_end_turn(dealer_blackjack = True)

    else:
        totals = []
        for player in players_list:
            for hand in player.hands:
                if hand.value <= 21:
                    totals.append(hand.value)
        goal = max(totals)
        sleep(0.5)
        print(f'They will aim for {goal} points.\n')
        if dealer.hands[0].blackjack != True:
            while dealer.hands[0].value < goal:
                dealer.hands[0].get_card(deck)
                print_hit(dealer, 0, dealer.hands[0])
                if dealer.hands[0].value < goal:
                    print(f'Totalling {dealer.hands[0].value} so far.')
                else:
                    print(f'Stopping at {dealer.hands[0].value}.')
                    sleep(1)
        print_end_turn()


def end_turn(players_bust = False, players_blackjack = False, dealer_blackjack = False, dealer_bust = True):

    if players_blackjack == True and dealer_blackjack == True:
        for player in players_list:
            for hand in player.hands:
                player.wallet += hand.bet

    elif dealer_blackjack == True:
        for player in players_list:
            for hand in player.hands:
                if hand.blackjack == True:
                    player.wallet += hand.bet
    
    elif dealer_bust == True:
        for player in players_list:
            for hand in player.hands:
                if hand.bust == False:
                    player.wallet += hand.bet * 2

    else:
        for player in players_list:
            for hand in player.hands:
                if dealer.hands[0].value == hand.value:
                    player.wallet += hand.bet
                elif dealer.hands[0].value < hand.value:
                    if hand.blackjack:
                        player.wallet += hand.bet * 2.5
                    else:
                        player.wallet += hand.bet * 2

    sleep(3)
    interim()


def print_end_turn(players_bust = False, players_blackjack = False, dealer_blackjack = False):

    print('\nEnd of turn. Calculating and displaying the results...\n')
    sleep(2)

    if players_bust == True:

        sleep(0.5)
        print('All player\'s hands are bust!')
        for player in players_list:
            for hand in player.hands:
                sleep(0.5)
                print(f'{player.name} lost their bet of ${hand.bet} for hand {player.hands.index(hand) + 1}.')
        
        end_turn(players_bust = True)

    elif players_blackjack == True and dealer_blackjack == True:

        sleep(0.5)
        print('It\'s a push between all hands and the dealer, since everyone has a blackjack.')
        
        end_turn(players_blackjack = True, dealer_blackjack = True)
    
    elif dealer_blackjack == True:

        for player in players_list:
            for hand in player.hands:
                if hand.surrended == True:
                    sleep(0.5)
                    print(f'{player.name} chose to surrender this hand. They lose half of their original bet.')
                elif hand.blackjack == True:
                    sleep(0.5)
                    print(f'It\'s a push between the dealer and {player.name} for their hand {player.hands.index(hand) + 1}.')
                else:
                    sleep(0.5)
                    print(f'{player.name}\'s hand {player.hands.index(hand) + 1} lost their bet of {hand.bet} to the dealer\'s blackjack.')
        
        end_turn(dealer_blackjack = True)
    
    elif dealer.hands[0].bust == True:

        sleep(0.5)
        print(f'{dealer.name} is bust!')
        for player in players_list:
            for hand in player.hands:
                if hand.surrended == True:
                    sleep(0.5)
                    print(f'{player.name} chose to surrender this hand. They lose half of their original {hand.bet * 2} bet.')
                elif hand.bust == False:
                    sleep(0.5)
                    print(f'{player.name}\'s hand {player.hands.index(hand) + 1} won ${hand.bet} over the dealer\'s hand.')
                elif hand.bust == True:
                    sleep(0.5)
                    print(f'{player.name}\'s hand {player.hands.index(hand) + 1} is bust! They lose their ${hand.bet}.')
        
        sleep(1)
        end_turn(dealer_bust = True)

    else:

        for player in players_list:
            for hand in player.hands:
                if hand.surrended == True:
                    sleep(0.5)
                    print(f'{player.name} chose to surrender this hand. They lose half of their original {hand.bet * 2} bet.')
                elif hand.blackjack == True:
                    sleep(0.5)
                    print(f'{player.name}\'s hand {player.hands.index(hand) + 1} won ${hand.bet * 1.5} over the dealer with a blackjack.')
                elif hand.bust == True:
                    sleep(0.5)
                    print(f'{player.name}\'s hand {player.hands.index(hand) + 1} is bust! They lose their ${hand.bet}.')
                elif hand.bust == True:
                    sleep(0.5)
                    print(f'{player.name}\'s hand {player.hands.index(hand) + 1} is bust and lost its bet of ${hand.bet}.')
                elif dealer.hands[0].value > hand.value:
                    sleep(0.5)
                    print(f'{player.name}\'s hand {player.hands.index(hand) + 1} lost its bet of ${hand.bet} to the dealer.')
                elif dealer.hands[0].value == hand.value:
                    sleep(0.5)
                    print(f'{player.name}\'s hand {player.hands.index(hand) + 1} tied with the dealer.')
                elif dealer.hands[0].value < hand.value:
                    sleep(0.5)
                    print(f'{player.name}\'s hand {player.hands.index(hand) + 1} won ${hand.bet} over the dealer\'s hand.')
        end_turn()


def interim():
    
    for player in players_list:
        while len(player.hands) > 1:
            player.hands.pop()
        for hand in player.hands:
            hand.renew_hand()

    dealer_hand.renew_hand()

    new_turn()


def new_turn():

    print('\nNew turn.')
    sleep(0.5)
    for player in players_list:
        sleep(0.5)
        print(f'\n{player.name} is starting the turn with ${player.wallet} in their wallet.')
        sleep(1)
        bet = input(f'How much does {player.name} want to bet? ')
        player.place_bet(bet, 0)
    
    dealing()


start_game()