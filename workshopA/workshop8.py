def inputPh():
    province = input('จังหวัด : ')
    ph = int(input('ค่า PH : '))
    return province,ph

def checkPh(ph):
    if ph == 7 or ph == 8:
        return 'Result is Normal'
    elif ph > 8:
        return  'Result is Acid'
    else:
        return 'Result is Alkali'

def showPh(province,ph):
    print(f'จังหวัด : {province} ค่า PH : {ph}')

province,ph = inputPh()
showPh(province,checkPh(ph))

