class DtiTest04 :
    data1 = 10 

    def _init_(self,data2) : 
        self.data2 = data2
        print('Hi....')

    def doTask(self) :
        print(':<<')

    def doTask(self,value) :
        print(value)

    # destructor
    def _del_(self):
        print('Bye')
        
    def showHey():
        print('Hey')

#-------------------------------------------------------

sauA = DtiTest04(20)
sauB = DtiTest04(20)
sauC = DtiTest04(20)

sauC.doTask2('UUUOOHHHHH')
sauC.doTask1()
print(sauA.data1 + sauB.data1)