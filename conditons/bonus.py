salary = int(input("enter your salary: "))
experience = int(input("enter your experience (years): "))

if experience >= 10:
    bonus = salary * 20 / 100
    print(f"20% bonus: {bonus}")
elif experience >= 5:
    bonus = salary * 10 / 100
    print(f"10% bonus: {bonus}")
elif experience >= 2:
    bonus = salary * 5 / 100
    print(f"5% bonus: {bonus}")
else:
    print("no bonus, less than 2 years experience")