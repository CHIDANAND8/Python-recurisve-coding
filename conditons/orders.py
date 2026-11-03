orders = ['order1', 'order2', 'order3', 'order4', 'order5']
user = input("enter your order: ")
price = int(input("enter price: "))
coupon = input("you have coupon or not (yes/no): ")

if user in orders:
    if price >= 500:
        if coupon in ('yes', 'y', '1'):
            discount = price * 0.1
            print(f"discount={discount}")
        else:
            print(f"no discount for you")
    else:
        print("no discount for you")
else:
    print("your order is not ready, please try again")
