from random import choice, sample

cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
    }

def obtener_valores_cartas(dic):
    valores = (dic.values())
    return valores

def obtener_cartas(dic):
    cartas = sorted(dic.keys())
    return cartas

def jugador_escoge2_cartas(dic):
    cartas = obtener_cartas(dic)
    carta1= choice(cartas)
    carta2= choice(cartas)
    score = dic[carta1]+dic[carta2]
    return carta1, carta2, score

def banca_coge2_cartas(dic):
    cartas = obtener_cartas(dic)
    cartas_banca = sample(cartas,2)
    score_banca = sum(dic[carta] for carta in cartas_banca)
    return cartas_banca, score_banca

def blackjack(dic):
    carta1, carta2, score = jugador_escoge2_cartas(dic)
    cartas_banca, score_banca = banca_coge2_cartas(dic)
    print("Ha seleccionado: {} {}  >> su score es {}".format(carta1, carta2, score))
    print("La banca tiene: {} {}  >> su score es {}".format(cartas_banca[0],cartas_banca[1],score_banca))

