import random

while True:
    level = int(input("Level:" ))
    while True:
            guess = int(input("Guess: "))
            if guess > x:
                print("Too large!")
            elif guess < x:
                print("Too small!")
            elif guess == x:
                print("Just right!")
                raise EOFError
    except ValueError:
        pass
    except EOFError:
        break
