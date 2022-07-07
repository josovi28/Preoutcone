# >>La sentencia while
# El primer mecanismo que existe en Python para repetir instrucciones es usar la sentencia
# while. La semántica tras esta sentencia es: «Mientras se cumpla la condición haz algo».
# Veamos un sencillo bucle que muestra por pantalla los números del 1 al 4

# # value = 1
# # while value <= 4:
# #     print(value)
# #     value += 1

# >>Romper un bucle while
# Python ofrece la posibilidad de romper o finalizar un bucle antes de que se cumpla la
# condición de parada. Supongamos un ejemplo en el que estamos buscando el primer número
# múltiplo de 3 yendo desde 20 hasta 1

# # num = 20
# # while num >= 1:
# #     if num % 3 == 0:
# #        print(num)
# #        break
# #     num -= 1

# >>Comprobar la rotura
# Python nos ofrece la posibilidad de detectar si el bucle ha acabado de forma ordinaria,
# esto es, ha finalizado por no cumplirse la condición establecida. Para ello podemos hacer uso
# de la sentencia else como parte del propio bucle. Si el bucle while finaliza normalmente (sin
# llamada a break) el flujo de control pasa a la sentencia opcional else.
# Veamos un ejemplo en el que tratamos de encontrar un múltiplo de 9 en el rango [1, 8] (es
# obvio que no sucederá):

# # num = 8
# # while num >= 1:
# #     if num % 9 == 0:
# #         print('f	{num} is a multiple of 9!	')
# #         break
# #     num -= 1
# # else:
# #      print(	"No multiples of 9 found!	")

# >>Continuar un bucle
# Hay situaciones en las que, en vez de romper un bucle, nos interesa saltar adelante hacia
# la siguiente repetición. Para ello Python nos ofrece la sentencia continue que hace
# precisamente eso, descartar el resto del código del bucle y saltar a la siguiente iteración.
# Veamos un ejemplo en el que usaremos esta estrategia para mostrar todos los números en el
# rango [1, 20] ignorando aquellos que sean múltiplos de 3:

# # num = 21
# # while num >= 1:
# #     num -= 1
# #     if num % 3 == 0:
# #         continue
# #     print(f'{num}') # Evitar salto de línea

#>>Bucle infinito

contador=0
while contador!=-0.5:
    contador+=1
    print(f"{contador}")



