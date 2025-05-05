import adivinhacao
import forca

print("Escolha o jogo desejado:")
print("1- Adivinhação\n2-Forca")

opcao = int(input("Digite o número do jogo desejado: "))

if(opcao == 1):
    # Executar adivinhação
    print("Executando adivinhação...")
    adivinhacao.jogar()
elif(opcao == 2):
    #Executar forca
    print("Executando forca...")
    forca.jogar()
else:
    # Opção inválida
    print("Opção inválida.")