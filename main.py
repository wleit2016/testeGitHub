from Calculos import proximoNumeroPrimo

if __name__ == '__main__':
    listaNumeroPrimo = []
    numeroPrimo = 2

    numero1TXT = input("Digite um numero: ")
    numero2TXT = input("Digite um numero: ")

    numero1 = int(numero1TXT)
    numero2 = int(numero2TXT)

    condicao = True

    while condicao:
        if numero1 % numeroPrimo == 0 or numero2 % numeroPrimo == 0:
            print(numero1, " - ", numero2, "|", numeroPrimo)
            if numero1 % numeroPrimo == 0:
                numero1 = int(numero1 / numeroPrimo)

            if numero2 % numeroPrimo == 0:
                numero2 = int(numero2 / numeroPrimo)

            listaNumeroPrimo.append(numeroPrimo)
        else:
            numeroPrimo = proximoNumeroPrimo(numeroPrimo)

        if numero1 == 1 and numero2 == 1:
            condicao = False

    print(numero1, " - ", numero2, "|")

    tamanho = len(listaNumeroPrimo)
    posicao = 0
    multiplicar = 1

    while(posicao < tamanho):
        multiplicar = multiplicar * listaNumeroPrimo.pop()
        posicao = posicao + 1

    print('MMC = ', str(multiplicar))
