# อ่านข้อมูลจากไฟล์
f_dti = open("myfile01.txt","r",encoding="utf-8")
try:
    data = f_dti.readline()
    print(data ,end="")
    data = f_dti.readline()
    print(data ,end="")
except Exception:
    print("ติดต่อ Admin 043232234....")
finally:
    f_dti.close()