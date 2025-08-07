from conta import Conta

conta1 = Conta(123, "10500-1", "Francisco Cisco", 30000.0, 1234)

print(f'Saldo inicial: R${conta1.extrato()}')
valor = float(input("Insira um valor para depositar: "))
if valor > 0:
    conta1.deposito(valor)
    print(f'Saldo após depósito: R${conta1.extrato()}')
else:
    print("Não é possível depositar esse valor.")

valor = float(input("Insira um valor para sacar: "))

if valor > conta1.extrato:
    conta1.saque(valor)
    print(f'Saldo após saque: R${conta1.extrato()}')
else:
    print("Não é possível sacar esse valor.")
