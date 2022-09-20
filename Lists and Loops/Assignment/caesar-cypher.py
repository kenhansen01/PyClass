# Assign alphabet a string value "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Get secret message from user input.
# Assign the secret message to stringToEncrypt


# Get secret key from user, the value should be an integer from 1 - 25. 
# Use the while - try except pattern to check
# Assign shiftAmount the secret key 
# Extra bonus yippee hooray - tell the user if they need to enter a number or if it is too high or low


# Assign encryptedString an empty string ""


# Encrypt each letter in the message, keep other characters (punctuation)
# for letter in stringToEncrypt

    # Find the letter in alphabet and assign the index to position
    # alphabet.find(letter.upper()) will find the index of the first time the letter appears


    # Assign newPosition the value of position + shiftAmount


    # if letter in alphabet

        # Assign encryptedString the value encryptedString + alphabet[newPosition]
         
         
    # else

        # Assign encryptedString the value encryptedString + letter
