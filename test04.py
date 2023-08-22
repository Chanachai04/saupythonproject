people = int(input("จำนวนคน : "))
money = float(input("จำนวนเงิน : "))

result = float(money / people)
a = format(float(result), ".2f")
print(f"จำนวนคน {people} หารคนละ {result:.2f} บาท ")
print("จำนวนคน", people, "หารคนละ", a, "บาท")
print("จำนวนคน" + " " + str(people) + " " + "หารคนละ" + " " + str(a) + " " + "บาท")
print("จำนวนคน {} หารคนละ {:.2f} บาท".format(people, result))
