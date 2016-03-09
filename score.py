import random

def calc_score_rolled(final_score,dice_held_container,current_dice_container):

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

def create_roll(dice_held,dice_container):

    not_rolled = 0


    #if any dice are 0 they need to be rolled before rolling all the dice
    for dice in range(6):
        if dice_held[dice] == 0:
            not_rolled += 1


    #checks if dice =0  roll dice, if
    if not_rolled > 0:
        for dice in range(6):
            if dice_held[dice] == 0:
                dice_container[dice] = random.randint(1,6)
    else: #All the dice have been rolled and scored, roll all the dice again
        for dice in range(6):
            dice_container[dice] = random.randint(1,6)
        for dice in range(6):
            dice_held[dice] = 0

    return(dice_held,dice_container)



def reset_indices(dice_held_container):
    for dice in range(6):
        dice_held_container[dice] = 0
    return dice_held_container


def update_temp_score(score_board,final,current_turn,dice_held_container,current_dice_container):

    temp_player = "{player}tempscore".format(player=current_turn)
    #false parameter means its not the final score so we need all possible scores
    score = calc_score_rolled(final,dice_held_container,current_dice_container)

    if score:
        highest_score_key = max(score, key=score.get)
        print(highest_score_key,"highest_score")
        score_board[temp_player] += score[highest_score_key]
    return score_board





def update_score(score_board,current_turn):
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
    return score_board
