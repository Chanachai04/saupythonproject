# OOP
class DtiSau:
    # data/property member ค่าข้อมูล
    stu_name = ''
    score = 0
    gpa = 0

    # method member คือการทำงาน(เขียนแบบฟังก์ชัน เพียงแต่ว่ามันอยู่ใน class เท่านั้นเอง)
    def hiStudent(self):
        print(f'สวัสดี {self.stu_name}')

    def showScoreAndGPA(self):
        print(f'คะแนน {self.score} ได้ GPA: {self.gpa}')

# สร้าง object
obj01 = DtiSau() # ชื่อคลาสที่มี ( ) เราเรียกว่าเป็นการสั่งให้ constructor ของคลาสทำงาน
obj02 = DtiSau()

obj01.stu_name = 'สมชาย'
obj01.hiStudent()
obj02.stu_name = 'สมหญิง'
obj02.score = 99
obj02.gpa = 3.99



























