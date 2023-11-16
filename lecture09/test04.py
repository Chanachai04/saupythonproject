class DtiTest05 :
    infoA = 10
    infoB = 20

    def _init_(self,infoC,infoD) :
        self.infoC = infoC
        self.__infoD = infoD

    def setInfoD(self,infoD):
        self.__infoD = infoD

    def getInfoD(self):
        return self.__infoD 

    def showInfo(self):
        print(self.infoA,end='')
        print(self.infoB,end='')   
        print(self.infoC,end='')   
        print(self.__infoD,end='')
        print('---------------------------------------------------------------')              

obj1 = DtiTest05(30,40)
obj2 = DtiTest05(30,100)
obj1.showInfo() 
obj1.infoA = 555
obj1.setinfoB(999) 
obj1.showInfo() 
print(obj1.getinfoB()+obj1.getinfoD())