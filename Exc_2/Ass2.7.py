"""Design a program that asks the user to enter a series of 20 numbers. The program should store the numbers in a list """
# Hayrunnisa Bıyıklı - 21091010143
numbers = []
for i in range(20):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

lowest = min(numbers)

highest = max(numbers)

total = sum(numbers)

average = total / len(numbers)

print(f"Lowest number: {lowest}")
print(f"Highest number: {highest}")
print(f"Total: {total}")
print(f"Average: {average}")
