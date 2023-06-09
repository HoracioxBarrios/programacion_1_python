'''
Gimnasio - Listas paralelas
Un gimnasio desea llevar el control de sus miembros. Cada miembro 
tiene un número de identificación, nombre, edad y tipo de membresía 
(por ejemplo, mensual o anual). La información se encuentra almacenada en 
cuatro listas paralelas: una lista con los números de identificación, 
otra lista con los nombres, una lista con las edades y una lista con 
los tipos de membresía.

Escriba un programa que permita a los usuarios realizar las siguientes 
operaciones:


1-Agregar un nuevo miembro: el programa debe pedir al usuario que ingrese el 
número de identificación, nombre, edad y tipo de membresía del nuevo miembro. 
La información debe ser agregada a las listas paralelas.


2-Mostrar toda la información de todos los miembros (número de identificación, 
nombre, edad y tipo de membresía).

3-Actualizar el tipo de membresía de un miembro: el programa debe pedir al 
usuario que ingrese el número de identificación del miembro y el nuevo tipo 
de membresía. El programa debe buscar el número de identificación en la lista 
de números de identificación y actualizar el tipo de membresía correspondiente 
en la lista de tipos de membresía. En caso de no encontrar al miembro informar 
con un mensaje de que el mismo no se encontró

4- Buscar información de un miembro: el programa debe pedir al usuario que ingrese 
el número de identificación del miembro. El programa debe buscar el número de 
identificación en la lista de números de identificación y mostrar el nombre, 
edad y tipo de membresía correspondientes en las listas de nombres, edades y 
tipos de membresía.


5- Calcular el promedio de edad de los miembros: el programa debe recorrer la 
lista de edades y calcular el promedio de edad de los miembros.

6- Buscar el miembro más joven y el más viejo: el programa debe buscar la edad 
máxima y mínima en la lista de edades y mostrar el nombre y número de 
identificación correspondientes en las listas de nombres y números de 
identificación.


El programa debe permitir al usuario realizar estas operaciones tantas veces 
como desee, hasta que decida salir del programa. El programa debe mostrar un 
menú de opciones para que el usuario pueda elegir la operación que desea realizar.

'''


lista_nombres = ["Lili", "Erica", "Federico", "Ricardo", "Pricila"]

lista_edad = [18, 20, 30, 41, 25]

lista_membresia = ["mensual", "mensual", "anual", "anual", "mensual"]

lista_id = ["100", "200", "300", "400", "500"] # id en str

while True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Agregar un nuevo miembro")
    print("2. Mostrar la informacion de todos los miembros")
    print("3. Actualizar el tipo de membresía de un miembro")
    print("4. Buscar información de un miembro")
    print("5. Calcular el promedio de edad de los miembros")
    print("6. Buscar el miembro más joven y el más viejo")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")

    # Opción 1: Agregar un nuevo miembro
    if opcion == "1":
        nombre_ingresado = input("Ingrese nombre ")

        edad_str = input("Ingrese edad ")
        edad_int = int(edad_str)

        membresia = input("Ingrese tipo de membresia. mensual/anual ")

        id_ingresado_str = input("Ingrese numero id ")

        lista_nombres.append(nombre_ingresado)
        lista_edad.append(edad_int)
        lista_membresia.append(membresia)
        lista_id.append(id_ingresado_str)
    
        # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        for indice in range(len(lista_nombres)):
            print("nombre: {0} edad: {1} membresia: {2} n° ID: {3}".format(
                lista_nombres[indice],
                lista_edad[indice],
                lista_membresia[indice],
                lista_id[indice]
            ))

        # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        id_buscado_str = input("Busqueda de Id. Ingrese  Id")
        for indice in range(len(lista_id)):
            if (id_buscado_str == lista_id[indice]):
                # print("indice{0}".format(indice))
                nueva_membresia = input("Actualizar membresia mensual/anual")
                lista_membresia[indice] = nueva_membresia

        # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        id_buscado_str = input("Busqueda de Id. Ingrese  Id")
        for indice in range(len(lista_id)):
            if (id_buscado_str == lista_id[indice]):
                print("nombre {0} edad {1} membresia {2} id {3}".format(
                    lista_nombres[indice], lista_edad[indice],
                    lista_membresia[indice], lista_id[indice]
                ))

        # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        acum_edad = 0 
        for indice in range(len(lista_edad)):
            acum_edad = acum_edad + lista_edad[indice]

        promedio_edades = acum_edad / len(lista_edad)
        
        print("El promedio de edades es: {0}".format(
            promedio_edades))

        # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        flag_edad = True
        for indice in range(len(lista_edad)):
            edad_in_posicion = lista_edad[indice]
            nombre_in_posicion = lista_nombres[indice]
            membresia_in_posicion = lista_membresia[indice]
            id_in_posisicion = lista_id[indice]
            
            if(flag_edad): #Maximos y minimos
                edad_min = edad_in_posicion
                edad_max = edad_in_posicion
                nombre_edad_min = nombre_in_posicion
                nombre_edad_max = nombre_in_posicion
                membresia_edad_min = membresia_in_posicion
                membresia_edad_max = membresia_in_posicion
                id_de_edad_min = id_in_posisicion
                id_de_edad_max = id_in_posisicion
                flag_edad = False
            else:
                if(edad_in_posicion < edad_min):# datos del de menor edad
                    edad_min = edad_in_posicion
                    nombre_edad_min = nombre_in_posicion
                    membresia_edad_min = membresia_in_posicion
                    id_de_edad_min = id_in_posisicion
                    
                if(edad_in_posicion > edad_max):# datos del de mayor edad
                    edad_max = edad_in_posicion
                    nombre_edad_max = nombre_in_posicion
                    membresia_edad_max = membresia_in_posicion
                    id_de_edad_max = id_in_posisicion
        
        print("El mas joven es: {0} su edad es: {1} su membresia: {2} y su ID: {3}".format(
            nombre_edad_min, edad_min, membresia_edad_min, id_de_edad_min))
        
        print("El mas viejo es: {0} su edad es: {1} su membresia: {2} y su ID: {3}".format(
            nombre_edad_max, edad_max, membresia_edad_max, id_de_edad_max))
        
        # Opcion 0: Salir
    elif opcion == "0":
        break
    else:
        print("Opción inválida. Intente de nuevo.")
