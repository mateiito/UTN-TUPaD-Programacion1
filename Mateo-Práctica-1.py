# EJERCICIO 1:  Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("¡Hola Mundo!") # En esta Línea, el programa imprime en la consola el mensaje: "¡Hola Mundo!" 

# EJERCICIO 2: Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
nombre= input("Ingresa tu nombre: ")
print("¡Hola " + nombre + "!") # En esta línea, el programa imprime el saludo usando el nombre ingresado.

# EJERCICIO 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
nombre=input("Ingresa tu nombre: ")
apellido=input("Ingresa tu apellido: ")    #Se ingresan los datos del usuario pedidos.
edad=input("Ingresa tu edad: ")
lugar_residencia=input("Ingresa tu lugar de residencia: ")
print("¡Hola, soy " + nombre + " " + apellido + " , tengo " + edad + " años y vivo en " + lugar_residencia + "!")  #Se suman los datos ingresados para formar una oración que se imprime por pantalla.

# EJERCICIO 4: Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro. 
radio=float(input("ingresa el radio del círculo:"))
area= 3.14159 * radio ** 2        #Cálculos para el área y perímetro del círculo.
perimetro= 2 * 3.14159 * radio
print(F"el área del círculo es: {area:.2f}")
print(F"el perímetro del círculo es: {perimetro:.2f}")     #Se imprime el áre y perímetro del círculo con dos decimales.

# EJERCICIO 5: Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos=int(input("ingresa la cantidad de segundos: "))
horas= segundos / 3600
print(F"{segundos} segundos equivalen a {horas:.2f} horas") #Se imprime la cantidad de segundos ingresada y su equivalencia en horas con dos decimales.

#EJERCICIO 6: Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dnúmero.  
numero=int(input("Ingresa un número para mostrar su tabla de multiplicar: "))
print(F"Tabla de multiplicar del {numero}:")
print(F"{numero} x 1 = {numero * 1}")
print(F"{numero} x 2 = {numero * 2}")
print(F"{numero} x 3 = {numero * 3}")
print(F"{numero} x 4 = {numero * 4}")
print(F"{numero} x 5 = {numero * 5}")          #Multiplicación del número ingresado por los números del 1 al 10, se imprime cada resultado por pantalla.
print(F"{numero} x 6 = {numero * 6}")
print(F"{numero} x 7 = {numero * 7}")
print(F"{numero} x 8 = {numero * 8}")
print(F"{numero} x 9 = {numero * 9}")
print(F"{numero} x 10 = {numero * 10}")

#EJERCICIO 7: Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 
numero1=int(input("Ingresa el primer número entero distinto de 0: "))
numero2=int(input("Ingresa el segundo número entero distinto de 0: "))
suma= numero1 + numero2
resta= numero1 - numero2
multiplicacion= numero1 * numero2             #Operaciones con los números ingresados.
division= numero1 / numero2
print(F"La suma de {numero1} y {numero2} es: {suma}")
print(F"La resta de {numero1} y {numero2} es: {resta}")
print(F"La multiplicación de {numero1} y {numero2} es: {multiplicacion}")
print(F"La división de {numero1} y {numero2} es: {division:.2f}") #Se imprime el resultado de las operaciones con los números ingresados, la división se muestra con dos decimales. 

#EJERCICIO 8: Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
altura=float(input("Ingresa tu altura en metros: "))
peso=float(input("Ingresa tu peso en kilogramos: "))
indice= peso / (altura ** 2)
print(F"Tu índice de masa corporal es: {indice:.2f}") #Se imprime el índice de masa corporal con dos decimales.

#EJERCICIO 9: Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
celsius=float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit= (celsius * 9/5) + 32
print(F"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}") #Se imprime la temperatura en grados Fahrenheit con dos decimales.

#EJERCICIO 10:Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números.
nro1=float(input("Ingresa el primer número para promediar: "))
nro2=float(input("Ingresa el segundo número para promediar: "))
nro3=float(input("Ingresa el tercer número para promediar: "))
prom= (nro1 + nro2 + nro3) / 3
print(F"El promedio de los números ingresados es: {prom:.2f}") #Se imprime el promedio de los números ingresados con dos decimales.