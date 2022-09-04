# Get name from player, store it in a variable playerName
playerName = input("What is your name? ")
# Get planet from player, store it in variable playerPlanet
playerPlanet = input("What planet are you from? ")
# Get the number of lightyears travelled
playerPlanetDistance = int(input("How many lightyears away is that? ")) # change to float for decimals
# Print "Hello playerName from playerPlanet! playerPlanetDistance lightyears is very far away."
print("Hello", playerName, "from", playerPlanet, "!", playerPlanetDistance, "lightyears is very far away.") # sep=None --> Make it better --> print("Hello {0} from {1}!".format(playerName, playerPlanet)) 