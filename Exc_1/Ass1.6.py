"""The distance a vehicle travels can be calculated as follows: distance = speed x time"""

# Hayrunnisa Bıyıklı 21091010143

# Get user input for speed and time
speed = float(input("What is the speed of the vehicle in mph? "))
hours = int(input("How many hours has it traveled? "))

# Print header for distance traveled
print("Hour\tDistance Traveled")

# Loop through each hour and calculate distance traveled
for hour in range(1, hours + 1):
    distance = speed * hour
    print("{}\t    {}".format(hour, distance))
