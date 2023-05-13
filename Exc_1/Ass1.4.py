"""Write a program that asks the user to enter a number of seconds and works"""

# Hayrunnisa Bıyıklı 21091010143

seconds = int(input("Enter the number of seconds: ")) # Get number of seconds from user

# Calculate days, hours, minutes, and remaining seconds
days = seconds // 86400
seconds %= 86400
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

# Display the converted time
if days > 0:
    print("Converted time: {} days, {} hours, {} minutes, {} seconds".format(days, hours, minutes, seconds))
elif hours > 0:
    print("Converted time: {} hours, {} minutes, {} seconds".format(hours, minutes, seconds))
elif minutes > 0:
    print("Converted time: {} minutes, {} seconds".format(minutes, seconds))
else:
    print("Converted time: {} seconds".format(seconds))
