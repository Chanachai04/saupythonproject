def inputNumUser():
    numScore = int(input('กรอกตัวเลข : '))
    return numScore

def checkNumUser(numScore):
    if numScore == 25:
        print('Correct,You are the winner')
    else:
        print('Not Correct !!!!')    
            
def showAnswer(answer):
    return answer

numScore = inputNumUser()
answer = checkNumUser(numScore)
showAnswer(answer)