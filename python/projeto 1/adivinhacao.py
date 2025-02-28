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
   sorteio = random.randint(1, numero_max)
   print("Você escolheu o nível fácil! Você deve acertar o número entre 1 e 10 em 3 tentativas!")
elif(nivel == 2):
   limite_tentativas = 5
   numero_max = 20
   sorteio = random.randint(1, numero_max)
   print("Você escolheu o nível médio! Você deve acertar o número entre 1 e 20 em 5 tentativas!")
elif(nivel == 3):
   limite_tentativas = 10
   numero_max = 100
   sorteio = random.randint(1, numero_max)
   print("Você escolheu o nível difícil! Você deve acertar o número entre 1 e 100 em 10 tentativas!")
else:
   print("Opção inválida")


if(nivel == 1):
   while (limite_tentativas >= tentativa):
       print("Tentativa", tentativa)
       chute = int(input("Digite o seu chute: "))
       if (chute == sorteio):
           print("Parabéns, você acertou!")
           break
       elif (tentativa <=2 and chute > sorteio):
           print("Chute um número menor!")
       elif (tentativa <=2 and chute < sorteio):
           print("Chute um número maior!")
       tentativa = tentativa + 1
       if(tentativa > 3 and chute != sorteio):
        print("Você perdeu! O número era: ", sorteio,)
        print("Jogue novamente e boa sorte!")

if(nivel == 2):
   while (limite_tentativas >= tentativa):
       print("Tentativa", tentativa)
       chute = int(input("Digite o seu chute: "))
       if (chute == sorteio):
           print("Parabéns, você acertou!")
           break
       elif (tentativa <=4 and chute > sorteio):
           print("Chute um número menor!")
       elif (tentativa <=4 and chute < sorteio):
           print("Chute um número maior!")
       tentativa = tentativa + 1
       if(tentativa > 5 and chute != sorteio):
        print("Você perdeu! O número era: ", sorteio,)
        print("Jogue novamente e boa sorte!")

if(nivel == 3):
   while (limite_tentativas >= tentativa):
       print("Tentativa", tentativa)
       chute = int(input("Digite o seu chute: "))
       if (chute == sorteio):
           print("Parabéns, você acertou!")
           break
       elif (tentativa <=9 and chute > sorteio):
           print("Chute um número menor!")
       elif (tentativa <=9 and chute < sorteio):
           print("Chute um número maior!")
       tentativa = tentativa + 1
       if(tentativa > 10 and chute != sorteio):
        print("Você perdeu! O número era: ", sorteio,)
        print("Jogue novamente e boa sorte!")
