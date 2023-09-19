def inputEquationX():
    return int(input('กรอกค่าสมการ x : '))

def calEquation(x):
    return 2 * x ** 2 + 2 * x + 1

def showEquation(x, y):
    print(f'ค่าสมการของ x : {x} คำนวณออกมาได้ : {y}')

x = inputEquationX()
y = calEquation(x)
showEquation(x, y)
