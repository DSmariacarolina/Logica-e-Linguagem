# Passo 1: Entrada de dados
try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    # Passo 2: Processamento dos dados
    adicao = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    divisao = numero1 / numero2

    # Passo 3: Saída de dados
    print(f"A adição dos números é: {adicao}")
    print(f"A subtração dos números é: {subtracao}")
    print(f"A multiplicação dos números é: {multiplicacao}")
    print(f"A divisão dos números é: {divisao}")

except ValueError:
    print("Por favor, digite números válidos.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")