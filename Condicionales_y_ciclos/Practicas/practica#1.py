#Escriba un programa que solicite una contraseña y la vuelva a solicitar hasta que las dos contraseñas coincidan, con un límite de tres peticiones.
Intentos=3
while Intentos!=0:
    contraseña=str(input("Ingrese su contraseña:"))
    confirmacion=str(input("Confirmar contraseña:"))
    Intentos-=1

    if contraseña==confirmacion:
     print("Bien PAH")
     
     break
    print(f'{Intentos} intentos PAH')
else:
     print(f'MAMO PAH')
