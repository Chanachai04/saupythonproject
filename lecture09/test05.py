class Sau01 :
    infoA = 10

    def showHi():
        print('Hi.....')

class Sau02(Sau01) :
    infoB = 20 
    
    def showHey() :
        print('Hey....')

    def showHi():
        print('Hi Hi Hi.....')


ob1 = Sau01()
ob2 = Sau02()
ob2.showHi()