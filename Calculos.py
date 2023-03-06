def ePrimo(numero):
    resposta = False
    contar = 0
    indice = 2

    while (indice <= numero and contar != 2):
        if(numero % indice == 0):
            contar = contar + 1
        indice = indice + 1
    if(contar == 1):
        resposta = True
    return resposta

def proximoNumeroPrimo(numero):
    numero = numero + 1
    avancar = True

    while(avancar):
        if(not ePrimo(numero)):
            numero = numero + 1
        else:
            avancar = False
    return numero