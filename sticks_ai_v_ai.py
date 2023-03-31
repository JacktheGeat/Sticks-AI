# AI vs AI. really cool. takes a while but they get there eventually.

import random


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
        elif current_player[1] == "ai":
            num = 0
            num = random.choice(current_player[2][sticks - 1])
            current_player[3][sticks - 1].append(num)
            print("Player ", current_player[0], " Chose: ", num)
            sticks -= num
            placeholder = current_player
            current_player = other_player
            other_player = placeholder
        elif current_player[1] == "perfect":
            num = 0
            for i in range(3):
                if ((sticks - (i+1)) % 5) == 0:
                    num = i+1
            if sticks <= 4:
                num = sticks - 1
            if num == 0: num = 1
            print("Player 2: How many sticks do you choose? ", num)
            sticks -= num
            placeholder = current_player
            current_player = other_player
            other_player = placeholder
    if current_player == player1:
        print("Player 1 wins!")
    else: 
        print("Player 2 wins!")
    if current_player[1] == "ai":
        index = 0
        for i in current_player[3]:
            if len(i) > 0:
                current_player[2][index].append(i[0])
                current_player[3][index].pop(0)
            index += 1
    if other_player[1] == "ai":
        index = 0
        for i in other_player[3]:
            if len(i) > 0: other_player[3][index].pop(0)
            index += 1

    # Complete this function
    # Feel free to define as many additional function as you think are useful

def initialize_ai(player_num, total_sticks):
    """Create a new AI player represented as a 4-tuple of the form
    (player_num, "ai", hats, besides_hats)."""
    hats = []
    besides_hats = []
    for i in range(total_sticks):
        hats.append([1, 2, 3])
        besides_hats.append([])
    # Add code to initialize the hat contents
    # Add code to initialize what's besides the hats
    return (player_num, "ai", hats, besides_hats)


# Main

def sticks():
    total_sticks = introduction()
    player1 = initialize_ai(1, total_sticks)
    player2 = initialize_ai(2, total_sticks)
    
    keep_playing = 'y'
    x = 0
    while keep_playing == 'y':
        one_round_of_sticks(total_sticks, player1, player2)
        print("HATS:", player2[2]) # see what the AI is learning
        keep_playing = get_yn_input()
        if keep_playing == 'y':
            print("Great!")
    print("Ok. See you next time. Bye, bye!")

    
### DO NOT DELETE THIS LINE: beg testing

sticks()
