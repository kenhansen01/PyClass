# Step 4
# Import date-time
from time import time

# Step 2
# Set gameCount
gameCount = 0

# Step 4
# Set gameStart
gameStart = time()

# Step 1
# Play again
while True:
    
    # Step 2
    # Increment game Count
    gameCount += 1
    
    # Get name from player, store it in a variable playerName
    playerName = input("What is your name? ")
    
    # Get planet from player, store it in variable playerPlanet
    playerPlanet = input("What planet are you from? ")
    
    # Print "Hello playerName from playerPlanet"
    print("Hello {0} from {1}!".format(playerName, playerPlanet))
    
    # Step 2
    # Print how many times this was played
    print("You have played {} times.".format(gameCount))

    # Step 3
    # Let players quit
    keepPlaying = input("Do you want to keep playing? Enter y for yes, enter n for no. ")
    if keepPlaying.lower() == "n":
        break

# Step 4
# Set gameEnd
gameEnd = time()
# Set timePlayed
timePlayed = gameEnd - gameStart
# Print time played
print("You played for {} seconds".format(int(timePlayed)))