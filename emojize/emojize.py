import emoji

# // Get the user input
inp: str = input("Input: ")

# // Convert the input to an emojized string
emojized: str = emoji.emojize(inp, language='alias')

# // Print the emojized result
print(emojized)
