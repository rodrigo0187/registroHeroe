import csv
import random
import os
from os import system

listaHeroes = []
head = ["Heroe", "Aparicion", "Popularidad"]

# ruta del archivo
ruta = r'D:\WorkSpace\python\practicaejercicios\csv\registrosHeroes.csv'


def heroes():
    system('cls')
    print('Gestion de Heroes')
    print('1. Agregar heroe')
    print('------------------------------------------------')
    while True:
        nombreHereo = input('Ingrese el nombre del heroe: ').strip().lower()
        try:
            if len(nombreHereo) < 3 or len(nombreHereo) > 20:
                print('el nombre del heroe debe tener entre 3 y 20 caracteres.')
                return False
            else:
                print('El nombre del heroe es valido.')
                break
        except ValueError:
            print('El nombre del heroe debe ser un texto.')

    while True:
        print('----------------------------------------------------------------')
        anoAparicion = int(input('Ingrese el año de aparicion del heroe: '))
        try:
            if anoAparicion < 1900:
                print('el ano del heroe debe ser mayor o igual a 1900.')
                return False
            else:
                print('El ano de aparicion del heroe es valido.')
                break
        except (ValueError, TypeError) as e:
            print(f'Error en la entrada: {e}')

    diccHeroe = {
        "Heroe": nombreHereo,
        "Aparicion": anoAparicion,
        "Popularidad": None
    }

    listaHeroes.append(diccHeroe)

    # valido si existe el archivo en caso contrario, lo creo
    directory = os.path.dirname(ruta)
    os.makedirs(directory, exist_ok=True)

    # se crea el archivo si no existe
    if not os.path.isfile(ruta):
        print('El archivo no existe, creando...')
        print()
        with open(ruta, 'a', newline='') as heroes_csv:
            writer = csv.DictWriter(heroes_csv, fieldnames=head)
            writer.writeheader()
            writer.writerows(listaHeroes)

    #  se agrega el heroe al archivo existente
    with open(ruta, 'a', newline='') as heroes_csv:
        writer = csv.DictWriter(heroes_csv, fieldnames=head)
        writer.writeheader()
        writer.writerows(listaHeroes)

    print('Heroes en la lista')
    for i, heroe in enumerate(listaHeroes, start=1):
        print(f'{i} {heroe} registrado')
    print('------------------------------------------------')
    print('Heroe agregado con exito.')
    enter = input('Presione enter para continuar...')
    print('------------------------------------------------')

    system('cls')


def popularidadHeroes():
    system('cls')
    print('Gestion de Heroes')
    print('2. Agregar popularidad a un heroe')
    print('------------------------------------------------')
    while True:
        if not listaHeroes:
            print('No hay heroes registrados.')
            return False

        print('Heroes en la lista')
        for i, heroe in enumerate(listaHeroes, start=1):
            print(f'{i} {heroe["Heroe"]}')
        try:
            ubicacion = int(
                input(f'Ingrese la posicion del heroe, entre(1, y {len(listaHeroes)}): '))
            if 1 <= ubicacion <= len(listaHeroes):
                superhereo = listaHeroes[ubicacion - 1]
                popularidad = random.randint(1, 10)
                superhereo["Popularidad"] = popularidad
                print(f'El heroe {superhereo["Heroe"]} tiene una popularidad de {
                    popularidad}')

                # actualizacion del archivo
                with open(ruta, 'w', newline='') as heroes_csv:
                    writer = csv.DictWriter(heroes_csv, fieldnames=head)
                    writer.writeheader()
                    writer.writerows(listaHeroes)
                break
            else:
                print('por favor ingrese una posicion valida, entre 1 y',
                      len(listaHeroes))
        except ValueError:
            print('Por favor ingrese un numero valido.')


def mostrarHeroes():
    system('cls')
    ruta = r'D:\\WorkSpace\\python\\practicaejercicios\\csv\\registrosHeroes.csv'
    with open(ruta, 'r', newline='') as mostrar_csv:
        reader = csv.DictReader(
            mostrar_csv, dialect='excel', delimiter=',', fieldnames=head)

        heroes = [(row["Heroe"], row["Aparicion"], row["Popularidad"])
                  for row in reader]
        if not heroes:
            print('no hay heroes registrados')
            return False

        print('Heroes registrados:')
        print('---------------------------')
        for heroe in heroes:
            print(f'{heroe[0]}|{heroe[1]}|{heroe[2]}')
        print('---------------------------')
        print()
        enter = input('Presione enter para continuar...')
        system('cls')


def maximaPopularidad():
    os.system('cls')
    if not listaHeroes:
        print('No hay heroes registrados.')
        enter = input('Presione enter para continuar...')
        os.system('cls')
        return

    maxPopularidad = [h for h in listaHeroes if h.get(
        "Popularidad") is not None]

    if not maxPopularidad:
        print('no se encontraron heroes con popularidad.')
        enter = input('Presione enter para continuar...')
        os.system('cls')
        return

    maxPopularidad = max(maxPopularidad, key=lambda h: h['Popularidad'])

    print(f'el heroe con la mayor popularidad es :{
          maxPopularidad["Heroe"]}')
    print('------------------------------------------------')
    print(f'con una popularidad de : {maxPopularidad["Popularidad"]}')
    enter = input('Presione enter para continuar...')
    system('cls')


def buscarHeroe():
    os.system('cls')
    print('Gestion buscar heroe')
    print('------------------------------------------------')
    buscarHeroe = input(
        'ingrese el nombre del heroe a buscar: ').strip().lower()
    heroes = [(row["Heroe"], row["Aparicion"], row["Popularidad"])
              for row in listaHeroes]
    if not heroes:
        print('No hay heroes registrados.')
    else:
        encontrado = False
        for heroe in heroes:
            if heroe[0].lower() == buscarHeroe:
                print(f'Heroe encontrado: {heroe[0]}')
                print(f'{heroe[0]},{heroe[1]},{heroe[2]}\n')
                encontrado = True
        if not encontrado:
            print('Heroe no encontrado.')
    return


def menu():
    print('\tMenu Heroes')
    print('1. Agregar heroe')
    print('2. Popularidad heroes')
    print('3. Mostrar heroes')
    print('4. Mostrar maxima popularidad heroe')
    print('5. Buscar heroe')
    print('6. Salir')
    o = int(input('Ingrese una opcion: '))
    if o == 1:
        heroes()
    if o == 2:
        popularidadHeroes()
    if o == 3:
        mostrarHeroes()
    if o == 4:
        maximaPopularidad()
    if o == 5:
        buscarHeroe()
    if o == 6:
        system('cls')
        print(
            'Saliendo del registro de heroes...\nGracias por utilizar nuestro programa. :)')
        exit()


if __name__ == '__main__':
    while True:
        menu()
