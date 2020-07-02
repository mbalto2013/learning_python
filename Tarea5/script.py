
import sys
import random
from datetime import datetime as dt
from mazo.resultados import Resultado, guardar_resultados, cargar_resultados
from mazo.cartas import Carta, crear_mazo, revolver_mazo, sacar_cartas, LISTA_PALOS


def obtener_palos():
    palos_rojos = ['Diamantes', 'Corazones']
    palos_negros = ['Flores', 'Espadas']

    random.shuffle(palos_rojos)
    random.shuffle(palos_negros)

    resultado = {
        'palo_fuerte': palos_rojos[0],
        'palo_debil': palos_negros[1],
        'palos_regulares': [palos_rojos[1], palos_negros[0]]}
    return(resultado)


def enrutar_accion(id_de_accion, nombre):
    acciones = [1, 2, 3]
    if id_de_accion in acciones:
        if id_de_accion == 1:
            iniciar_juego(nombre)
        if id_de_accion == 2:
            imprimir_resultados()
        if id_de_accion == 3:
            print('Gracias por participar')
            exit(0)
    else:
        print('Accion invalida')


def realizar_encuentros(nombre, cartas_jugador,
                        cartas_ocultas, palos, juegos_por_ganar):
    resulado_de_encuetros = []
    print('\nENCUENTROS:')
    for indice in range(0, 10):
        carta_jugador, carta_oculta = cartas_jugador[indice], cartas_ocultas[indice]
        resultado = calcular_puntaje(carta_jugador, carta_oculta, palos)
        resulado_de_encuetros.append(resultado)
        print(
            f'  {carta_jugador.informacion()} vs {carta_oculta.informacion()} = {resultado.get("msj")}')

    victorias = len(
        [resultado for resultado in resulado_de_encuetros if resultado.get('puntaje') == 1])
    puntos = 10 - (abs(victorias - juegos_por_ganar))
    resultados = cargar_resultados()
    resultados.append(Resultado(dt.now(), nombre, puntos))
    guardar_resultados(resultados)
    print(f'\n {nombre} Haz obtenido {puntos} puntos!\n')


def calcular_puntaje(carta_jugador, carta_oculta, palos):
    palo_fuerte = palos.get('palo_fuerte')
    palo_debil = palos.get('palo_debil')
    palos_regulares = palos.get('palos_regulares')

    resultado = {'msj': 'Haz, perdido', 'puntaje': 0}
    if carta_jugador.get_palo() == carta_oculta.get_palo():
        if carta_jugador.get_valor() > carta_oculta.get_valor():
            resultado = {'msj': 'Haz, ganado!', 'puntaje': 1}

    elif carta_jugador.get_palo() in palos_regulares and carta_oculta.get_palo() in palos_regulares:
        if carta_jugador.get_valor() >= carta_oculta.get_valor():
            resultado = {'msj': 'Haz, ganado!', 'puntaje': 1}

    elif carta_jugador.get_palo() == palo_fuerte and carta_oculta.get_palo() in palos_regulares:
        resultado = {'msj': 'Haz, ganado!', 'puntaje': 1}

    elif carta_jugador.get_palo() in palos_regulares and carta_oculta.get_palo() == palo_debil:
        resultado = {'msj': 'Haz, ganado!', 'puntaje': 1}

    elif carta_jugador.get_palo() == palo_debil and carta_oculta.get_palo() == palo_fuerte:
        resultado = {'msj': 'Haz, ganado!', 'puntaje': 1}
    return(resultado)


def iniciar_juego(nombre):
    print('iniciando el juego')
    nuevo_mazo = revolver_mazo(crear_mazo())
    cartas_del_jugador = sacar_cartas(nuevo_mazo, 10)
    cartas_ocultas = sacar_cartas(nuevo_mazo, 10)

    palos = obtener_palos()

    print('\nPALOS DEL JUEGO')
    print(f' Fuerte: {palos.get("palo_fuerte")}')
    print(f' Debil: {palos.get("palo_debil")}\n')

    print('SUS CARTAS:')

    for carta in cartas_del_jugador:
        print(f'  {carta.informacion()}')
    encuentros_estimados = int(
        input('De diez encuetros, cuantos cree ganar? (1-10): '))

    if encuentros_estimados in range(1, 11):
        realizar_encuentros(
            nombre,
            cartas_del_jugador,
            cartas_ocultas,
            palos,
            encuentros_estimados)
    else:
        print('Error')


def imprimir_resultados():
    resultados = cargar_resultados()
    if len(resultados) > 0:
        for resultado in resultados:
            print(resultado.informacion())
        print('')
    else:
        print('\nNo existen registros\n')


nombre = sys.argv[1]
opcion = 0
while opcion != 3:
    print('''Acciones disponibles:
    1- Iniciar Juego
    2- Ver Puntuaciones
    3- Salir
    ''')
    accion = int(input(f'{nombre}, cual desea ejecutar?: '))
    enrutar_accion(accion, nombre)
