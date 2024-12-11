def validarNumero(num):
    if num < 0:
        return "Número negativo"
    elif num == 0:
        return "Número neutro"
    else:
        return "Número positivo"

numero = 0;
print(validarNumero(numero))