import random

def carregar_palavras(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            return [linha.strip().lower() for linha in arquivo.readlines()]
    except FileNotFoundError:
        print(f"Erro: O arquivo {nome_arquivo} não foi encontrado.")
        return []

temas = {
    "kpop": "forca/gruposkpop.txt",
    "doramas": "forca/doramas.txt",
    "animes": "forca/animes.txt"
}

print("Escolha um tema:")
for tema in temas:
    print(f"- {tema}")

tema_escolhido = input("Digite o tema desejado: ").strip().lower()
while tema_escolhido not in temas:
    print("Tema inválido! Tente novamente.")
    tema_escolhido = input("Digite o tema desejado: ").strip().lower()
    
palavras = carregar_palavras(temas[tema_escolhido])
if not palavras:
    print("Não foi possível carregar palavras. O jogo será encerrado.")
    exit()

palavra = random.choice(palavras)
limite_tentativas = len(palavra) + 5
acertou = False
enforcou = False

letras_acertadas = ["_" if letra != " " else " " for letra in palavra]

contador = 1

while not acertou and not enforcou:
    print(" ".join(letras_acertadas))
    print(f"Tentativas: {contador}/{limite_tentativas}")
    chute = input("Digite uma letra: ").strip().lower()
    
    indice = 0
    for letra in palavra:
        if chute == letra:
            letras_acertadas[indice] = chute
        indice += 1

    if contador == limite_tentativas:
        enforcou = True
        print(f"Você perdeu! ˊᴖˋ\n A palavra era: {palavra}")
    
    if "_" not in letras_acertadas:
        acertou = True
        print("Parabéns! Você encontrou a palavra secreta! ♡⸜(˶˃ ᵕ ˂˶)⸝♡")

    contador += 1
