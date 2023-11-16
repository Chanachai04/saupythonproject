# ลบไฟล์
import os
from os import remove

if os.path.exists("myfile02.txt"):
    remove("myfile02.txt")
else:
    print("ไฟล์ที่จะลบไม่มี")