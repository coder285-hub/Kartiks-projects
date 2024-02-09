expression = input("Enter an arithmetic expression (e.g., 1 + 1): ")

try:
    result = calculate(expression)
    print("Result:", result)
except (ValueError, ZeroDivisionError):
    print("Invalid input. Please enter a valid arithmetic expression.")

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
    result = z / x

return round(result, 1)  # Round the result to one decimal place



