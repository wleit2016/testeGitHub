from Calculos import proximoNumeroPrimo

if __name__ == '__main__':
    numeroPrimo = 2

    numero1TXT = input("Digite um numero: ")
    numero2TXT = input("Digite um numero: ")

    numero1 = int(numero1TXT)

    while numero1 != 1:
        if numero1 % numeroPrimo == 0 :
            print(numero1, "|", numeroPrimo)
            numero1 = int(numero1 / numeroPrimo)
        else:
            numeroPrimo = proximoNumeroPrimo(numeroPrimo)

