def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

# Example usage
num1 = int(input("Enter the numerator: "))
num2 = int(input("Enter the denominator: "))

output = divide(num1, num2)
print("Result:", output)
