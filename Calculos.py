def ePrimo(numero):
    resposta = False
    contar = 0
    indice = 2

    while (indice <= numero):
        if(numero % indice == 0):
            contar = contar + 1
        indice = indice + 1
    if(contar == 1):
        resposta = True
    return resposta