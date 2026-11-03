
# Program to check if a date is valid or not

day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

def is_leap_year(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def is_valid_date(d, m, y):
    if y < 1 or m < 1 or m > 12 or d < 1:
        return False

    # Days in each month (index 0 unused)
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Adjust February for leap year
    if is_leap_year(y):
        days_in_month[2] = 29

    if d > days_in_month[m]:
        return False

    return True

if is_valid_date(day, month, year):
    print(f"{day:02d}-{month:02d}-{year} is a VALID date")
else:
    print(f"{day:02d}-{month:02d}-{year} is an INVALID date")
