ganhos = input("Digite os valores dos ganhos separados por vírgula: ")
ganhos = [float(valor) for valor in ganhos.split(",")]

gastos = input("Digite os valores dos gastos separados por vírgula: ")
gastos = [float(valor) for valor in gastos.split(",")]

def somatoria(lista):
    contador = 0
    soma = 0
    while (contador < len(lista)):
        soma = soma + lista[contador]
        contador = contador + 1
    return soma

somagastos = somatoria(gastos)
print ("Soma dos gastos: ", somagastos)
somaganhos = somatoria(ganhos)
print ("Soma dos ganhos: ", somaganhos)
print ("Saldo final: ", somaganhos - somagastos)
