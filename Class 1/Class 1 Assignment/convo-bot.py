# Import time from the time module
from time import time

# Set gameStart to time
gameStart = time()

# Set gameName to convo-bot
gameName = "convo-bot" 
# Set roundCounter to 0
roundCounter = 0

# Make an infinite while loop
while True:
    # Create empty variables by assigning value None.
    # playerName, playerAge, favoriteGame, gameEnd, gameAge
    playerName = playerAge = favoriteGame = gameEnd = gameAge = None

    # Print You have played roundCounter times.
    print("You have played {} times.".format(roundCounter))
    
    # Use input to set letsPlay. Ask if player would like to play
    letsPlay = input("Do you want to play a game? Enter y for yes, enter n for no")
    
    # If letsPlay equals no, break
    if letsPlay.lower() == "n":
        break
    
    # Increment roundCounter
    roundCounter += 1
    
    # Print "Hello, my name is " gameName 
    print("Hello my name is {}.".format(gameName))
    
    # Use input to set playerName.
    playerName = input("What is your name? ")
    
    # Print "Nice to meet you " playerName
    print("Nice to meet you {}.".format(playerName))
    
    # Use input to set favoriteGame.
    favoriteGame = input("What is your favorite game? ")
    
    # Print favoriteGame " sounds fun. I am my own favorite game."
    print("{} sounds fun! My favorite game is me.".format(favoriteGame))
    
    while True:
        # try
        try:
            # Use input to get playerAge as an integer
            playerAge = int(input("How old are you? "))
            break
        # except
        except ValueError:
            # Print I only understand whole numbers for your age. Let's start over...
            print("I only understand integers. Please try again...")
            # continue
            continue
    
    # Set gameEnd to now
    gameEnd = time()
    
    # Set gameAge to gameEnd - gameStart
    gameAge = gameEnd - gameStart
    
    # Print Wow, is that in years?. I am only gameAge milliseconds old
    print("Wow is that in years? I am only {} milliseconds old".format(int(gameAge * 1000)))