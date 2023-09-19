def inputTelephone():
    user = input('ขื่อผู้ใข้โทรศัพท์ : ')
    tel = int(input('เบอร์โทรศัพท์ : '))
    timeMinute = int(input('จำนวนนาที : '))
    return user,tel,timeMinute

def checkTelephoneBill(timeMinute):
    if timeMinute == 1 & timeMinute <= 15:
        return timeMinute * 5
    elif timeMinute == 16 & timeMinute <=30:
        return timeMinute * 3
    else:
        return timeMinute * 1.5

def showTelephone( user,tel,timeMinute,service):
    print(f'ชื่อผู้ใช้ : {user} เบอร์ : {tel} จำนวนนาที : {timeMinute} ค่าบริการ : {service}')

user,tel,timeMinute = inputTelephone()
service = checkTelephoneBill(timeMinute)
showTelephone( user,tel,timeMinute,service)

