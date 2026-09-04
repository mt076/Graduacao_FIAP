print("Escola o código de console entre 001 - Playstation 5, 002 - Xbox Series X, 003 - Nintendo Switch)")
membro1 = int(input("Digite qual código de console você deseja ganhar!: "))
membro2 = int(input("Digite qual código de console você deseja ganhar!: "))
membro3 = int(input("Digite qual código de console você deseja ganhar!: "))
membro4 = int(input("Digite qual código de console você deseja ganhar!: "))
membro5 = int(input("Digite qual código de console você deseja ganhar!: "))

lista = []

for i in range(1, 6):
    if i == 1:
        lista.append(membro1)
    elif i == 2:
        lista.append(membro2)
    elif i == 3:
        lista.append(membro3)
    elif i == 4:
        lista.append(membro4)
    elif i == 5:
        lista.append(membro5)
print(f"O console mais votado é: {max(set(lista), key = lista.count)}")