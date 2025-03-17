ganhos = [3500, 55]
gastos = [1500, 54, 245, 98]

def somatoria(lista):
    contador = 0
    soma = 0
    while (contador < len(lista)):
        soma = soma + lista[contador]
        contador = contador + 1
    return soma

somacusto = somatoria(custos)
print ("Soma dos custos: " , somacusto)
somaganhos = somatoria(ganhos)
print ("Soma dos ganhos: " , somaganhos)
print ("Saldo final: " , somaganhos - somacusto)
