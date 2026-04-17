def calcular_preco_final(valor, desconto_percentual):
    valor_do_desconto = valor * (desconto_percentual/100)
    preco_com_desconto = valor - valor_do_desconto
    return preco_com_desconto

total = calcular_preco_final(2352, 20)
print(total)

frete = calcular_preco_final(1800, 15)

print(frete)