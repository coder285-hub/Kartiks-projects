def main():
    user_input = input("Input:")
    final_result = shorten(user_input)
    print("Output: " + final_result)

def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""

    for char in user_input:
        if char not in vowels:
            result = result + char

    return result

if __name__ == "__main__":
    main()
