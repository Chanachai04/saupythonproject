# dtiworkshop01.py
print('Calculate Triangle Area U_U')

def inputVaseHigh():
    base = float(input('ป้อนฐาน :'))
    hight = float(input('ป้อนสูง :'))
    return base, hight

def calandShowTriangkeArea(base, hight):
    area = (base*hight)/2
    print(
        f'สามเหลี่ยมฐาน : {base:.2f} สูง : {hight:.2f} มีพื้นที่ : {area:.2f}')

base, hight = inputVaseHigh()
calandShowTriangkeArea(base, hight)
