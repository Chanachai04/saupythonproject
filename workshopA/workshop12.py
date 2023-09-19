def inputGroupTour():
    nameLeader = input("ชื่อหัวหน้ากรุ๊ป : ")
    groupLeaderContact  = input("เบอร์โทรศัพท์ติดต่อหัวหน้ากรุ๊ปทัวร์ : ")
    countGroupTour = int(input("จำนวนคนที่ไปทัวร์: "))
    return nameLeader, groupLeaderContact, countGroupTour

def checkGroupTour(countGroupTour) :
    if countGroupTour == 1 or countGroupTour ==2 :
        package = countGroupTour * 300
    elif countGroupTour == 3 or countGroupTour <= 5 :
        package = countGroupTour * 250
    elif countGroupTour == 6 or countGroupTour <=10 :
        package = countGroupTour * 210
    else :
        package = countGroupTour * 150
    avg = package/countGroupTour
    return package,avg

def showGroupTour(nameLeader, groupLeaderContact, countGroupTour,package,avg):
    print(f"ชื่อหัวหน้ากรุ๊ป : {nameLeader} เบอร์โทรศัพท์ติดต่อ : {groupLeaderContact} จำนวนคนที่ไปทัวร์ : {countGroupTour} แพ็คเก็จ {package} บาท ค่าเฉลี่ย {avg} ต่อคน")

nameLeader, groupLeaderContact, countGroupTour = inputGroupTour()
package,avg = checkGroupTour(countGroupTour)
showGroupTour(nameLeader, groupLeaderContact, countGroupTour,package,avg)