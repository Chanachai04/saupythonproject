def inputScoreStudent():
    idStudent = int(input('รหัสนักเรียน : '))
    nameStudent = input('ชื่อนักเรียน : ')
    score1 = float(input('คะแนนนักเรียนครั้งที่1 :'))
    score2 = float(input('คะแนนนักเรียนครั้งที่2 :'))
    score3 = float(input('คะแนนนักเรียนครั้งที่3 :'))
    return idStudent,nameStudent,score1,score2,score3

def calScoreStudent(score1,score2,score3):
    return (score1+score2+score3)/3
    

def showScoreStudent(idStudent,nameStudent,avgScore):
    print(f'รหัสนักเรียน : {idStudent} ชื่อนักเรียน : {nameStudent} คะแนนเฉลี่ยของนักเรียน : {avgScore}')

idStudent,nameStudent,score1,score2,score3 = inputScoreStudent()
avgScore = calScoreStudent(score1,score2,score3)
showScoreStudent(idStudent,nameStudent,avgScore)