game_list = [0,1,2]
def display_game(game_list):
    print("Here is the current list:")
    print(game_list)
display_game(game_list)
def position_choice():
    choice = "Wrong"
    while choice not in [0,1,2]:
        choice = input("pick a position(0,1,2)")
        if choice not in ["0", "1", "2"]:
            print("sorry invalid chocie")
    return

position_choice()