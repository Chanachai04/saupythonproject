# รับค่าข้อมูล
def inputMoneyPerson():
    money = float(input("ป้อนเงิน :"))
    person = int(input("ป้อนคน :"))
    return money, person


# คำนวณ แล้วแสดงออกมา
def calAndShowMoneyShare(money, person):
    m = format(money,".2f")
    print(f"จำนวนเงิน {money:.2f} บาท คน {person} คน แชร์กันคนละ {round(money/person)} บาท")
    print("จำนวนเงิน", m, "บาท คน", person, "คน แชร์กันคนละ", round(money / person),"บาท")
    print("จำนวนเงิน"+" "+ str(m)+ " " + "บาท คน" + " " + str(person) + " " + "คน แชร์กันคนละ" + " " + str(round(money / person))+ " " +"บาท")
    print("จำนวนเงิน {:.2f} บาท คน {} คน แชร์กันคนละ {} บาท".format(money,person,round(money/person)))
    print("จำนวนเงิน %.2f บาท คน %d คน แชร์กันคนละ %d บาท"%(money,person,round(money/person)))


money, person = inputMoneyPerson()
calAndShowMoneyShare(money, person)
