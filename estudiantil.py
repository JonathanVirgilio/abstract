from abc import ABC, abstractmethod
class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, genero,peso):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.peso = peso

    @abstractmethod
    def datos():
        pass

class Virgilio(Persona):
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def datos(self):
        return'El nombre de la persona es {}, de una edad de {} y su genero es {}'.format(self.nombre,self.edad,self.genero)

class Dueño(Persona):
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    
    def datos(self):
        return'El nombre del gato es {}, tiene {} meses y su genero es {}'.format(self.nombre,self.edad,self.genero)

class Hijo(Persona):
    def __init__(self, nombrePadre, nomHijo):
        self. nombrePadre = nombrePadre
        self.nomHijo = nomHijo

    def datos(self):
        return'{} es el padre del alumno {}'.format(self.nombrePadre, self.nomHijo)
    
virgi = Virgilio('Virgilio', 21, 'Masculino')
dueñito = Dueño('Rocky', 4, 'masculino')
hijito = Hijo('Rene', 'Jonathan')
print(virgi.datos())
print(dueñito.datos())
print(hijito.datos())