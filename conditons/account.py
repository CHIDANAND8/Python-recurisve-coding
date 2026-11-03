balance=10000
n=int(input("enter your withdraw amount:"))
if(n>=1000):
    print(f"balance:{balance-n}")
    print("withdraw successful")
elif(n>=500 and n<1000):
    print(f"balance:{balance-n}")
    print("medium withdraw")
else:
    print("insufficient balance")
