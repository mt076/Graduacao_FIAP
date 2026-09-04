print("------- Agência de Viagens -------")

classe = input("Digite a classe do voo (Econômica, Executiva, Primeira): ")
quantidade_passagens = int(input("Digite a quantidade de passageiros: "))

lista_classes = ["Econômica", "Executiva", "Primeira"]
preco_passagem = 850

if classe == lista_classes[0] and quantidade_passagens == 2:
    desconto = preco_passagem * 0.03
    valor_final = preco_passagem - desconto
    print(f"Você finalizaou a compra de {quantidade_passagens} passagens na classe {classe}, no valor de R${preco_passagem}. Foi aplicado um desconto de 3% e o valor final ficou em R${valor_final:.2f}")
elif classe == lista_classes[0] and quantidade_passagens == 3:
    desconto = preco_passagem * 0.04
    valor_final = preco_passagem - desconto
    print(f"Você finalizaou a compra de {quantidade_passagens} passagens na classe {classe}, no valor de R${preco_passagem}. Foi aplicado um desconto de 4% e o valor final ficou em R${valor_final:.2f}")
elif classe == lista_classes[0] and quantidade_passagens >= 4:
    desconto = preco_passagem * 0.05
    valor_final = preco_passagem - desconto
    print(f"Você finalizaou a compra de {quantidade_passagens} passagens na classe {classe}, no valor de R${preco_passagem}. Foi aplicado um desconto de 5% e o valor final ficou em R${valor_final:.2f}")
elif classe == lista_classes[1] and quantidade_passagens == 2:
    desconto = preco_passagem * 0.05
    valor_final = preco_passagem - desconto
    print(f"Você finalizaou a compra de {quantidade_passagens} passagens na classe {classe}, no valor de R${preco_passagem}. Foi aplicado um desconto de 5% e o valor final ficou em R${valor_final:.2f}")
elif classe == lista_classes[1] and quantidade_passagens == 3:
    desconto = preco_passagem * 0.07
    valor_final = preco_passagem - desconto
    print(f"Você finalizaou a compra de {quantidade_passagens} passagens na classe {classe}, no valor de R${preco_passagem}. Foi aplicado um desconto de 7% e o valor final ficou em R${valor_final:.2f}")
elif classe == lista_classes[1] and quantidade_passagens >= 4:
    desconto = preco_passagem * 0.08
    valor_final = preco_passagem - desconto
    print(f"Você finalizaou a compra de {quantidade_passagens} passagens na classe {classe}, no valor de R${preco_passagem}. Foi aplicado um desconto de 8% e o valor final ficou em R${valor_final:.2f}")
elif classe == lista_classes[2] and quantidade_passagens == 2:
    desconto = preco_passagem * 0.10
    valor_final = preco_passagem - desconto
    print(f"Você finalizaou a compra de {quantidade_passagens} passagens na classe {classe}, no valor de R${preco_passagem}. Foi aplicado um desconto de 10% e o valor final ficou em R${valor_final:.2f}")
elif classe == lista_classes[2] and quantidade_passagens == 3:
    desconto = preco_passagem * 0.15
    valor_final = preco_passagem - desconto
    print(f"Você finalizaou a compra de {quantidade_passagens} passagens na classe {classe}, no valor de R${preco_passagem}. Foi aplicado um desconto de 15% e o valor final ficou em R${valor_final:.2f}")
elif classe == lista_classes[2] and quantidade_passagens >= 4:
    desconto = preco_passagem * 0.20
    valor_final = preco_passagem - desconto
    print(f"Você finalizaou a compra de {quantidade_passagens} passagens na classe {classe}, no valor de R${preco_passagem}. Foi aplicado um desconto de 20% e o valor final ficou em R${valor_final:.2f}")
else:
    print("A classe ou quantidade não consta em nosso banco de dados!")