graduated = input("are you graduated or not(yes/no): ").strip().lower()
experience = int(input("enter your experience in years: "))
percentage = int(input("enter your percentage: "))

if graduated == 'no':
    print("you are not eligible to apply")
elif graduated == 'yes':
    if experience > 2 or percentage > 70:
        print("you are eligible to apply, move on to the next step")
    else:
        print("you are not eligible to apply")
else:
    print("invalid input for graduation status")