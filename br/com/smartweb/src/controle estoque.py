print("-------------------------SISTEMA DE VENDAS-----------------------------")
i = 0
total = 0
media = 0

venda = float(input("Digite o valor da venda ou -1 para sair:"))


while venda != -1:
    
    i += 1
    total += venda

    venda = float(input("Digite o valor da venda ou -1 para sair:"))
    if i > 0:
        media = total / i
    else:
        media = 0


print("-------------------------RELATORIO DO SISTEMA DE VENDAS-----------------------------")
print(f"\nQuantidade de vendas: {i}")
print(f"\nTotal vendido: {total:.2f}")
print(f"\nMedia das vendas: R$ {media:.2f}")
print("------------------------------------------------------------------------------------")