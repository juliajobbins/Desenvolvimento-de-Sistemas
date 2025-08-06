class Quarto:
    def __init__(self, numero, tipo, diaria, disponivel = True):
        self.numero = numero
        self.tipo = tipo
        self.diaria = diaria
        self.disponivel = disponivel

    def exibir_detalhes(self):
        if self.disponivel:
            status = "Disponível"
        else:
            status = "Ocupado"
        print(f"Quarto {self.numero} - Tipo: {self.tipo}")
        print(f"Valor da diária: R${self.diaria}")
        print(f"Status: {status}")
        print("----------")
 
    def reservar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"Quarto {self.numero} reservado com sucesso!")
        else:
            print(f"Quarto {self.numero} já está ocupado.")
    
    def liberar(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"Quarto {self.numero} foi liberado!")
        else:
            print(f"Quarto {self.numero} já está disponível.")

    def alterar_preco(self, novo_valor):
        self.diaria = novo_valor
        print(f"Valor da diária do quarto {self.numero} alterado para R${self.diaria}")