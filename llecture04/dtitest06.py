name = input("ชื่อสินค้า : ")
price = float(input("ราคาสินค้า(ต้นทุน) : "))
total_price = price + (price * 10 / 100)
print(f"ชื่อสินค้า {name} ราคาต้นทุน {price} ราคาขายสินค้า {total_price}")
