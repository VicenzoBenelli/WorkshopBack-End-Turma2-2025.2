import math

def Arredondamento_total(num):
    piso = math.floor(num)
    teto = math.ceil(num)
    arredondado = math.ceil(num)

    return piso, teto, arredondado

num = float(input("Digite um valor real: "))

resultado = Arredondamento_total(num)


