n=int(input("Enter your number##:"))
if(n%2==0 and n%3==0 and n%5==0 ):
    print("divisible")
elif(n%2==0 and n%3==0):
    print("divisible by 2 and 3")
elif(n%3==0 and n%5==0):
    print("divisible by 3 and 5")
elif(n%5==0 and n%2==0):
    print("divisible by 5 and 2")
elif(n%2==0):
    print("divisible by 2")
elif(n%3==0):
    print("divisible by 3")
elif(n%5==0):
    print("divisible by 5")
else:
    print("not divisible")
