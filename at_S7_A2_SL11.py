print("Cáculo de desconto")
valor = float(input("Informe o Valor do Produto R$:"))
if valor >= 100:
    desconto = valor * 0.90
    valor_novo = desconto
    print(f"Valor do produto com desconto de 10% é R${valor_novo}")
else:
    print(f"Valor menor que R$ 100,00 não há desconto")
    print(f"seu valor permanece R${valor}")
