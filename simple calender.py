import calendar

# Simple calendar program
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# Display calendar
print(calendar.month(year, month))
