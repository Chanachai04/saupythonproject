def inputInterest():
    name = input('ชื่อผู้กู้ : ')
    money = float(input('จำนวนเงินกู้ : '))
    return name,money

def calInterest(money):
    if money > 1000:
        return money* (2.5/100)
    else:
        return money* (5.5/100)
    
def showInterest(name,money):
    print(f'ชื่อผู้กู้ : {name} อัตราดอกเบี้ยเงินกู้ที่คำนวณได้ : {money}')

name,money = inputInterest()
showInterest(name,calInterest(money))