num = int(input("Enter a number: "))

div_by_2 = (num % 2 == 0)
div_by_3 = (num % 3 == 0)

if div_by_2 and div_by_3:
    print(f"{num} is divisible by both 2 and 3")
elif div_by_2:
    print(f"{num} is divisible by 2 only")
elif div_by_3:
    print(f"{num} is divisible by 3 only")
else:
    print(f"{num} is not divisible by 2 or 3")
