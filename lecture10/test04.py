# เขียนข้อมูลลงไฟล์
# เปิดไฟล์เพื่อเขียนข้อมูลลงไฟลื
f_dti = open("myfile03.txt","a",encoding="utf-8")# เปิดไฟล์เพื่อเขียนข้อมูลลงไฟล์
f_dti.write("aaaaa.....\n")
f_dti.write("bbbbb\n")
f_dti.write("สวัสดีทุกคน...\n")
f_dti.write("ง่วงมากครับทุกคน...\n")

f_dti.close()
print('บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว.....')