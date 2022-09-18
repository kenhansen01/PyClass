# Assign alphabet a string value "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Get secret message from user input.
# Assign the secret message to stringToEncrypt


# Get secret key from user, the value should be an integer from 1 - 25.
# Assign the secret key to shiftAmount
# Extra bonus yippee hooray - tell the user if they need to enter a number or if it is too high or low


# Assign encryptedString an empty string ""


# Encrypt each letter in the message, keep other characters (punctuation)
# for letter in stringToEncrypt
#### Find the letter in alphabet and assign the index to position
#### alphabet.find(letter.upper()) will find the index of the first time the letter appears
#### Add position and shiftAmount and assign the value to newPosition
#### if letter in alphabet
######## Add encryptedString and alphabet[newPosition] and assign to encryptedString
#### else
######## Add encryptedString and letter and assign to encryptedString