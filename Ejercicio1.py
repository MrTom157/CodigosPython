NombresUsu=[]
SexoUsu=[]
ContraseñasUsu=[]

def validarUsuario(sexo):
    if sexo!="M" and sexo!="F":
        print("Valor incorrecto, solo (M-F)")
        return False
    else:
        return True

def validarContraseña(contraseña):
    contadorLetras=0
    contadorNumeros=0

    for letra in str(contraseña):
        if letra.isnumeric():
            contadorNumeros+=1
        if letra.isalpha():
            contadorLetras+=1
    
    if len(contraseña)<8:
        print("Su contraseña debe ser minimo 8 caracteres")
        return False
    elif contadorLetras<1:
        print("Almenos debe tener 1 letra")
        return False
    elif contadorNumeros<1:
        print("Almenos debe tener 1 numero")
        return False
    else:
        return True

while True:
    print("Bienvenido al menu de usuarios, seleccione su opcion:\n1- Ingresar Usuario\n2- Buscar usuario\n3- Eliminar Usuario\n4- Salir")
    try:
        opcion=int(input())
    except ValueError:
        print("Solo opciones numericas, desde 1 hasta 4")
        continue
    
    match opcion:
        case 1:
            while True:
                nombreUsuario=input("Ingrese su nombre: ")
                sexo=input("Ingrese su sexo (M-F): ").upper()
                if validarUsuario(sexo)==False:
                    continue
                contraseña=input("Ingrese su contraseña. Debe tener 8 caracteres minimo y almenos 1 letra y 1 numero: ")
                if validarContraseña(contraseña)==True:
                    print("Usuario ingresado correctamente. ")
                    NombresUsu.append(nombreUsuario)
                    SexoUsu.append(sexo)
                    ContraseñasUsu.append(contraseña)

                    break
                else:    
                    print("Datos incorrectos, intente denuevo. ")
        case 2:
            print("Escriba el nombre de quien quiera buscar en la lista: ")
            buscarusuario=input()
            if buscarusuario in NombresUsu:
                print("Se ha encontrado el usuario: ")
                indice=NombresUsu.index(buscarusuario)
                print(NombresUsu[indice])
                print(SexoUsu[indice])
                print(ContraseñasUsu[indice])
            else:
                print("No se encontro el usuario que esta buscando!")

        case 3:
            print("Escriba el nombre de quien quiera eliminar de la lista: ")
            eliminarusuario=input()
            if eliminarusuario in NombresUsu:
                print("Se ha encontrado el usuario, desea eliminarlo? (Si-No)")
                respuesta=input().upper()
                if respuesta=="SI":
                    indice=NombresUsu.index(eliminarusuario)
                    del NombresUsu[indice]
                    del SexoUsu[indice]
                    del ContraseñasUsu[indice]
            else:
                print("No se pudo Eliminar usuario!")

        case 4:
            print("Saliendo del menu!!!")
            break



