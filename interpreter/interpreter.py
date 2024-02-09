expression = input("Enter an arithmetic expression (e.g., 1 + 1): ")


z, y, x = expression.split()

    # Convert operands to integers
x = int(x)
z = int(z)

    # Perform the operation based on the operator
if y == '+':
    result = z + x
elif y == '-':
    result = z - x
elif y == '*':
    result = z * x
elif y == '/':
    try:
        result = z / x
    except (ValueError, ZeroDivisionError):
        print("Invalid input. Please enter a valid arithmetic expression.")

print(round(result,1))


