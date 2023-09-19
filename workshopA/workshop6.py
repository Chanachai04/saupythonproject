def inputInterest():
    name = input('ชื่อผู้กู้ : ')
    money = float(input('จำนวนเงินกู้ : '))
    return name,money
def calInterest(money):
    if money > 1000:
        m = money* 2.5
    else:
        m = money*5.5
    return m
def showInterest(name,money):
    print(f'ชื่อผู้กู้ : {name} อัตราดอกเบี้ยเงินกู้ที่คำนวณได้ : {money}')

name,money = inputInterest()
m = calInterest(money)
showInterest(name,m)