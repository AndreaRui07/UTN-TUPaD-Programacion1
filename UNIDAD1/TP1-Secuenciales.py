#EJERCICIO 1

print("Hola mundo")

#EJERCICIO 2

nombre = input("Ingrese su nombre: ")

print(f"Hola {nombre}")

#EJERCICIO 3

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido},tengo {edad} años y vivo en {residencia}")

#EJERCICIO 4

# crear un programa que solicite el radio de un circulo e imprima por pantalla su area y su perimetro

radio = int(input("Ingrese el radio de un circulo: "))

pi = 3.14159

area = pi * radio * radio
perimetro = 2 * pi * radio

print(f"El area del circulo es:{area} y su perimetro es:{perimetro}")

#EJERCICIO 5

#pedir que el usuario ingrese una cantidad de segundos e imprimir su equivalencia en horas

segundos = int(input("Ingrese los segundos que desea convertir: "))

horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas}horas")

#EJERCICIO 6

#pedir un numero al usuario e imprimir su tabla de multiplicar

numero = int(input("Ingrese un numero: "))

for i in range (0,11):
    resultado = numero * i
    print(resultado)

#EJERCICIO 7

numeroA = int(input("Ingrese un numero positivo: "))
numeroB = int(input("Ingrese otro numero positivo: "))

print("La suma de ", numeroA,"y", numeroB, "es:", numeroA + numeroB)
print("La resta de ", numeroA, "menos", numeroB, "es", numeroA - numeroB)
print("El producto entre ", numeroA, "y", numeroB, "es", numeroA * numeroB)
print("La division entre ", numeroA, "y", numeroB, "es", numeroA / numeroB)

#EJERCICIO 8

altura = float(input("Ingrese su altura: "))
peso = int(input("Ingrese su peso: "))

indice_masa_corporal = peso / altura

print(f"Su indice de masa corporal es:{indice_masa_corporal}")

#EJERCICIO 9

temperatura = int(input("Ingrese su temperatura corporal: "))

temp_faren = 9 / 5 * temperatura + 32

print(f"Su temperatura corporal equivale a {temp_faren} grados Fahrenheit")

#EJERCICIO 10

num1 = int(input("Ingrese el primer numero positivo: "))
num2 = int(input("Ingrese el segundo numero positivo: "))
num3 = int(input("Ingrese el tercer numero positivo: "))

promedio = (num1 + num2 + num3) // 3

print(f"El promedio de los numeros ingresados es:{promedio} ")