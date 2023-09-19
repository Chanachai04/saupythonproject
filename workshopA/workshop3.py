def inputNameProduct():
    return input('ชื่อสินค้า : ')
    
def inputPriceProduct():
    return float(input('ราคาสินค้า : '))
    
def showScoreStudent(nameProduct,priceProduct):
    vatProduct = priceProduct * (7/100)
    print(f'ชื่อสินค้า : {nameProduct} ราคาสินค้า: {priceProduct} ราคาภาษีของสินค้า : {vatProduct:.2f}')

nameProduct = inputNameProduct()
priceProduct = inputPriceProduct()
showScoreStudent(nameProduct,priceProduct)