# เชื่อมข้อมูลหลาย ประเภทเข้าด้วยดัน
# ใช้ ,
score = 500
print("Hello...", 20, True, 6434.534, 10/2, "Hi....", score)

# ใช้ +
print("Hello..." + str(20) + str(True) + str(6434.534) + str(10/2) + "Hi...." + str(score))

# ใช้ เมธอด format 
print("Hello... {} {} {} {} Hi.... {}".format(20, True, 6434.534, 10/2,score))

# ใช้ f-string
print(f"Hello... {20} {True} {6434.534} {10/2} Hi.... {score}")

# ใช้ modular operator %
print('Hello... %d %f Hi...'%(20, 17.5))
