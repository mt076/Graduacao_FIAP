lista_produtos = {"celular": 2040, "Acer_predator": 9400, "monitor_aox": 640, "microfone_fifine": 105}

print(f"Lista de produtos disponíveis em nossa loja: {list(lista_produtos.keys())}")
pedido = input("Qual produto irá levar?:  ")


if pedido in lista_produtos:
    print(f"O preço do {pedido} é R$ {lista_produtos[pedido]:.2f}")
    print("Obrigado por comprar conosco!")
if pedido == "Acer_predator":
    desconto = lista_produtos[pedido] * 0.20
    print(f"Você recebeu um desconto de R$ {desconto:.2f}!")
else:
    print("Você digitou um produto que não consta na lista!")