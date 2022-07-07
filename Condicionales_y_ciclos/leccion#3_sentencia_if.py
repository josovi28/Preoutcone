# La sentencia condicional en Python (al igual que en muchos otros lenguajes de programación)
# es if. En su escritura debemos añadir una expresión de comparación terminando con
# dos puntos al final de la línea. Veamos un ejemplo:

# # temperatura=40
# # if temperatura > 35:
# #     print("Alta temperatura")

# En el caso anterior se puede ver claramente que la condición se cumple y por tanto se ejecuta
# la instrucción que tenemos dentro del cuerpo de la condición. Pero podría no ser así. Para
# controlar ese caso existe la sentencia else. Veamos el mismo ejemplo anterior pero añadiendo
# esta variante:

# # temperature = 20
# # if temperature > 35:
# #     print("Alta temperatura")
# # else:
# #     print("	Parámetros normales	")

# Podríamos tener incluso condiciones dentro de condiciones, lo que se viene a llamar
# técnicamente condiciones anidadas3
# . Veamos un ejemplo ampliando el caso anterior:

# # temperature = 38
# # if temperature < 20:
# #     if temperature < 10:
# #         print(	"Nivel azul"	)
# #     else:
# #         print(	"Nivel verde"	)
# # else:
# #     if temperature < 30:
# #         print(	"Nivel naranja"	)
# #     else:
# #         print(	"Nivel rojo"	)

# Python nos ofrece una mejora en la escritura de condiciones anidadas cuando aparecen
# consecutivamente un else y un if. Podemos sustituirlos por la sentencia elif:

# # temperature = 28
# # if temperature < 20:
# #     if temperature < 10:
# #         print(	"Nivel azul"	)
# #     else:
# #         print(	"Nivel verde"	)
# # elif temperature < 30:
# #     print(	"Nivel naranja"	)
# # else:
# #     print(	"Nivel rojo"	)