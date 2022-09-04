# Step 5
# Import date-time
from time import time

# Step 2
# Set gameCount
gameCount = 0

# Step 5
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

    # Step 4
    # Wait for number
    while True:
        # Step 4
        # Use try-except to handle error
        try:
            # Get the number of lightyears travelled
            playerPlanetDistance = float(input("How many lightyears away is that? "))
            break
        except ValueError:
            print("Oops! That was not a number. Try again...")
    
    # Print "Hello playerName from playerPlanet! playerPlanetDistance lightyears is very far away."
    print("Hello {0} from {1}! {2} lightyears is very far away".format(playerName, playerPlanet, playerPlanetDistance))
    
    # Step 2
    # Print how many times this was played
    print("You have played {} times.".format(gameCount))

    # Step 3
    # Let players quit
    keepPlaying = input("Do you want to keep playing? Enter y for yes, enter n for no. ")
    if keepPlaying.lower() == "n":
        break
    else:
        continue

# Step 5
# Set gameEnd
gameEnd = time()
# Set timePlayed
timePlayed = gameEnd - gameStart
# Print time played
print("You played for {} seconds".format(int(timePlayed)))