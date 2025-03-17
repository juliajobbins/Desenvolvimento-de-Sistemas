ganhos = [3500, 55]
gastos = [1500, 54, 245, 98]

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
