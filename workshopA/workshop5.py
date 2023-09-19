def inputEmployee():
    idEmp = int(input('รหัสพนักงาน : '))
    nameEmp = input('ชื่อพนักงาน : ')
    salaryEmp = float(input('เงินเดือนพนักงาน : '))
    return idEmp, nameEmp, salaryEmp

def calSalaryEmployee(salaryEmp):
    salary = salaryEmp-(salaryEmp*7/100)-500
    return salary
def showSalaryEmployee(idEmp,nameEmp,salaryEmp,salary):
    print(f'รหัสพนักงาน : {idEmp} ชื่อพนักงาน : {nameEmp} เงินเดือนปกติ:{salaryEmp} เงินเดือนสุทธิ : {salary}')

idEmp, nameEmp, salaryEmp = inputEmployee()
salary = calSalaryEmployee(salaryEmp)
showSalaryEmployee(idEmp,nameEmp,salaryEmp,salary)
