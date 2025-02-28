import random

print("##### BEM-VINDO(A) AO JOGO! #####")
print("Escolha o nível de dificuldade:")
tentativa = 1
print("1 - Nível Fácil")
print("2 - Nível Médio")
print("3 - Nível Difícil")
nivel = int(input("Digite a opção desejada: "))


if(nivel == 1):
   limite_tentativas = 3
   numero_max = 10
   print("Você escolheu o nível fácil! Você deve acertar o número entre 1 e 10 em 3 tentativas!")
elif(nivel == 2):
   limite_tentativas = 5
   numero_max = 20
   print("Você escolheu o nível médio! Você deve acertar o número entre 1 e 20 em 5 tentativas!")
elif(nivel == 3):
   limite_tentativas = 10
   numero_max = 100
   print("Você escolheu o nível difícil! Você deve acertar o número entre 1 e 100 em 10 tentativas!")
else:
   print("Opção inválida")
   exit()

sorteio = random.randint(1, numero_max)

while (limite_tentativas >= tentativa):
    print("Tentativa", tentativa)
    chute = int(input("Digite o seu chute: "))
    if (chute == sorteio):
        print("Parabéns, você acertou!")
        break
    elif (tentativa <= limite_tentativas - 1 and chute > sorteio):
        print("Chute um número menor!")
    elif (tentativa <= limite_tentativas - 1 and chute < sorteio):
        print("Chute um número maior!")
    tentativa = tentativa + 1
    if(tentativa > limite_tentativas and chute != sorteio):
        print("Você perdeu! O número era: ", sorteio)
        print("Jogue novamente e boa sorte!")
