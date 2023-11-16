class DtiTest01 :
    pass

class DtiTest02 :
    #data atribute property field
    infoA = ''
    infoB = 20
    
    # method function
    def showHi(self) :
        print('Hi....')

    def showinfoAandB(self)  :
        print(self.infoA)
        print(self.infoB) 

#object 
objA = DtiTest02()   
objB = DtiTest02()   
sombat = DtiTest02()

objA.infoA = 'xxx'
objB.infoB = 100
print(objA.infoB + objB.infoB)
sombat.showinfoAandB()