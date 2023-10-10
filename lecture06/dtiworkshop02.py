def inputCarDetail():
    carNo = input('ป้อนทะเบียนรถ : ')
    carWeight = float(input('ป้อนน้ำหนักรถ : '))
    return carNo,carWeight
def checkCarAndShowWeight(carNo,carWeight):
    if carWeight>1000:
        print(f'รถทะเบียน {carNo} น้ำหนักไม่ผ่านเกณฑ์')
    else:
        print(f'รถทะเบียน {carNo} น้ำหนักผ่านเกณฑ์')

carNo,carWeight = inputCarDetail()
checkCarAndShowWeight(carNo,carWeight)