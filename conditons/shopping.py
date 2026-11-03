total = int(input("Enter your product range: "))
if total >= 12000:
    print("you grabed 20% off on this shopping, have a great day ahead")
if total >= 7999:
    print("you grabed 12% off on this shopping, have a great day ahead")
elif total >= 5000:
    print("you grabed 5% off on this shopping, have a great day ahead")
elif total < 5000 and total > 0:
    print("you have to shop for 5000 more to grab discount")
else:
    print("Invalid amount")

print("Thanks for shopping")


        
