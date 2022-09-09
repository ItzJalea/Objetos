class Soldado():
    puntoDeEncuento = [1000,1000]

    def __init__(self,nombre,rango,posicionActual):
        self.nombre = nombre
        self.rango = rango
        self.posicionActual = posicionActual
    def saludar(self):
        print("Hola, mi nombre es:", self.nombre, ", rango:", self.rango)

    def atacar(self):
        print("ataque al enemigo")
    def CPE(self):
        puntoDeEncuentro = [0,0]
        if self.rango != "general":
            print("No tiene el suficiente rango para cambiar el punto de encuentro")
        else:
            puntoDeEncuentro[1] = input(int("Indique las nueva cordenada x"))
            puntoDeEncuentro[2] = input(int("Indique las nueva cordenada y"))

a=Soldado("marcos","general","20000")
b=Soldado("Juan","oficial",30000)
c=Soldado("Fernanda","cabo",15000,30)

a.saludar()
b.CPE()
c.atacar()
