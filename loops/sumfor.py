n=int(input("enter a value"))
temp=n
sum=0
length=len(str(n))
for i in range(1,length+1):
    rem=n%10
    sum+=rem
    n//=10
print(sum)

