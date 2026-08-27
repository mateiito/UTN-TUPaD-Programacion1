#EJERCICIO 1:  Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

edad = int(input("Escribí tu edad: "))
if edad >= 18:                   #"if" evalúa el valor que el usuario ingresa, si es mayor o igual a 18, se imprime el mensaje "Es mayor de edad"
    print("Es mayor de edad")
else:                            #De lo contrario se imprime "No es mayor de edad".
    print("No es mayor de edad")

#EJERCICIO 2: Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”. 

nota = float(input("Escribí tu nota: "))
if nota >= 6:                   #"if" evalúa el valor que el usuario ingresa, si es mayor o igual a 6, se imprime el mensaje "Aprobado"
    print("Aprobado")
else:                            #"else" evalúa el valor que el usuario ingresa, si es menor a 6, se imprime el mensaje "Desaprobado"
    print("Desaprobado")

#EJERCICIO 3: Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".

numero = int(input("Escribí un número: "))
if numero % 2 == 0:             #"if" evalúa el valor que el usuario ingresa, si es par, se imprime el mensaje "Ha ingresado un número par"
    print("Ha ingresado un número par")
else:                           #De lo contrario, se imprime "Por favor, ingrese un número par".
    print("Por favor, ingrese un número par")

#EJERCICIO 4:  Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años. 

edad = int(input("Escribí tu edad: "))
if edad < 12:                   #"if" evalúa el valor que el usuario ingresa, si es menor a 12, se imprime el mensaje "Niño/a"
    print("Niño/a")
elif edad < 18 and edad >= 12:     #"elif" evalúa el valor que el usuario ingresa, si es mayor o igual a 12 y menor a 18, se imprime el mensaje "Adolescente"           
    print("Adolescente")           
elif edad < 30 and edad >= 18:     #"elif" evalúa el valor que el usuario ingresa, si es mayor o igual a 18 y menor a 30, se imprime el mensaje "Adulto/a joven"
    print("Adulto/a joven")
elif edad >= 30:                              #"elif" evalúa el valor que el usuario ingresa, si es mayor o igual a 30, se imprime el mensaje "Adulto/a"
    print("Adulto/a")   

#EJERCICIO 5: Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 

contraseña = input("Escribí tu contraseña: ")
if 8 <= len(contraseña) <= 14:                            #"len" evalúa la longitud de la contraseña ingresada por el usuario
    print("Ha ingresado una contraseña correcta")         #si es mayor o igual a 8 y menor o igual a 14, se imprime el mensaje "Ha ingresado una contraseña correcta"
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#EJERCICIO 6: Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo.

import random
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]  #Se genera una lista de 100 números aleatorios entre 1 y 100.
from statistics import mode, median, mean
mean = mean(numeros_aleatorios)  #Se calcula la media de la lista.
median = median(numeros_aleatorios)  #Se calcula la mediana de la lista.
mode = mode(numeros_aleatorios)  #Se calcula la moda de la lista.
if mean > median:  #Se compara la media y la mediana para determinar el sesgo.
    print("Sesgo positivo")
elif mean < median:
    print("Sesgo negativo")
else:
    print("No hay sesgo")

#EJERCICIO 7: Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla. 

frase = input("Escribí una frase o palabra: ")
vocales = "aeiouAEIOU"
if frase[-1] in vocales:        #Se evalúa si el último carácter de la frase ingresada por el usuario es una vocal, si es así, se añade un signo de exclamación al final de la frase.
    frase += "!"

print(frase)                    #Se imprime la frase resultante por pantalla.

#EJERCICIO 8:  Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.

nombre = input("Escribí tu nombre: ")
opcion = int(input("Escribí 1 para mayúsculas, 2 para minúsculas o 3 para primera letra mayúscula: "))
if opcion == 1:
    print(nombre.upper())             #"upper" transforma el nombre ingresado por el usuario a mayúsculas y lo imprime por pantalla.
elif opcion == 2:
    print(nombre.lower())             #"lower" transforma el nombre ingresado por el usuario a minúsculas y lo imprime por pantalla.
elif opcion == 3:
    print(nombre.capitalize())        #"capitalize" transforma la primera letra del nombre ingresado por el usuario a mayúscula y lo imprime por pantalla.

#EJERCICIO 9: Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Escribí la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")  
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7: 
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:  
    print("Extremo (puede causar graves daños a gran escala)")

#EJERCICIO 10: Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Escribí en qué hemisferio te encuentras, N para hemisferio norte o S para hemisferio sur: ")
mes = int(input("Escribí el mes (Desde 1 a 12): "))
dia = int(input("Escribí el día: "))

if hemisferio == "S":
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        print("Estás en Verano")
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        print("Estás en Otoño")
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        print("Estás en Invierno")
    elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20):
        print("Estás en Primavera")

elif hemisferio == "N":
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        print("Estás en Invierno")
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        print("Estás en Otoño")
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        print("Estás en Verano")
    elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20):
        print("Estás en Primavera")