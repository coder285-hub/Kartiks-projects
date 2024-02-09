user_input=input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

user_input_stripped = user_input.strip()

if user_input_stripped == "42" or user_input_stripped == "forty-two" or user_input_stripped == "Forty two" or user_input_stripped == "forty two" or user_input_stripped == "FoRty TwO":
    print("yes")

else:
    print("no")
