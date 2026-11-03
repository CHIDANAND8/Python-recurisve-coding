
# Program to check if a triangle is valid and find its type

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

# Triangle is valid only if sum of any two sides is greater than the third side
if (a + b > c) and (b + c > a) and (a + c > b):
    print(f"Triangle with sides ({a}, {b}, {c}) is VALID")

    # Check triangle type
    if a == b == c:
        print("It is an EQUILATERAL triangle (all 3 sides are equal)")
    elif a == b or b == c or a == c:
        print("It is an ISOSCELES triangle (2 sides are equal)")
    else:
        print("It is a SCALENE triangle (no sides are equal)")
else:
    print(f"Triangle with sides ({a}, {b}, {c}) is INVALID")
    print("Sum of any two sides must be greater than the third side")
