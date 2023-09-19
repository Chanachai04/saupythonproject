def inputEmployee():
    idEmp = int(input('รหัสพนักงาน : '))
    nameEmp = input('ชื่อพนักงาน : ')
    moneyEmp = float(input('ยอดขายที่ทำได้ : '))
    return idEmp,nameEmp,moneyEmp

def checkEmployee(moneyEmp):
    if moneyEmp >= 1001 or moneyEmp == 2000:
        return moneyEmp * (1 / 100)
    elif moneyEmp >= 2001 or moneyEmp == 3000:
        return moneyEmp * (3 / 100)
    elif moneyEmp > 3000:
        return moneyEmp * (5 / 100)
    else:
        return moneyEmp * 0
    
def showEmployee(idEmp,nameEmp,commission):
    print(f'รหัสพนักงาน : {idEmp} ชื่อพนักงาน : {nameEmp} ค่าคอมมิชชั่น: {commission:.2f}')

idEmp,nameEmp,moneyEmp = inputEmployee()
commission = checkEmployee(moneyEmp)
showEmployee(idEmp,nameEmp,commission)