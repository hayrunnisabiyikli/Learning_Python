"""Create a list with includes 5,9, 10, 12, 7, 3, 11 numbers. Write the code that finding the
length, biggest- smallest element, sum, average and sort the list."""
# Hayrunnisa Bıyıklı - 21091010143
numbers = [5, 9, 10, 12, 7, 3, 11]

length = len(numbers)

biggest = max(numbers)
smallest = min(numbers)

total = sum(numbers)

average = total / length

sorted_numbers = sorted(numbers)

print("List of numbers:", numbers)
print("Length of the list:", length)
print("Biggest element:", biggest)
print("Smallest element:", smallest)
print("Sum of elements:", total)
print("Average of elements:", average)
print("Sorted list:", sorted_numbers)
