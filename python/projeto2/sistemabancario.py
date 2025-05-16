def criaConta(agencia, numero, titular, saldo, limite, senha):
    conta = {
        "agencia": agencia,
        "numero": numero,
        "titular": titular,
        "saldo": saldo,
        "limite": limite,
        "senha": senha
    }
    return conta

conta2 = criaConta(456, "1000-5", "Francisco Cisco", 30000.0, 50000.0, 9555)
print(f"Agência: {conta2['agencia']}\nNúmero: {conta2['numero']}\nTitular: {conta2['titular']}\nSaldo: {conta2['saldo']}\nLimite: {conta2['limite']}\nSenha: {conta2['senha']}")