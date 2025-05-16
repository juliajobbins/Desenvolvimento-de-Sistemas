# 1)
nome = "Julia Fernanda Jobbins"
numero = 15

# 2)
print(f"##### Bem-vindo ao Sistema! #####\nSistema criado por {nome}, nº da chamada: {numero}")

# 3)
altura = 1.58
musicafav = "The Truth Untold"
animefav = "Attack on Titan"
notaIMDb = 9.1

# 4)

altura_usuario = float(input("Insira a sua altura em metros: "))

if altura_usuario > altura:
    print("Você é maior que eu (๑•ᴗ•๑)")
elif altura_usuario == altura:
    print("Nós temos a mesma altura (˵>ᗜ<˵) !!")
else:
    print("Você é mais baixo que eu (˶ᵔ ᵕ ᵔ˶)")

# 5)
musicas_usuario = []
contador = 0

while contador < 3:
    musica = input(f"Digite três músicas que você gosta ({contador +1}/3): ")
    musicas_usuario.append(musica)
    contador += 1

if musicafav in musicas_usuario:
    print("Ótimo gosto! Você gosta da minha música favorita ♡⸜(˶˃ ᵕ ˂˶)⸝♡")
else:
    print("Parece que temos gostos diferentes em música ˙◠˙")

# 6)

animes_usuario = []
notas_animes = []

for i in range(3):
    anime = (input(f"Digite um anime que você gosta ({i+1}/3): "))
    nota = float(input(f"Digite a nota do IMDb para {anime}: "))
    animes_usuario.append(anime)
    notas_animes.append(nota)

for i in range(3):
    if notas_animes[i] > notaIMDb:
        print(f"O anime {animes_usuario[i]} tem uma nota maior que {animefav} ( ˶ˆᗜˆ˵ )")
    elif notas_animes[i] == notaIMDb:
        print(f"O anime {animes_usuario[i]} tem uma nota igual a nota de {animefav} (˵>ᗜ<˵) !!")
    else:
        print(f"O anime {animes_usuario[i]} tem uma nota menor que {animefav} (˶ᵔ ᵕ ᵔ˶)")