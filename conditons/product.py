product_list={"pen":10, "book":25, "mobile":10000, "laptop":100000}
product_name=input("enter product name:")

if product_name in product_list:
    product_price = product_list[product_name]
    if(product_price >= 100000):
        discount = 0.10 * product_price
        print(f"discount {discount}")
        print("10% discount")
    elif(product_price >= 10000):
        discount = 0.05 * product_price
        print(f"discount {discount}")
        print("5% discount")
    elif(product_price >= 1000):
        discount = 0.02 * product_price
        print(f"discount {discount}")
        print("2% discount")
    else:
        discount = 0
        print("no discount")
    print(f"final price: {product_price - discount}")
else:
    print("product not found")