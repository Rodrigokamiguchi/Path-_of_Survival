import random

# Atributos iniciais do jogador
comida = 50
agua = 50
saude = 50
energia = 50
dias_sobrevividos = 0

print("Bem-vindo à simulação de vida!")
print("Sobreviva o maior número de dias possível.")
print("Cuidado: se qualquer atributo chegar a 0, você perde.")

# Loop principal do jogo
while comida > 0 and agua > 0 and saude > 0 and energia > 0:
    print(f"\nDia {dias_sobrevividos + 1}")
    print(f"Comida: {comida} | Água: {agua} | Energia: {energia} | Saúde: {saude}")
    print("Selecione uma opção:")
    print("1. Procurar recursos")
    print("2. Descansar")
    print("3. Explorar")
    print("4. Construir abrigo")

    escolha = input("Digite o número da ação: ")

    if escolha == "1":
        recursos_comida = random.randint(10, 30)
        recursos_agua = random.randint(10, 30)
        comida += recursos_comida
        agua += recursos_agua
        energia -= 10
        print(f"Você encontrou {recursos_comida} de comida e {recursos_agua} de água!")

    elif escolha == "2":
        energia += 20
        saude += 10
        comida -= 10
        agua -= 10
        print("Você descansou e recuperou 20 de energia e 10 de saúde, mas perdeu 10 de comida e 10 de água.")

    elif escolha == "3":
        energia -= 15
        evento = random.choice(["tempestade", "tesouro", "criatura", "sobrevivente"])
        
        if evento == "tempestade":
            chance = random.randint(1, 100)  # Gera um número de 1 a 100
            if chance <= 50:  # 50% de chance de ser atingido
                saude -= 20
                print("Você enfrentou uma tempestade e foi atingido, perdendo 20 de saúde.")
            else:
                print("Você enfrentou uma tempestade, mas conseguiu escapar ileso!")
        
        elif evento == "tesouro":
            ganho_comida = 20
            ganho_agua = 20
            comida += ganho_comida
            agua += ganho_agua
            print(f"Você encontrou um tesouro com {ganho_comida} de comida e {ganho_agua} de água!")
       
        elif evento == "criatura":
            saude -= 30
            print("Você foi atacado por uma criatura e perdeu 30 de saúde.")
        
        elif evento == "sobrevivente":
            chance = random.choice(["amigo", "inimigo"])
            if chance == "amigo":
                ganho_comida = 15
                ganho_agua = 15
                comida += ganho_comida
                agua += ganho_agua
                print(f"Você encontrou um sobrevivente amigável que compartilhou recursos: +{ganho_comida} comida e +{ganho_agua} água!")
            else:
                saude -= 15
                print("Você encontrou um sobrevivente hostil e foi ferido, perdendo 15 de saúde.")
    elif escolha == "4":
        energia -= 20
        print("Você trabalhou no abrigo, melhorando sua eficiencia, mas perdeu 20 de energia")
    else:
        print("Escolha invalida! Você perdeu a sua vez")
    
    # Reduz recursos a cada dia
    comida -= 5
    agua -= 5
    energia -= 5

    # Incrementa dias sobrevividos
    dias_sobrevividos += 1

# Fim do jogo
print("\nVocê não conseguiu sobreviver.")
print(f"Dias Sobrevividos: {dias_sobrevividos}")
  