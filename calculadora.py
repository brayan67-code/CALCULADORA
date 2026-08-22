

# calculadora.py
# Backend de la calculadora 
# Calculadora en equipo - Brayan, Santiago y Oscar

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

def restar(numero1, numero2):
    return numero1 - numero2

def sumar(a, b):
    return a + b

def potencia(a, b):
    return a ** b


# ---- Parte que hace que el programa muestre algo al ejecutarlo ----
print("===== CALCULADORA (Oscar) =====")
print("1. Multiplicar")
print("2. Dividir")
print("3. Restar")
print("4. Sumar")

opcion = input("Elige una opcion (1, 2, 3 y 4): ")

num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))

if opcion == "1":
    print("Resultado:", multiplicar(num1, num2))
elif opcion == "2":
    print("Resultado:", dividir(num1, num2))
elif opcion == "3" :
    print("Resultado:", restar(num1, num2))
elif opcion == "4":
    print("Resultado:", sumar(num1, num2))
elif opcion == "5":
    print("Resultado:", potencia(num1, num2))
else:
    print("Opcion no valida")



