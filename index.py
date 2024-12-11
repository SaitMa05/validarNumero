def validarNumero(num):
    if num < 0:
        return "Número negativo"
    elif num == 0:
        return "Número neutro"
    else:
        return "Número positivo"

numero = int(input("Digite um número: "))
print(validarNumero(numero))