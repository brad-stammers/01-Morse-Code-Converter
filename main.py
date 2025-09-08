###################################################################################################
#   100 Days of Code: The Complete Python Pro Bootcamp
#   Portfolio Assignment 01 - Morse Code Converter
###################################################################################################

ALPHANUMERIC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
MORSE = ['._', '_...', '_._.', '_..', '.', '.._.', '__.', '....', '..', '.___', '_._', '._..', '__', '_.', '___', '.__.', '__._', '._.', '...', '_', '.._', '..._', '.__', '_.._', '_.__', '__..', '_____', '.____', '..___', '...__', '...._', '.....', '_....', '__...', '___..', '____.']

# initialise
exit_convert = False


# process
while not exit_convert:
    morse_convert = []
    # prompt for text to convert
    prompt = input('Enter any string of words and numbers you would like to convert to Morse Code (enter a blank to exit):  ').lower()

    # check exit state
    if prompt == "":
        exit_convert = True
    else:
        for char in prompt:
            idx = ALPHANUMERIC.index(char)
            morse_convert.append(MORSE[idx])

        # output results
        morse_output = " ".join(morse_convert)
        print(f"The Morse Code equivalent of your string is: {morse_output}\n")



