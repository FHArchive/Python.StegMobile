'''
Kieran W

StegMobile encoder/ decoder
'''

text = [
    "1:",
    "2:abc",
    "3:def",
    "4:ghi",
    "5:jkl",
    "6:mno",
    "7:pqrs",
    "8:tuv",
    "9:wxyz",
    "0: "
    ]


def encode(message):
    # Set up encodedMessage to return to calling program
    encodedMessage = ""
    # Go through each charInMessage
    for messageChar in range(len(message)):
        charInMessage = message[messageChar]
        # Go through each numberCharDict
        for textNumber in range(len(text)):
            numberCharDict = text[textNumber]
            '''
            If the charInMessage appears in numberCharDict add the correct
            number of numbers to the encodedMessage
            '''
            for phoneChar in range(2,len(numberCharDict)):
                if(charInMessage == numberCharDict[phoneChar]):
                    for iteration in range (phoneChar - 1):
                        encodedMessage += numberCharDict[0]
                    # Add "-" after each sequence of numbers
                    encodedMessage += "-"
    return encodedMessage



def decode(message):
    # Set up decodedMessage to return to calling program
    decodedMessage = ""
    # Split the message into parts
    messageParts = message.split("-")
    # Go through each of these parts
    for part in range(len(messageParts)):
        numberSeq = messageParts[part]
        # Go through each numberCharDict
        for textNumber in range(len(text)):
            numberCharDict = text[textNumber]
            if (len(numberSeq) and (numberCharDict[0] == numberSeq[0])):
                decodedMessage += numberCharDict[len(numberSeq)+1]

    return decodedMessage



# Define an interface
def cli():
    print("Encode/ decode message or quit (E/d/q)" )
    choice = input(">")
    if (len(choice) > 0):
        choice = choice[0].lower()

    # Quit application
    if choice == "q":
        return True

    # All functions require a message
    print("Type (or copy in) your message (use '-' to seperate numbers)")
    inputMessage = input(">")

    # DECODE
    if (choice == "d"):
        print(decode(inputMessage))
    # DEFAULT = ENCODE
    else:
        print(encode(inputMessage))

# Run the cli while the user has not finished
finished = False
while not finished:
    finished = cli()


