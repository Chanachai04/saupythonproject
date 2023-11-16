class DtiTest03 :
    infoA = 10

    # contructor
    def _init_(self,infoB,infoC):
        self.infoB = infoB
        self.infoC = infoC
        print('wow wow wow')


    # method
    def showMixandinfo(self,mix) :
        print( self.infoA + self.infoB + self.infoC + mix )

# object
sau1 = DtiTest03(20,20)
sau2 = DtiTest03(10,100)
sau3 = DtiTest03(20,30)