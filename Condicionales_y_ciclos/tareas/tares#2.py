# Escriba un programa que pregunte una y otra vez si desea 
# continuar con el programa, siempre que se conteste exactamente 
# sí (en minúsculas, mayúsculas y con tilde).
# Pistas:
# a. Condición del if se puede usar conectores para el if por ejemplo and,or,! Ejemplo 
# de uso if nelver<josue AND Josue>David:print(“Josue es mayor”)no

print("Diga SI para continuar")

respuesta = input("¿Desea continuar?: ")

while respuesta != "SI" or "Si" or "si" or "SÍ" or "Sí" or "sí":

        respuesta = input("¿Desea continuar?: ")
        
print("¡Continuamos!")
