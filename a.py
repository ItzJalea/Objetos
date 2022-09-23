class Complejo():
    def __init__(self,real,imaginario):
        self.real = real
        self.imaginario = imaginario
    
    def getreal(self):
        return self.real
    def getimaginario(self):
        return self.imaginario
    def setreal(self,real):
        self.real = real
    def setimg(self,imaginario):
        self.imaginario = imaginario
    
    def suma (self,num):
        real = self.getreal() + num.getreal()
        img = self.getimgaginario() + num.getimaginario()
        return self.Complejo(real,imaginario)
