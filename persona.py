class Persona:
    contador_personas = 0

    def __init__(self, nombre, genero, edad, direccion):
        self._nombre = nombre
        self._genero = genero
        self._edad = edad
        self._direccion = direccion

        Persona.contador_personas += 1

    def obtener_nombre(self):
        return self._nombre

    def obtener_genero(self):
        return self._genero

    def obtener_edad(self):
        return self._edad

    def obtener_direccion(self):
        return self._direccion

    def mostrar_datos(self):
        print(f"Nombre: {self._nombre}")
        print(f"Género: {self._genero}")
        print(f"Edad: {self._edad}")
        print(f"Dirección: {self._direccion}")

persona1 = Persona("daiela", "Femenino", 19, "lomas de la florida")
persona2 = Persona("luis", "Masculino", 25, "guayaquil")
persona2 = Persona("alberto", "Masculino", 18, "Entrada de la 8")
persona1 = Persona("cristhian", "Femenino", 21, "cerecita")

persona1.mostrar_datos()
persona2.mostrar_datos()

print(f"Total de personas creadas: {Persona.contador_personas}")