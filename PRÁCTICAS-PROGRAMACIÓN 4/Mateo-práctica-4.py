#EJERCICIO 1: Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for i in range(101):
    print(i)

#EJERCICIO 2:Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

num = int(input("Por favor, ingresa un número entero: "))
cantidad_digitos = len(str(abs(num)))            #Convertimos el número a cadena y usamos la funcion "len"
print("La cantidad de dígitos es:", cantidad_digitos)

#EJERCICIO 3:Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores. 

num1 = int(input("Por favor, ingresa el primer número: "))
num2 = int(input("Por favor, ingresa el segundo número: "))
suma = 0
for i in range(num1 + 1, num2):
    suma += i
print("La suma de los números comprendidos entre", num1, "y", num2, "es:", suma)

#EJERCICIO 4: Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. 

total = 0
while True:
    num = int(input("Por favor, ingresa un número entero (ingresa 0 para finalizar): "))
    if num == 0:
        break
    total += num
print("El total acumulado es:", total) 

#EJERCICIO 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numero_secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_secreto:
        print("¡Acertaste! El número era", numero_secreto)
        print("Necesitaste", intentos, "intentos para acertar.")
        break
    else:
        print("No acertaste. Inténtalo de nuevo.")

#EJERCICIO 6: Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i)

#EJERCICIO 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario. 

num = int(input("Por favor, ingresa un número entero positivo: "))
suma = 0
for i in range(num + 1):
    suma += i
print("La suma de los números comprendidos entre 0 y", num, "es:", suma)

#EJERCICIO 8: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. 

pares = 0
impares = 0
negativos = 0
positivos = 0

for _ in range(100):
    num = int(input("Por favor, ingresa un número entero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num < 0:
        negativos += 1
    else:
        positivos += 1

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números negativos:", negativos)
print("Cantidad de números positivos:", positivos)

#EJERCICIO 9:  Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.

suma = 0
for _ in range(100):
    num = int(input("Por favor, ingresa un número entero: "))
    suma += num
media = suma / 100
print("La media de los números ingresados es:", media)

#EJERCICIO 10: Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario.

num = int(input("Por favor, ingresa un número entero: "))
if num < 0:
    num_str = str(-num)  # Convertimos el número a cadena y eliminamos el signo negativo
    num_invertido = int(num_str[::-1])  # Invertimos la cadena y la convertimos a entero
    print("El número invertido es:", -num_invertido)  # Mostramos el número invertido con el signo negativo
else:
    num_str = str(num)
    num_invertido = int(num_str[::-1])
    print("El número invertido es:", num_invertido)