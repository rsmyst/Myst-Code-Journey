# Tic Tac Toe Game for 2 Players
from secrets import choice
import time

def full_game():
    print("Welcome to the tic tac toe game!")
    def pref():
        p1pref = -1
        acc_values = ["X", "O"]
        if p1pref == -1:
            p1pref = input("Choose whether P1 wants to be an X or O: ")
            p1pref = p1pref.upper()
        while p1pref not in acc_values:
            print(f"Sorry, {p1pref} isn't an accepted value. Enter again.")
            p1pref = input("Choose whether you want to be X or O: ")
            p1pref = p1pref.upper()
        acc_values.remove(p1pref)
        p2pref = acc_values[0]
        print("Player 1 is,", p1pref)
        print("Player 2 is,", p2pref)
        return p1pref, p2pref

    p1pref,p2pref = pref()


    time.sleep(1.5)
    print("Here's a view of the current board, You can enter values from 1-9 to place your respective signs in! Enjoy!")


    def dis_board(plist  = (" "," "," "," "," "," "," "," "," ")):
        leng = len(plist)
        for item in plist:
            i1 = plist[0]
            i2 = plist[1]
            i3 = plist[2]
            i4 = plist[3]
            i5 = plist[4]
            i6 = plist[5]
            i7 = plist[6]
            i8 = plist[7]
            i9 = plist[8]
        print(f"""     
        __________________________
            {i1}    |   {i2}    |   {i3}   
        __________________________
            {i4}    |   {i5}    |   {i6}    
        __________________________
            {i7}    |   {i8}    |   {i9}    
        __________________________
            """)

    time.sleep(2)
    dis_board()

    def game_logic(plist):
        n = 0
        if [plist[0], plist[1], plist[2]] == ["X", "X", "X"] or [plist[3], plist[4], plist[5]] == ["X", "X", "X"] or [plist[6], plist[7], plist[8]] == ["X", "X", "X"] or [plist[0], plist[3], plist[6]] == ["X", "X", "X"] or [plist[2], plist[5], plist[8]] == ["X", "X", "X"] or [plist[0], plist[4], plist[8]] == ["X", "X", "X"] or [plist[2], plist[4], plist[6]] == ["X", "X", "X"] or [plist[1], plist[4], plist[7]] == ["X", "X", "X"]:
            print("game over! X wins")
            n = 2
        elif [plist[0], plist[1], plist[2]] == ["O", "O", "O"] or [plist[3], plist[4], plist[5]] == ["O", "O", "O"] or [plist[6], plist[7], plist[8]] == ["O", "O", "O"] or [plist[0], plist[3], plist[6]] == ["O", "O", "O"] or [plist[2], plist[5], plist[8]] == ["O", "O", "O"] or [plist[0], plist[4], plist[8]] == ["O", "O", "O"] or [plist[2], plist[4], plist[6]] == ["O", "O", "O"] or [plist[1], plist[4], plist[7]] == ["O", "O", "O"]:
            print("game over! O wins")
            n = 1

        return n 

    def p1_choice():
        num_check = ["1","2",'3','4','5','6','7','8','9']
        num_check2 = [1,2,3,4,5,6,7,8,9]
        choice1 = -1
        if choice1 == -1:
            choice1 = input("Player 1, Enter a number from 1-9 to place a cross or circle: ")
        while choice1 not in num_check:
            print("1-chan, you can only enter numbers, no words please!")
            choice1 = input("Player 1, Enter a number from 1-9 to place a cross or circle: ")
        choice1 = int(choice1)
        while choice1 not in num_check2:
            print("1-chan, You entered a number out of range, you can't place things outside the board (just yet).")
            choice1 = int(input("Player 1, Enter a number from 1-9 to place a cross or circle: "))
        return choice1
    def p2_choice():
        num_check = ["1","2",'3','4','5','6','7','8','9']
        num_check2 = [1,2,3,4,5,6,7,8,9]
        choice2 = -1
        if choice2 == -1:
            choice2 = input("Player 2, Enter a number from 1-9 to place a cross or circle: ")
        while choice2 not in num_check:
            print("2-chan, you can only enter numbers, no words please!")
            choice2 = input("Player 2, Enter a number from 1-9 to place a cross or circle: ")
        choice2 = int(choice2)
        while choice2 not in num_check2:
            print("2-San, You entered a number out of range, you can't place things outside the board (just yet)")
            choice2 = int(input("Player 2, Enter a number from 1-9 to place a cross or circle: "))
        print(choice2)
        return choice2


    def p1new_board(plist):
        p1choice = p1_choice() - 1
        while plist[p1choice] in ["X", "O"]:
            print("You can't enter values there! It's occupied! \n")
            p1choice = p1_choice()
        plist[p1choice] = p1pref
        print(100*"\n")
        dis_board(plist)

    def p2new_board(plist):
        p2choice = p2_choice() - 1
        while plist[p2choice] in ["X", "O"]:
            print("You can't enter values there! It's occupied!\n")
            p2choice = p2_choice()
        plist[p2choice] = p2pref
        print(100*"\n")
        dis_board(plist)

    player_list = [" "," "," "," "," "," "," "," "," "]

    def game(player_list):
        i = 0
        while " " in player_list:
            if i%2 == 0:
                p1new_board(player_list)
                b = game_logic(player_list)
                i+=1

                if b==1:
                    break
            else:    
                p2new_board(player_list)
                b = game_logic(player_list)
                i+=1
                if b==2:
                    break
    game(player_list)
    j = int(input("Enter 0 if you want to replay the game and anything else if you want to quit: "))
    return j
j = full_game()
while j <1:
    print("Please wait while we clear up the old boards")
    time.sleep(3)
    print(100*"\n")
    time.sleep(1)
    full_game()

