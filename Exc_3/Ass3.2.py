date = input("Enter a date in the format mm/dd/yyyy: ")

# split the date into month, day, and year components
month, day, year = date.split('/')

# convert the month component to its corresponding name
month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month_name = month_names[int(month) - 1]

print(month_name, day + ',', year)








