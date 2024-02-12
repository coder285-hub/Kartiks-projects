user_input = input("Input:")

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""

for char in user_input:
    if char not in vowels:
        result = result + char

print("\nAfter removing Vowels: ", result)
