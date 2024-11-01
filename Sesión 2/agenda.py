agenda = {}

def agregar_contacto(nombre, telefono, correo):
    if nombre in agenda:
        print(f'El contacto {nombre} ya existe')
    else: 
        agenda[nombre] = (telefono, correo)
        print(f'El contacto {nombre} fué agregado con éxito')

def buscar_contacto(nombre):
    if nombre in agenda:
        telefono, correo = agenda[nombre]
        print(f'\nNombre: {nombre}\nTeléfono: {telefono}\nCorreo: {correo}')
    else:
        print(f'El nombre {nombre} no existe en tu agenda')

def mostrar_contactos():
    if agenda:
        for nombre, (telefono, correo) in agenda.items():
            print(f'\nNombre: {nombre}\nTeléfono: {telefono}\nCorreo: {correo}')
    else:
        print('La agenda está vacía')

def menu():
    while True:
        print("\nAgenda de contactos")
        print("\t1. Agregar contacto")
        print("\t2. Buscar contacto")
        print("\t3. Mostar todos los contactos")
        print("\t4. Salir")
        opcion = input('\tElige una opción: ')

        if opcion == "1":
            print("\nFormulario para añadir un contacto")
            nombre = input('Escribe el nombre: ')
            telefono = input('Escribe su teléfono: ')
            correo = input('Escribe el correo: ')
            agregar_contacto(nombre, telefono, correo)

        elif opcion == "2":
            print("\nBúsqueda de contacto")
            nombre = input('escribe el nombre del contacto a buscar: ')
            buscar_contacto(nombre)

        elif opcion == "3":
            print("\nListado de contactos:")
            mostrar_contactos()

        elif opcion == "4":
            print("Gracias por usar la mejor agenda del universo")
            break
        else:
            print("Opción inválida, intentalo de nuevo")

menu()