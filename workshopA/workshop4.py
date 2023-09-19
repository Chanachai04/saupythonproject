import math

def inputEquationX():
    x = int(input('กรอกค่าสมการ x : '))
    return x

def calEquation(x):
    y = 2*math.pow(x, 2)+2*x+1
    return y
def showEquation(x,y):
    print(f'ค่าสมการของ x : {x} คำนวณออกมาได้ : {y}')

x = inputEquationX()
y = calEquation(x)
showEquation(x,y)
    
