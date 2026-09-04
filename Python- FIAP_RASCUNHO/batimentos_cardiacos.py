print("----------- Programa de Batimentos Cardiacos FIAP -----------")
print("120 até 140 BPM OU 80 até 100 BPM OU 70 até 80 BPM OU 50 até 60 BPM")


batimentos = int(input("Com base na lista revelada acima, digite o seu batimento cardiaco: "))

if batimentos >= 120 and batimentos <= 140:
    print("Você tem 2 anos de idade ou é um atleta!")
elif batimentos >= 80 and batimentos <= 100:
    print("Você tem entre 8 a 17 anos de idade")
elif batimentos >= 70 and batimentos <= 80:
    print("Você é sedentário! Procure fazer atividades física")
else:
    print("Você certamente é um idoso!")