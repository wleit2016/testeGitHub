from Calculos import ePrimo
from Calculos import proximoNumeroPrimo

if __name__ == '__main__':
    numero = int(input("Digite um numero: "))
    resultado = ePrimo(numero)

    proximoNumero = proximoNumeroPrimo(numero)
    print(resultado)
    print("Proximo número: " + str(proximoNumero))