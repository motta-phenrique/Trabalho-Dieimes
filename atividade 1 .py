class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor} realizado com sucesso.')

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado com sucesso.')
        else:
            print('Saldo insuficiente para realizar o saque.')

    def ver_saldo(self):
        print(f'Saldo atual da conta de {self.titular}: R${self.saldo}')



conta = ContaBancaria("Diemes")


conta.depositar(500)
conta.ver_saldo()

conta.sacar(200)
conta.ver_saldo()

conta.sacar(400)
conta.ver_saldo()
