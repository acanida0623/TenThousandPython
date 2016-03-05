import random
import time

players_container ={}
score_board = {'player1':0,
               'player2':0,
               'player3':0,
               'player4':0,
               'player1tempscore':0,
               'player2tempscore':0,
               'player3tempscore':0,
               'player4tempscore':0}

current_dice_container =[1,2,3,4,5,6]
dice_held_container = [0,0,0,0,0,0]

current_turn = "player1"
rolls_left = 3
final_score = False
num_playing = 0



def calc_score_rolled():

    current_roll = []
    final_score_roll = []
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    possible_scores_rolled = {}
    # Check index on current dice hand and see if the dice held value was 0, if it's 0, it means the dice was rolled this hand

    # 0 = open to roll again  #2 = on hold from previous #1 = is used after player holds dice to pick a new score
    #ignore the 2s because they've already been scored
    for dice in range(6):

        if dice_held_container[dice] == 0:

            current_roll.append(current_dice_container[dice])

        if dice_held_container[dice] == 1:

            final_score_roll.append(current_dice_container[dice])

    print (final_score_roll)

    #Count the amounts of different dice we currently rolled
    if final_score == False:
        for x in range(len(current_roll)):
            if current_roll[x] == 1:
                count1 += 1
            elif current_roll[x] == 2:
                count2 += 1
            elif current_roll[x] == 3:
                count3 += 1
            elif current_roll[x] == 4:
                count4 += 1
            elif current_roll[x] == 5:
                count5 += 1
            else:
                count6 += 1
    else:
        for x in range(len(final_score_roll)):
            if final_score_roll[x] == 1:
                count1 += 1
            elif final_score_roll[x] == 2:
                count2 += 1
            elif final_score_roll[x] == 3:
                count3 += 1
            elif final_score_roll[x] == 4:
                count4 += 1
            elif final_score_roll[x] == 5:
                count5 += 1
            else:
                count6 += 1
    #Check combonations


        #six of all dice
    if count1 == 6:
        possible_scores_rolled['1x6'] = 4000
    if count2 == 6:
        possible_scores_rolled['2x6'] = 1000
    if count3 == 6:
        possible_scores_rolled['3x6'] = 1000
    if count4 == 6:
        possible_scores_rolled['4x6'] = 1000
    if count5 == 6:
        possible_scores_rolled['5x6'] = 1000
    if count6 == 6:
        possible_scores_rolled['6x6'] = 1000

        #Five of all dice
    if count1 == 5:
        possible_scores_rolled['1x5'] = 3000
    if count2 == 5:
        possible_scores_rolled['2x5'] = 600
    if count3 == 5:
        possible_scores_rolled['3x5'] = 900
    if count4 == 5:
        possible_scores_rolled['4x5'] = 1200
    if count5 == 5:
        possible_scores_rolled['5x5'] = 1500
    if count6 == 5:
        possible_scores_rolled['6x5'] = 1800

        #Four of all dice
    if count1 == 4:
        possible_scores_rolled['1x4'] = 2000
    if count2 == 4:
        possible_scores_rolled['2x4'] = 400
    if count3 == 4:
        possible_scores_rolled['3x4'] = 600
    if count4 == 4:
        possible_scores_rolled['4x4'] = 800
    if count5 == 4:
        possible_scores_rolled['5x4'] = 1000
    if count6 == 4:
        possible_scores_rolled['6x4'] = 1200

        #Three of all dice
    if count1 == 3:
        possible_scores_rolled['1x3'] = 1000
    if count2 == 3:
        possible_scores_rolled['2x3'] = 200
    if count3 == 3:
        possible_scores_rolled['3x3'] = 300
    if count4 == 3:
        possible_scores_rolled['4x3'] = 400
    if count5 == 3:
        possible_scores_rolled['5x3'] = 500
    if count6 == 3:
        possible_scores_rolled['6x3'] = 600



    if count1 ==1 and count2 == 1 and count3 == 1 and count4 == 1 and count5 == 1 and count6 ==1:
        possible_scores_rolled['straight'] = 1500


    if count1 == 2 and count2 == 2 and count3 == 2:
        possible_scores_rolled['3doubles123'] = 1000

    if count1 == 2 and  count2 == 2 and count4 == 2:
        possible_scores_rolled['3doubles124'] = 1000

    if count1 == 2 and count2 == 2 and count5 == 2:
        possible_scores_rolled['3doubles125'] = 1000

    if count1 == 2 and count2 == 2 and count6 == 2:
        possible_scores_rolled['3doubles126']

    #if count1 == 2 and count2 == 2 and count1 == 2:
    #    possible_scores_rolled['3doubles121'] = 1000

    #if count1 == 2 and  count2 == 4:
    #    possible_scores_rolled['3doubles122'] = 1000


    #if count1 == 2 and count3 == 4:
    #    possible_scores_rolled['3doubles133'] = 1000

    if count1 == 2 and count3 == 2 and count4 ==2:
        possible_scores_rolled['3doubles134'] = 1000

    if count1 == 2 and count3 == 2 and count5 ==2:
        possible_scores_rolled['3doubles135'] = 1000

    if count1 == 2 and count3 == 2 and count6 ==2:
        possible_scores_rolled['3doubles136'] = 1000

    #if count1 == 2 and count4 == 4:
    #    possible_scores_rolled['3doubles144'] = 1000

    if count1 == 2 and count4 == 2 and count5 ==2:
        possible_scores_rolled['3doubles145'] = 1000

    if count1 == 2 and count4 == 2 and count6 ==2:
        possible_scores_rolled['3doubles146'] = 1000

    #if count1 == 2 and count5 == 4:
    #    possible_scores_rolled['3doubles155'] = 1000

    #if count1 == 2 and count6 == 4:
    #    possible_scores_rolled['3doubles166'] = 1000

    #if count2 == 2 and count2 == 2 and count2 == 2:
    #    possible_scores_rolled['3doubles222'] = 1000

    #if count3 == 2 and count3 == 2 and count3 == 2:
    #    possible_scores_rolled['3doubles333'] = 1000


    #if count4 == 2 and count4 == 2 and count4 == 2:
    #    possible_scores_rolled['3doubles444'] = 1000

    #if count5 == 2 and count5 == 2 and count5 == 2:
    #    possible_scores_rolled['3doubles555'] = 1000

    #if count6 == 2 and count6 == 2 and count6 == 2:
    #    possible_scores_rolled['3doubles666'] = 1000

    #if count3 == 2 and count3 == 2 and count3 == 2:
    #    possible_scores_rolled['3doubles333'] = 1000

    #if count3 == 4 and count4 == 2:
    #    possible_scores_rolled['3doubles334'] = 1000


    #if count3 == 4 and count5 == 2:
    #    possible_scores_rolled['3doubles335'] = 1000

    #if count3 == 4 and count6 == 2:
    #    possible_scores_rolled['3doubles336'] = 1000

    #if count4 == 4 and count3 == 2:
    #    possible_scores_rolled['3doubles443'] = 1000

    #if count4 == 4 and count5 == 2:
    #    possible_scores_rolled['3doubles445'] = 1000


    #if count4 == 4 and count6 == 2:
    #    possible_scores_rolled['3doubles446'] = 1000

    #if count3 == 2 and count5 == 4:
    #    possible_scores_rolled['3doubles355'] = 1000

    #if count5 == 4 and count6 == 2:
    #    possible_scores_rolled['3doubles556'] = 1000

    #if count4 == 2 and count5 == 4:
    #    possible_scores_rolled['3doubles455'] = 1000

    #if count3 == 2 and count6 == 4:
    #    possible_scores_rolled['3doubles366'] = 1000

    #if count6 == 4 and count4 == 2:
    #    possible_scores_rolled['3doubles466'] = 1000


    #if count6 == 4 and count5 ==2:
    #    possible_scores_rolled['3doubles566'] = 1000


        #counting down 1s and 5s
        #
    if count1 == 5 and count5 == 1:
        possible_scores_rolled['1x5 + 5x1'] = 3050

    if count1 == 4 and count5 == 1:
        possible_scores_rolled['1x4 + 5x1'] = 2050

    if count1 == 3 and count5 ==1:
        possible_scores_rolled['1x3 + 5x1'] = 1050


    if count1 == 4 and count5 == 2:
        possible_scores_rolled['1x4 + 5x2'] = 2100

    if count1 == 3 and count5 ==2:
        possible_scores_rolled['1x3 + 5x2'] = 1100


    if count1 == 3 and count5 == 3:
        possible_scores_rolled['1x3 + 5x3'] = 1500


    if count1 == 2 and count5 == 4:
        possible_scores_rolled['1x2 + 5x4'] = 1200

    if count1 == 2 and count5 == 3:
        possible_scores_rolled['1x2 + 5x3'] = 700

    if count1 == 2 and count5 == 2:
        possible_scores_rolled['1x2 + 5x2'] = 300

    if count1 == 2 and count5 == 1:
        possible_scores_rolled['1x2 + 5x1'] = 250

    if count1 == 1 and count5 == 5:
        possible_scores_rolled['1x1 + 5x5'] = 1600

    if count1 == 1 and count5 == 4:
        possible_scores_rolled['1x2 + 5x4'] = 1200

    if count1 == 1 and count5 == 3:
        possible_scores_rolled['1x1 + 5x3'] = 600

    if count1 == 1 and count5 == 2:
        possible_scores_rolled['1x1 + 5x2'] = 200

    if count1 == 1 and count5 == 1:
        possible_scores_rolled['1x1 + 5x1'] = 150

    if count1 == 1:
        possible_scores_rolled['1'] = 100

    if count1 == 2:
        possible_scores_rolled['1x2'] = 200

    if count5 == 1:
        possible_scores_rolled['5'] = 50

    if count5 == 2:
        possible_scores_rolled['5x2'] = 100



        #three and threes


    if count1 == 3 and count2 == 3:
        possible_scores_rolled['1x3 + 2x3'] = 600

    if count1 == 3 and count3 == 3:
        possible_scores_rolled['1x3 + 3x3'] = 1300

    if count1 == 3 and count4 == 3:
        possible_scores_rolled['1x3 + 4x3'] = 1400

    if count1 == 3 and count6 == 3:
        possible_scores_rolled['1x3 + 6x3'] = 1600



    if count2 == 3 and count3 == 3:
        possible_scores_rolled['2x3 + 3x3'] = 500

    if count2 == 3 and count4 == 3:
        possible_scores_rolled['2x3 + 4x3'] = 600

    if count2 == 3 and count5 == 3:
        possible_scores_rolled['2x3 + 5x3'] = 700

    if count2 == 3 and count6 == 3:
        possible_scores_rolled['2x3 + 6x3'] = 800


    if count3 == 3 and count4 == 3:
        possible_scores_rolled['3x3 + 4x3'] = 700

    if count3 == 3 and count5 == 3:
        possible_scores_rolled['3x3 + 5x3'] = 800

    if count3 == 3 and count6 == 3:
        possible_scores_rolled['3x3 + 6x3'] = 900


    if count4 == 3 and count5 == 3:
        possible_scores_rolled['4x3 + 5x3'] = 900

    if count4 == 3 and count6 == 3:
        possible_scores_rolled['4x3 + 6x3'] = 1000

    if count5 == 3 and count6 == 3:
        possible_scores_rolled['5x3 + 6x3'] = 1100

        # 2's and 4

    if count1 == 2 and count2 == 4:
        possible_scores_rolled['1x2 + 2x4'] = 600

    if count1 == 2 and count3 == 4:
        possible_scores_rolled['1x2 + 3x4'] = 800

    if count1 == 2 and count4 == 4:
        possible_scores_rolled['1x2 + 4x4'] = 1000

    if count1 == 2 and count6 == 4:
        possible_scores_rolled['1x2 + 6x4'] = 1400


    if count2 == 4 and count5 == 2:
        possible_scores_rolled['2x4 + 5x2'] = 500

    if count3 == 4 and count5 == 2:
        possible_scores_rolled['3x4 + 5x2'] = 700

    if count4 == 4 and count5 == 2:
        possible_scores_rolled['4x4 + 5x2'] = 900

    if count6 == 4 and count5 == 2:
        possible_scores_rolled['6x4 + 5x2'] = 1300

        #2 and 3

    if count1 == 2 and count2 == 3:
        possible_scores_rolled['1x2 + 2x3'] = 400

    if count1 == 2 and count3 == 3:
        possible_scores_rolled['1x2 + 3x3'] = 500

    if count1 == 2 and count4 == 3:
        possible_scores_rolled['1x2 + 4x3'] = 600

    if count1 == 2 and count6 == 3:
        possible_scores_rolled['1x2 + 6x3'] = 800


    if count2 == 3 and count5 == 2:
        possible_scores_rolled['2x3 + 5x2'] = 300

    if count3 == 3 and count5 == 2:
        possible_scores_rolled['3x3 + 5x2'] = 400

    if count4 == 3 and count5 == 2:
        possible_scores_rolled['4x3 + 5x2'] = 500

    if count6 == 3 and count5 == 2:
        possible_scores_rolled['6x3 + 5x2'] = 700

        #1 and 5

    if count1 == 1 and count2 == 5:
        possible_scores_rolled['1x1 + 2x5'] = 700

    if count1 == 1 and count3 == 5:
        possible_scores_rolled['1x1 + 3x5'] = 1000

    if count1 == 1 and count4 == 5:
        possible_scores_rolled['1x1 + 4x5'] = 1300

    if count1 == 1 and count6 == 5:
        possible_scores_rolled['1x1 + 6x5'] = 1900


    if count2 == 5 and count5 == 1:
        possible_scores_rolled['2x5 + 5x1'] = 650

    if count3 == 5 and count5 == 1:
        possible_scores_rolled['3x5 + 5x1'] = 950

    if count4 == 5 and count5 == 1:
        possible_scores_rolled['4x5 + 5x1'] = 1250

    if count6 == 5 and count5 == 1:
        possible_scores_rolled['6x5 + 5x1'] = 1850



        #1 and 4

    if count1 == 1 and count2 == 4:
        possible_scores_rolled['1x1 + 2x4'] = 500

    if count1 == 1 and count3 == 4:
        possible_scores_rolled['1x1 + 3x4'] = 700

    if count1 == 1 and count4 == 4:
        possible_scores_rolled['1x1 + 4x4'] = 900

    if count1 == 1 and count6 == 4:
        possible_scores_rolled['1x1 + 6x4'] = 1100


    if count2 == 4 and count5 == 1:
        possible_scores_rolled['2x4 + 5x1'] = 450

    if count3 == 4 and count5 == 1:
        possible_scores_rolled['3x4 + 5x1'] = 650

    if count4 == 4 and count5 == 1:
        possible_scores_rolled['4x4 + 5x1'] = 850

    if count6 == 4 and count5 == 1:
        possible_scores_rolled['6x4 + 5x1'] = 1050

        #1 and 3

    if count1 == 1 and count2 == 3:
        possible_scores_rolled['1x1 + 2x3'] = 300

    if count1 == 1 and count3 == 3:
        possible_scores_rolled['1x1 + 3x3'] = 400

    if count1 == 1 and count4 == 3:
        possible_scores_rolled['1x1 + 4x3'] = 500

    if count1 == 1 and count6 == 3:
        possible_scores_rolled['1x1 + 6x3'] = 700


    if count2 == 3 and count5 == 1:
        possible_scores_rolled['2x3 + 5x1'] = 250

    if count3 == 3 and count5 == 1:
        possible_scores_rolled['3x3 + 5x1'] = 350

    if count4 == 3 and count5 == 1:
        possible_scores_rolled['4x3 + 5x1'] = 450

    if count6 == 3 and count5 == 1:
        possible_scores_rolled['6x3 + 5x1'] = 650

    return possible_scores_rolled

def create_roll():
    global rolls_left
    rolls_left -= 1
    not_rolled = 0

    for dice in range(6):
        if dice_held_container[dice] == 0:
            not_rolled += 1



    if not_rolled > 0:
        for dice in range(6):
            if dice_held_container[dice] == 0:
                current_dice_container[dice] = random.randint(1,6)
    else:
        for dice in range(6):
            current_dice_container[dice] = random.randint(1,6)
        reset_indices()


create_roll()
scores_possible = calc_score_rolled()

def initiate_players():
    global num_playing
    while True:
        try:
            number_playing = int(input("How many people will be playing? "))
        except:
            ValueError
            print ("Please pick a number between 1 and 4.")

            continue

        else:
            if number_playing > 0 and number_playing < 5:
                num_playing = number_playing
                return number_playing

            else:
                print ("Please pick a number between 1 and 4.")
                continue

def define_player_names(numberplaying):
    for x in range(numberplaying):
        playernumber = x + 1

        strings = "What is the name of {PLAYER}? ".format(PLAYER="player "+str(playernumber))

        #set names for player 1-4

        playername = input(strings).lower()

        playerposition = "player"+str(playernumber)

        #add all the players and their names to the players dictionary
        players_container.update({playerposition: playername})

        #players[playerposition] = playername


def reset_board():
    currentplayer = ""
    #Check who's turn it is and print the player's name
    if current_turn == 'player1':
        currentplayer = players_container['player1'].title()
    elif current_turn == 'player2':
        currentplayer = players_container['player2'].title()
    elif current_turn == 'player3':
        currentplayer = players_container['player3'].title()
    else:
        currentplayer = players_container['player4'].title()

    print()
    print()
    print("⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹")
    print()
    print("{player}'s current dice.... ".format(player=currentplayer))
    print()
    print("⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹")

    for dice in range(6):

        #check if dice are held in player's hand, 1 means held to check score, 0 means not held

        dice_number = dice + 1

        if dice_held_container[dice] == 0:

            print ()
            print("DICE NUMBER {num} :  {roll}".format(num=dice_number,roll=current_dice_container[dice]))
            print ()

        elif dice_held_container[dice] == 2:

            print ()
            print("HELD FROM LAST ROLL. CAN'T BE ROLLED AGAIN: {roll}".format(num=dice_number,roll=current_dice_container[dice]))
            print ()


        else:
            print()
            print("DICE NUMBER {num} IS BEING HELD :  {roll}".format(num=dice_number,roll=current_dice_container[dice]))
            print()
    print (bool(scores_possible))

def change_turn():
    global current_turn
    global rolls_left
    rolls_left = 3
    if current_turn == "player1" and num_playing > 1:
        score_board['player1tempscore'] = 0
        current_turn = "player2"

    elif current_turn == "player2" and num_playing > 2:
        score_board['player2tempscore'] = 0
        current_turn = "player3"

    elif current_turn == "player3" and num_playing > 3:
        score_board['player3tempscore'] = 0
        current_turn = "player4"

    elif current_turn == "player4":
        score_board['player4tempscore'] = 0
        current_turn = "player1"


def check_if_scored():
    #Check if the player scored on their roll, if not, set current turn to next player and return false
    global current_turn
    if bool(scores_possible) == False:
        if current_turn == "player1" and num_playing > 1:
            score_board['player1tempscore'] = 0
            current_turn = "player2"
            print()
            print("You did not score anything. It's player 2's turn. ")
            print()
            return False
        elif current_turn == "player2" and num_playing > 2:
            score_board['player2tempscore'] = 0
            current_turn = "player3"
            print()
            print("You did not score anything. It's player 3's turn. ")
            print()
            return False
        elif current_turn == "player3" and num_playing > 3:
            score_board['player3tempscore'] = 0
            current_turn = "player4"
            print()
            print("You did not score anything. It's player 4's turn. ")
            print()
            return False
        elif current_turn == "player4":
            score_board['player4tempscore'] = 0
            current_turn = "player1"
            print()
            print("You did not score anything. It's player 1's turn. ")
            print()
            return False
        else:
            print()
            print("You didn't roll anything, try again! ")
            print()
            return False
    else:
        return True


def hold_dice():
    global scores_possible
    global rolls_left
    global final_score
    holding = True
    hold_index = 0
    reset_board()
    dice_held = False
    if check_if_scored() == True:
        while holding:
            hold_input = str(input("What number die would you like to hold? Please type in (1 - 6) to hold a die for next turn. Or '(R)oll' the leftover dice. "))

            if hold_input == '1':

                if dice_held_container[0] == 0:
                    dice_held_container[0] = 1
                    reset_board()
                    continue
                elif dice_held_container[0] == 2:
                    print()
                    print("Sorry you cannot change that die. ")
                    print()
                    continue
                else:
                    dice_held_container[0] = 0
                    reset_board()
                    continue

            elif hold_input == '2':
                if dice_held_container[1] == 0:
                    dice_held_container[1] = 1

                    reset_board()
                    continue

                elif dice_held_container[1] == 2:
                    print()
                    print("Sorry you cannot change that die. ")
                    print()
                    continue
                else:
                    dice_held_container[1] = 0
                    reset_board()
                    continue

            elif hold_input == '3':
                if dice_held_container[2] == 0:
                    dice_held_container[2] = 1
                    reset_board()
                    continue
                elif dice_held_container[2] == 2:
                    print()
                    print("Sorry you cannot change that die. ")
                    print()
                    continue
                else:
                    dice_held_container[2] = 0
                    reset_board()
                    continue
            elif hold_input == '4':
                if dice_held_container[3] == 0:
                    dice_held_container[3] = 1

                    reset_board()
                    continue

                elif dice_held_container[3] == 2:
                    print()
                    print("Sorry you cannot change that die. ")
                    print()
                    continue

                else:
                    dice_held_container[3] = 0
                    reset_board()
                    continue

            elif hold_input == '5':
                if dice_held_container[4] == 0:
                    dice_held_container[4] = 1

                    reset_board()
                    continue

                elif dice_held_container[4] == 2:
                    print()
                    print("Sorry you cannot change that die. ")
                    print()
                    continue

                else:
                    dice_held_container[4] = 0

                    reset_board()
                    continue

            elif hold_input == '6':
                if dice_held_container[5] == 0:
                    dice_held_container[5] = 1

                    reset_board()
                    continue

                elif dice_held_container[5] == 2:
                    print()
                    print("Sorry you cannot change that die. ")
                    print()
                    continue
                else:
                    dice_held_container[5] = 0

                    reset_board()
                    continue

            elif str(hold_input).lower() == "r" or str(hold_input).lower() == "roll":
                roll_next()
                break

            elif str(hold_input).lower() == "done" or str(hold_input).lower() == "d":
                global final_score

                finish_turn()

                break
    else:
        rolls_left = 3
        reset_indices()
        create_roll()
        final_score = False
        scores_possible = calc_score_rolled()
        hold_dice()


def reset_indices():
    for dice in range(6):
        dice_held_container[dice] = 0

def update_hold_indices():
    for dice in range(6):
        if dice_held_container[dice] == 1:
            dice_held_container[dice] = 2



def roll_next():
    dice_roll = 0
    global scores_possible
    dice_held = 0

    #check to make sure they held any dice eg: if any indices are 1 if no ones then
    for dice in range(6):
        if dice_held_container[dice] == 1:
            update_temp_score()
            update_hold_indices()
            create_roll()

            scores_possible = calc_score_rolled()
            hold_dice()
            dice_roll += 1
            break

    if dice_roll == 0:
        print()
        print("You need to hold at least one dice each turn!")
        print()
        time.sleep(5)
        hold_dice()





def finish_turn():
    global scores_possible
    global final_score

    if rolls_left == 2:
        update_temp_score()
        update_score()
        change_turn()
        reset_indices()
        create_roll()

        scores_possible = calc_score_rolled()
        hold_dice()

    else:
        final_score = True
        update_score()
        final_score = False
        change_turn()
        reset_indices()
        create_roll()
        scores_possible = calc_score_rolled()
        hold_dice()



def update_temp_score():
    global final_score
    final_score = True
    temp_player = "{player}tempscore".format(player=current_turn)
    score = calc_score_rolled()
    final_score = False
    if score:
        highest_score_key = max(score, key=score.get)
        print (score,"scoreheldtest")
        print (highest_score_key)
        score_board[temp_player] += score[highest_score_key]
        print(score_board[temp_player],"tempscore")



def update_score():
    tempscore = "{player}tempscore".format(player=current_turn)
    if score_board[current_turn] < 1000:
        if score_board[tempscore] > 1000:
            score_board[current_turn] += score_board[tempscore]
            print (score_board)
        else:
            print()
            print("You need to score at least a thousand points to get on the board. ")
    else:
        score_board[current_turn] += score_board[tempscore]
        print (score_board)







define_player_names(initiate_players())
print (players_container)


print(scores_possible)
hold_dice()
