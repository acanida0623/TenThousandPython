
import time
import display
import score



def main():

    score_board = {'player1':0,
                   'player2':0,
                   'player3':0,
                   'player4':0,
                   'player1tempscore':1000,
                   'player2tempscore':0,
                   'player3tempscore':0,
                   'player4tempscore':0}


    current_dice_container =[1,2,3,4,5,6]
    dice_held_container = [0,0,0,0,0,0]
    current_turn = "player1"
    rolls_left = 3
    final_score = False
    players_container = display.define_player_names(display.initiate_players())
    print(players_container)
    num_playing = len(players_container)
    while True:
        #Create a random roll for the dice
        (dice_held_container,current_dice_container) = score.create_roll(dice_held_container,current_dice_container)
        #Calculate the scores possible for the roll
        scores_possible = score.calc_score_rolled(False,dice_held_container,current_dice_container)
        #give the display information it needs to reset the playing board
        display.reset_board(current_turn,players_container,dice_held_container,current_dice_container,scores_possible,score_board)
        #Make sure the player scored on their roll
        if bool(scores_possible):
            while True:
                display.list_commands()
                hold_input = str(input("Please enter an input... "))

                if hold_input == '1':

                    if dice_held_container[0] == 0:
                        dice_held_container[0] = 1
                        display.reset_board(current_turn,players_container,dice_held_container,current_dice_container,scores_possible,score_board)
                        continue
                    elif dice_held_container[0] == 2:
                        print()
                        print("Sorry you cannot change that die. ")
                        print()
                        continue
                    else:
                        dice_held_container[0] = 0
                        display.reset_board(current_turn,players_container,dice_held_container,current_dice_container,scores_possible,score_board)
                        continue

                elif hold_input == '2':
                    if dice_held_container[1] == 0:
                        dice_held_container[1] = 1

                        display.reset_board(current_turn,players_container,dice_held_container,current_dice_container,scores_possible,score_board)
                        continue

                    elif dice_held_container[1] == 2:
                        print()
                        print("Sorry you cannot change that die. ")
                        print()
                        continue
                    else:
                        dice_held_container[1] = 0
                        display.reset_board(current_turn,players_container,dice_held_container,current_dice_container,scores_possible,score_board)
                        continue

                elif hold_input == '3':
                    if dice_held_container[2] == 0:
                        dice_held_container[2] = 1
                        display.reset_board(current_turn,players_container,dice_held_container,current_dice_container,scores_possible,score_board)
                        continue
                    elif dice_held_container[2] == 2:
                        print()
                        print("Sorry you cannot change that die. ")
                        print()
                        continue
                    else:
                        dice_held_container[2] = 0
                        display.reset_board(current_turn,players_container,dice_held_container,current_dice_container,scores_possible,score_board)
                        continue
                elif hold_input == '4':
                    if dice_held_container[3] == 0:
                        dice_held_container[3] = 1

                        display.reset_board(current_turn,players_container,dice_held_container,current_dice_container,scores_possible,score_board)
                        continue

                    elif dice_held_container[3] == 2:
                        print()
                        print("Sorry you cannot change that die. ")
                        print()
                        continue

                    else:
                        dice_held_container[3] = 0
                        display.reset_board(current_turn,players_container,dice_held_container,current_dice_container,scores_possible,score_board)
                        continue

                elif hold_input == '5':
                    if dice_held_container[4] == 0:
                        dice_held_container[4] = 1

                        display.reset_board(current_turn,players_container,dice_held_container,current_dice_container,scores_possible,score_board)
                        continue

                    elif dice_held_container[4] == 2:
                        print()
                        print("Sorry you cannot change that die. ")
                        print()
                        continue

                    else:
                        dice_held_container[4] = 0

                        display.reset_board(current_turn,players_container,dice_held_container,current_dice_container,scores_possible,score_board)
                        continue

                elif hold_input == '6':
                    if dice_held_container[5] == 0:
                        dice_held_container[5] = 1

                        display.reset_board(current_turn,players_container,dice_held_container,current_dice_container,scores_possible,score_board)
                        continue

                    elif dice_held_container[5] == 2:
                        print()
                        print("Sorry you cannot change that die. ")
                        print()
                        continue
                    else:
                        dice_held_container[5] = 0

                        display.reset_board(current_turn,players_container,dice_held_container,current_dice_container,scores_possible,score_board)
                        continue


                #roll the dice
                elif str(hold_input).lower() == "r" or str(hold_input).lower() == "roll":



                    dice_roll = 0
                    #check to make sure they held any dice eg: if any indices are 1 then safe to roll... if no ones then try again...
                    #Player must hold at least one dice
                    for dice in range(6):
                        if dice_held_container[dice] == 1:
                            score_board = score.update_temp_score(score_board,True,current_turn,dice_held_container,current_dice_container)
                            dice_held_container = update_hold_indices(dice_held_container)
                            #display.reset_board(current_turn,players_container,dice_held_container,current_dice_container,scores_possible,score_board)
                            dice_roll += 1
                            break

                    if dice_roll == 0:
                            print()
                            print("You need to hold at least one dice each turn!")
                            print()
                            time.sleep(5)
                            continue
                    break



                elif str(hold_input).lower() == "s" or str(hold_input).lower() == "score":
                    print()
                    print("⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹    CURRENT SCORES     ⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹")
                    n=1
                    for x in range(num_playing):
                        string = "player{n}".format(n=n)
                        n+=1
                        currentplayer = players_container[string].title()
                        print()
                        print("{name}   -   {score}".format(name=currentplayer.title(),score=score_board[string]))
                        print()

                    time.sleep(6)
                    display.reset_board(current_turn,players_container,dice_held_container,current_dice_container,scores_possible,score_board)
                    continue


                elif str(hold_input).lower() == "done" or str(hold_input).lower() == "d":

                    score_board = score.update_temp_score(score_board,True,current_turn,dice_held_container,current_dice_container)
                    score_board = score.update_score(score_board,current_turn)
                    dice_held_container = score.reset_indices(dice_held_container)
                    (current_turn,score_board) = change_turn(current_turn,num_playing,score_board)

                    break
        else:
            dice_held_container = score.reset_indices(dice_held_container)
            (score_board, current_turn) = rolled_nothing_change_turn(current_turn,score_board,num_playing)
            continue




def change_turn(current_turn,num_playing,score_board):

    if current_turn == "player1" and num_playing == 1:
        score_board['player1tempscore'] = 0
        current_turn = "player1"

    elif current_turn == "player1" and num_playing > 1:
        score_board['player1tempscore'] = 0
        current_turn = "player2"

    elif current_turn == "player2" and num_playing == 2:
        score_board['player2tempscore'] = 0
        current_turn = "player1"

    elif current_turn == "player2" and num_playing > 2:
        score_board['player2tempscore'] = 0
        current_turn = "player3"

    elif current_turn == "player3" and num_playing == 3:
        score_board['player3tempscore'] = 0
        current_turn = "player1"

    elif current_turn == "player3" and num_playing > 3:
        score_board['player3tempscore'] = 0
        current_turn = "player4"

    elif current_turn == "player4":
        score_board['player4tempscore'] = 0
        current_turn = "player1"

    return(current_turn,score_board)


def rolled_nothing_change_turn(current_turn,score_board,num_playing,):


        if current_turn == "player1" and num_playing == 1:
            score_board['player1tempscore'] = 0
            current_turn = "player1"
            print()
            print("You did not score anything. Try again. ")
            print()
            time.sleep(5)

        elif current_turn == "player1" and num_playing > 1:
            score_board['player1tempscore'] = 0
            current_turn = "player2"
            print()
            print("You did not score anything. It's player 2's turn. ")
            print()
            time.sleep(5)


        elif current_turn == "player2" and num_playing == 2:
            score_board['player2tempscore'] = 0
            current_turn = "player1"
            print()
            print("You did not score anything. It's player 1's turn. ")
            print()
            time.sleep(5)


        elif current_turn == "player2" and num_playing > 2:
            score_board['player2tempscore'] = 0
            current_turn = "player3"
            print()
            print("You did not score anything. It's player 3's turn. ")
            print()
            time.sleep(5)



        elif current_turn == "player3" and num_playing == 3:
            score_board['player3tempscore'] = 0
            current_turn = "player1"
            print()
            print("You did not score anything. It's player 1's turn. ")
            print()
            time.sleep(5)



        elif current_turn == "player3" and num_playing > 3:
            score_board['player3tempscore'] = 0
            current_turn = "player4"
            print()
            print("You did not score anything. It's player 4's turn. ")
            print()
            time.sleep(5)




        elif current_turn == "player4":
            score_board['player4tempscore'] = 0
            current_turn = "player1"
            print()
            print("You did not score anything. It's player 1's turn. ")
            print()
            time.sleep(5)


        else:
            print()
            print("You didn't roll anything, try again! ")
            print()
            time.sleep(5)

        return (score_board,current_turn)









def update_hold_indices(dice_held_container):
    for dice in range(6):
        if dice_held_container[dice] == 1:
            dice_held_container[dice] = 2
    return dice_held_container




main()
