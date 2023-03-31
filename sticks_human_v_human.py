# human vs human combat. its really boring.

def get_yn_input():
    """Get a yes/no answer from the user."""
    yes_no = input("Do you want to play again? Type y or n.    ")
    while yes_no not in ["y", "n"]:
        print("Please input 'y' or 'n'.")
        yes_no = input("Do you want to play again? Type y or n.    ")
    return yes_no
    
def introduction():
    stickstart = 0
    while stickstart < 10 or stickstart > 100: 
        stickstart = int(input("How many sticks are there on the table initially (10-100)?"))
        if stickstart < 10 or stickstart > 100: print("That's not a valid number! Try again!")
    return stickstart

def one_round_of_sticks(sticks, player1, player2):
    """player1 and player2 play one round of sticks against each other. 
    They start with a pile of total_sticks sticks."""
    current_player = player1
    other_player = player2
    while sticks > 0:
        print("There are ", sticks, "sticks.")
        if current_player[1] == "human":
            num = 0
            while num < 1 or num > 3 or num > sticks: 
                num = int(input("Player 1: How many sticks do you choose? "))

                if num < 1 or num > 3: print("That's not a valid number! Try again!")
            sticks -= num
            placeholder = current_player
            current_player = other_player
            other_player = placeholder
    if current_player == player1:
        print("Player 1 wins!")
    else: print("Player 2 wins!")
    # Complete this function
    # Feel free to define as many additional function as you think are useful

def sticks():
    total_sticks = introduction()
    player1 = (1, "human")
    player2 = (2, "human")
    
    keep_playing = 'y'
    while keep_playing == 'y':
        one_round_of_sticks(total_sticks, player1, player2)
        keep_playing = get_yn_input()
        if keep_playing == 'y':
            print("Great!")

    print("Ok. See you next time. Bye, bye!")

    
### DO NOT DELETE THIS LINE: beg testing

sticks()
