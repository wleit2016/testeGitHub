from Calculos import ePrimo
from Calculos import proximoNumeroPrimo

if __name__ == '__main__':
    numeroPrimo = 2
    numero = int(input("Digite um numero: "))

    while numero != 1:
        if numero % numeroPrimo == 0 :
            print(numero, "|", numeroPrimo)
            numero = int(numero / numeroPrimo)
        else:
            numeroPrimo = proximoNumeroPrimo(numeroPrimo)

