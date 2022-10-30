class Alumno:
    def __init__(self, Nombre, Nota):
        self.Nombre = Nombre
        self.Nota = Nota

    def aprobar(self):
        if self.Nota > 5:
            return "El alumno aprobó"
        else:
            return "El alumno no aprobó"

    def __str__(self):
         return f"Nombre: {self.Nombre}\nNota: {self.Nota}\n{self.aprobar()}"



Feid = Alumno("Feid", 10)
print(Feid)