def inputStudentYear():
    return int(input('ปีการศึกษา : '))
    

def checkStudentYear(studentYear):
    if studentYear == 66:
        return 'Welcome Freshman'
    elif studentYear == 65:
        return 'Welcome Sophomore'
    elif studentYear == 64:
        return 'Welcome Junior'

def showStudentYear(year,studentYear):
    print(f'ปีการศึกษา : {year} : {studentYear}')

studentYear = inputStudentYear()
checkYear = checkStudentYear(studentYear)
showStudentYear(studentYear,checkYear)