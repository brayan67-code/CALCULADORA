# calculadora.py
# Backend de la calculadora - Oscar
# Funciones: multiplicar y dividir

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b


# ---- Parte que hace que el programa muestre algo al ejecutarlo ----
print("===== CALCULADORA (Oscar) =====")
print("1. Multiplicar")
print("2. Dividir")

opcion = input("Elige una opcion (1 o 2): ")

num1 = float(input("Escribe el Dividendo: "))
num2 = float(input("Escribe el Divisor: "))

if opcion == "1":
    print("Resultado:", multiplicar(num1, num2))
elif opcion == "2":
    print("Resultado:", dividir(num1, num2))
else:
    print("Opcion no valida")