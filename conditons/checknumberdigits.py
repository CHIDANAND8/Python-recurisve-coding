n=int(input("enter your number:"))
if(n<10):
    print("single digit number")
elif(n<100):
    print("two digit number")
elif(n<1000):
    print("three digit number")
else:
    print("four digit number")