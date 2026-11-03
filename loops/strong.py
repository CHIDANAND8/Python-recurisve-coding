num = int(input("Enter a number: "))
temp = num
total = 0

while num > 0:
    rem = num % 10
    
    fact = 1
    i = 1
    while i <= rem:
        fact *= i
        i += 1
        
    total += fact
    num //= 10

if total == temp:
    print(temp, "is a Strong number")
else:
    print(temp, "is not a Strong number")