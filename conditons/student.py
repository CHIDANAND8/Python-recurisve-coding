
student=input("Enter your name:")
maths=int(input("Enter your marks"))
social=int(input("Enter your social marks"))
science=int(input("Enter your science marks"))
hindi=int(input("Enter your hindi marks"))
english=int(input("Enter your english marks"))

n=int(input("enter total percentage"))
total=(maths+social+science+hindi+english)/5
if(n>90):
    print("Grade A")
elif(n>80):
    print("Grade B")
elif(n>70):
    print("Grade C")
elif(n>60):
    print("Grade D")
else:
    print("Grade F")

