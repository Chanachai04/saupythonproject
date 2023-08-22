# รับค่าขอมูลจากแป้นพิมพ์
emp_name = input("ป้อนชื่อพนักงาน : ")
sale_price = float(input("ป้อนยอดขาย : "))
print("------------")
# แปลง str เป็น number -> int()จำนวนเต็ม float()จำนวนจริงหรือทศนิยม
commission = sale_price * 10 / 100
s = format(float(sale_price),".2f")
c = format(float(commission),".2f")

print(f'คุณ {emp_name} ยอดขาย {sale_price:.2f} บาท ได้ค่าคอม {commission:.2f} บาท')
print("คุณ", emp_name  ,"ยอดขาย",s ,"บาท ได้ค่าคอม",c ,"บาท")
print("คุณ"+ emp_name  +"ยอดขาย"+str(s) +"บาท ได้ค่าคอม"+str(c) +"บาท")
print("คุณ {} ยอดขาย {:.2f} บาท ได้ค่าคอม {:.2f} บาท".format(emp_name,sale_price,commission))

