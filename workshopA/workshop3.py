def inputNameProduct():
    nameProduct = input('ชื่อสินค้า : ')
    return nameProduct
def inputPriceProduct():
    priceProduct = float(input('ราคาสินค้า : '))
    return priceProduct
def showScoreStudent(nameProduct,priceProduct):
    vatProduct = priceProduct * (7/100)
    print(f'ชื่อสินค้า : {nameProduct} ราคาสินค้า: {priceProduct} ราคาภาษีของสินค้า : {vatProduct:.2f}')

nameProduct = inputNameProduct()
priceProduct = inputPriceProduct()
showScoreStudent(nameProduct,priceProduct)