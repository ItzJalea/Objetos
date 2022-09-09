class Personal():
    def __init__(self,nombre,cargo,pagoXhora):
        self.nombre = nombre
        self.cargo = cargo
        self.pagoXhora = pagoXhora
    def sueldo(self):
        pass

class Emp_Jornada(Personal):
    def sueldo(self):
        print("Su sueldo es:", self.pagoXhora*40)
class Emp_Planta(Personal):
    def sueldo(self):
        print("Su sueldo es:", self.pagoXhora*168)
class Emp_Contrata(Personal):
    def __init__(self,nombre,cargo,pagoXhora,horasTrabajo):
        self.horasTrabajo = horasTrabajo
        super().__init__(nombre,cargo,pagoXhora)
    def sueldo(self):
        sueldo=self.pagoXhora*self.horasTrabajo
        if(self.horasTrabajo>40):
            sueldo = sueldo+10*sueldo/100
        print("Su sueldo es:", sueldo)

a=Emp_Jornada("marcos","junior",20000)
b=Emp_Planta("Juan","analista",30000)
c=Emp_Contrata("Fernanda","diseñador",15000,30)

a.sueldo()
b.sueldo()
c.sueldo()
