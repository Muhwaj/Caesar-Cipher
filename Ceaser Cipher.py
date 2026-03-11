
#PESUDOCODE
# Repeat this for each character in initialMessage:
# if character is in possibleCharacters:
#   1) Find the initialPositon of the character
#   2) if encrypt:
#         shiftedPosition = initialPosition + key
#       else decrypt:
#         shiftedPosition = initialPosition - key
#  3)if shiftedPosition >= len(possibleCharacters)
#           shiftedPosition = shiftedPosition - len(possibleCharacters)
#   elif shiftedPosition < 0
#          shiftedPosition = shiftedPosition + len(possibleCharacters)
#   4) Find the character at the shiftedPosition
#   5) Add the character to the shiftedMessage
# else: keep the character same

import string 

# Global variables
initialPosition = 0
shiftedPosition = 0
shiftedMessage = ""
lettersLower = string.ascii_lowercase
lettersUpper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation 
possibleCharacters = lettersLower + lettersUpper + numbers + symbols 

#Define the function called encryptOrDecrypt
def encryptOrDecrypt():
    global shiftedPosition
    if mode.lower() == "e":
            shiftedPosition = initialPosition + key 
    elif mode.lower() == "d":
            shiftedPosition = initialPosition - key


#Define the function called wraparound
def wraparound():
    global shiftedPosition
    if shiftedPosition >= len(possibleCharacters):
        shiftedPosition = shiftedPosition - len(possibleCharacters)
    elif shiftedPosition < 0:
        shiftedPosition = shiftedPosition + len(possibleCharacters)

# Run code

# Introduction
print("Welcome! This program will encrypt or decrypt your secret message using the Caesar cipher. \n\nWhen creating your message, you may only choose from the following characters:\n"+ possibleCharacters + "\n\nLet's get started!\n")

# Receive user input, variables declaration
initialMessage = input("What is your message? ")
key = int(input("What is the key? Choose a number from 0 to 93. "))
mode = input("For Encrypt type 'e'\nFor Decrypt type 'd'\n")

# Encrypt or decrypt the message
for character in initialMessage:
    if character in possibleCharacters:
        initialPosition = possibleCharacters.find(character)
        encryptOrDecrypt()
        wraparound()
        shiftedMessage = shiftedMessage + possibleCharacters[shiftedPosition]
    else:
        shiftedMessage = shiftedMessage + character

# Print the shifted message
if mode.lower() == "e":
    print("Your encrypted message is: "  + shiftedMessage)
else:
    mode.lower() == "d"
    print("Your decrypted message is: "  + shiftedMessage)