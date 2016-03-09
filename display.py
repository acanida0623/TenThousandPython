def initiate_players():

    while True:
        try:
            number_playing = int(input("How many people will be playing? "))
        except:
            ValueError
            print ("Please pick a number between 1 and 4.")

            continue

        else:
            if number_playing > 0 and number_playing < 5:
                return number_playing

            else:
                print ("Please pick a number between 1 and 4.")
                continue

def define_player_names(numberplaying):
    players_container = {}

    for x in range(numberplaying):
        playernumber = x + 1

        strings = "What is the name of {PLAYER}? ".format(PLAYER="player "+str(playernumber))

        #set names for player 1-4

        playername = input(strings).lower()

        playerposition = "player"+str(playernumber)

        #add all the players and their names to the players dictionary
        players_container.update({playerposition: playername})
    return players_container

        #players[playerposition] = playername

def reset_board(current_turn,players_container,dice_held_container,current_dice_container,scores_possible,score_board):
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
    print("⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹")
    print("                                         |")
    print("       {player}'s current dice                        Dice Held From Last Turn  ".format(player=currentplayer))
    print("                                         |")
    print("⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹")

    for dice in range(6):

        #check if dice are held in player's hand, 1 means held to check score, 0 means not held

        dice_number = dice + 1

        if dice_held_container[dice] == 0:

            print ()
            print("DICE NUMBER {num} :  {roll}".format(num=dice_number,roll=current_dice_container[dice]))
            print ()

        elif dice_held_container[dice] == 2:

            print ()
            print("                                                        {roll}".format(roll=current_dice_container[dice]))
            print ()


        else:
            print()
            print("DICE NUMBER {num} IS BEING HELD :  {roll}".format(num=dice_number,roll=current_dice_container[dice]))
            print()
    print ("Possible combonations : ",scores_possible)
    possible = "{name}tempscore".format(name=current_turn)
    print ("Tenative Score -",score_board[possible])

def list_commands():
    print()
    print(" 1 - 6   -  Hold/Unhold Dice")
    print("(R)oll - roll all dice not currently held. ")
    print("(D)one - finish your turn and add your score to bank")
    print("(S)core - list current scores")
    print()
