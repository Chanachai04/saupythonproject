# Fuction แบบที่ 2 - Have parameters/No return
# parameters คือ เป็นตัวแปรประเภทหนึ่ง เอาไว้รับค่ามาใช้เฉพาะในฟังชันนั้นๆ เท่านั้น
def funcA(x, y):
    print("AAA")
    z = x + y
    print(f"{x} + {y} = {z}")
    # ไม่มีคำสั่ง return


def funcB(x, y, z):
    print(f"{x:.2f} {y:.4f} {z:.6f}")


funcA(10, 20)  # ข้อมูลที่ส่งให้ parameter เรียก argument
funcB(10, 5, 7)
