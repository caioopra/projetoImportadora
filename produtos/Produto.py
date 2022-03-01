class Produto():
    def __init__(self, valorCompra, moeda, taxaLucro, valorVenda, qtdDisponivel, disponivel):
        self.valorCompra = valorCompra
        self.moeda = moeda
        self.taxaLucro = taxaLucro
        self.valorVenda = valorVenda
        self.qtdDisponivel = qtdDisponivel
        self.disponivel = disponivel

    def atualizar_valor(self, valorCompra, taxaLucro, moeda):
        pass
