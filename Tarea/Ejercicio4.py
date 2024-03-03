#4. crear un archivo nuevo y realizar una funcion que permita dividir 2 numeros, importar esta funcion
# ponerlo en un bucle while True , y al ser llamada la importacion ponerlo dentro de un try except 
# ejecutar la funcion hasta que realice correctamente la division luego de eso romper el bucle

from operaciones import dividir

while True:
    try:
        num1 = float(input("Ingrese primer numero: "))
        num2 = float(input("Ingrese segundo numero: "))
        
        resultado = dividir(num1,num2)
        print(f"Resultado es {resultado}")
        break
    
    except Exception as e:
        print(e)