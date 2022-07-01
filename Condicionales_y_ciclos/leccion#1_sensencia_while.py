#Hacer las tablas de la escuela
tabladesiada=int(input("Digite un numero de tabla que desea: "))
contador=11
while contador!=0:
    contador-=1
    print(f"{tabladesiada}x{contador}={tabladesiada*contador}")
else:
    print("Fin de la tabla")