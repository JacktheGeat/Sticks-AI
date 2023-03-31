# you can't win. its literally the mathematically perfect algorithm.
def play():
    stickstart = 0
    while stickstart < 10 or stickstart > 100: 
        stickstart = int(input("How many sticks are there on the table initially (10-100)?"))
        if stickstart < 10 or stickstart > 100: print("That's not a valid number! Try again!")
    
    sticks = stickstart
    player = True
    while sticks > 0:
        print("There are ", sticks, "sticks.")
        if player:
            num = 0
            while num < 1 or num > 3 or num > sticks: 
                num = int(input("Player 1: How many sticks do you choose? "))

                if num < 1 or num > 3: print("That's not a valid number! Try again!")
            sticks -= num
            player = False
        else:
            num = 0
            for i in range(3):
                if ((sticks - (i+1)) % 5) == 0:
                    num = i+1
            if sticks <= 4:
                num = sticks - 1
            if num == 0: num = 1
            print("Player 2: How many sticks do you choose? ", num)
            sticks -= num
            player = True
    if player:
        print("Player 1 wins!")
    else: print("Player 2 wins!")

playing = True
while playing:
    play()
    x = input("Would you like to play again? (y/n)")
    if x == "n": playing = False