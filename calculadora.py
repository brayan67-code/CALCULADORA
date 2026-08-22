

# calculadora.py
# Backend de la calculadora - Oscar
# Funciones: multiplicar y dividir

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

def restar(numero1, numero2):
    return numero1 - numero2


# ---- Parte que hace que el programa muestre algo al ejecutarlo ----
print("===== CALCULADORA (Oscar) =====")
print("1. Multiplicar")
print("2. Dividir")
print("3. Resta")

opcion = input("Elige una opcion (1, 2, y 3): ")

num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))

if opcion == "1":
    print("Resultado:", multiplicar(num1, num2))
elif opcion == "2":
    print("Resultado:", dividir(num1, num2))
elif opcion == "3" :
    print("Resultado:", restar(num1, num2))
else:
    print("Opcion no valida")


sumando1 = int(input("Ingrese el primer número: "))
sumando2 = int(input("Ingrese el segundo número: "))

suma = sumando1 + sumando2

print("La suma es:", suma)

