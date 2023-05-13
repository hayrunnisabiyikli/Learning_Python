number = 0
while number <= 0:
    number=int(input("enter a nonnegative number/integer:"))
factorial = 1
for factor in range(1, number+1):
    factorial *= factor  #factorial = factorial * factor
print("the factorial of ",number,"is", factorial)