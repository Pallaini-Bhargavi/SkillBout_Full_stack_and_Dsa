
numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)


print("Reverse order:", numbers[::-1])


total = sum(numbers)
average = total / len(numbers)

# Step 4: Print sum and average
print("Sum :", total)
print("Average :", average)
