a, b, c = map(int,input("enter your values: ").split())
if(a==b==c):
    print("equilateral")
elif(a+b>c and b+c>a and a+c>b):
    if(a==b or b==c or a==c):
         print("valid triangle")
elif(a==b or b==c or a==c):
    print("isosceles")
else:
    print("scalene")