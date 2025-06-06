class Conta:
    # Método construtor
    def __init__(self, agencia, numero, titular, saldo, senha):
        # Criando os atributos da classe
        self.__agencia = agencia
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__senha = senha

    @property
    def numero(self):
        return self.__numero
    
    def extrato(self):
        return self.__saldo

    def saque(self, valor):
        if valor <= self.__saldo and valor > 0:
            self.__saldo -= valor
            return True
        else:
            return False

    def deposito(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        else:
            return False

        
        