#2. Realizar un programa que tenga una clase producto el cual solo tiene los atributos de nombre y codigo
# el codigo tiene la siguiente estructura PAIS-LOTE-AÑO ejemplo:PERU-00001-2024 crear un metodo que imprima el objeto de forma 
# literal (__str__) y que permita identificar el pais de origen y nro de lote

class Producto:
    nombre: None
    pais: None
    registro: None
    anio: None
    codigo: None
    
    def __init__(self, nombre, pais, registro, anio):
        self.nombre = nombre
        self.pais = pais
        self.anio = anio
        self.registro = registro
        self.codigo = self.generar_codigo()
        

    def generar_codigo(self):
        paisr = self.pais.upper()
        return f"{paisr}-{self.registro:05d}-{self.anio}"
    
    def __str__(self):
        return f"Nombre: { self.nombre}, Código: {self.codigo}, Pais: {self.pais}, Lote: {self.registro:05d}"


producto1 = Producto("Gasolina", "Peru", 1, "2020")

print(producto1)