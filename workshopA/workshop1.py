def inputPriceAndProduct():
    product = input('ชื่อสินค้า : ')
    price = float(input('ราคาสินค้า : '))
    return product,price
def calPriceProduct(price):
    priceProduct = price + (price *10/100)
    return priceProduct
def showPriceProduct(product,priceProduct):
    print(f'ชื่อสินค้า {product} ราคาขายสินค้า {priceProduct} ')

product,price = inputPriceAndProduct()
priceProduct = calPriceProduct(price)
showPriceProduct(product,priceProduct)