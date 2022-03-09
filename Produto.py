import re
from BancoProdutos import BancoMoedas, BancoProdutos


class Produto():
    def __init__(self, produto="", valorCompra="", moeda="", taxaLucro="", qtdDisponivel="", idProduto=""):
        self.produto = produto
        self.valorCompra = valorCompra
        self.moeda = moeda
        self.taxaLucro = taxaLucro
        self.qtdDisponivel = qtdDisponivel
        self.idProduto = idProduto

        for i in range(len(listaMoedas)):
            if listaMoedas[i][2] == self.moeda:
                self.valorVenda = round(float(
                    self.valorCompra) * (1 + float(taxaLucro) / 100) * listaMoedas[i][3], 2)
                print("valorVenda: R$", self.valorVenda)
                break

        if int(qtdDisponivel) > 0:
            self.disponivel = True
        else:
            self.disponivel = False

    def atualizar_valor(self, valorCompra, taxaLucro, moeda):
        pass

    def cadastrarProduto(self):
        banco = BancoProdutos()

        try:
            c = banco.conexao.cursor()
            c.execute(
                "insert into produtos (produto, valorCompra, moeda, taxaLucro, valorVenda, qtdDisponivel, disponivel) values ('" + self.produto + "', '" + self.valorCompra + "', '" + self.moeda + "', '" + self.taxaLucro + "', '" + self.valorVenda + "', '" + self.qtdDisponivel + "', '" + self.disponivel + "') ")

            banco.conexao.commit()
            c.close()

            return "Produto adicionado com sucesso!"
        except:
            return "Erro ao adicionar produto"


class Moeda():
    def __init__(self, nome="", sigla="", cotacao="", horarioAtualizacao="", idMoeda=""):

        self.nome = nome
        self.sigla = sigla
        self.cotacao = cotacao
        self.horarioAtualizacao = horarioAtualizacao
        self.idMoeda = idMoeda

    def cadastrarMoeda(self):
        banco = BancoMoedas()

        try:
            c = banco.conexao.cursor()

            c.execute("insert into moedas (nome, sigla, cotacao, horarioAtualizacao) values ('" + self.nome +
                      "', '" + self.sigla + "', '" + str(self.cotacao) + "', '" + self.horarioAtualizacao + "') ")
            banco.conexao.commit()
            c.close()

            return "Moeda cadastrada"
        except:
            return "Erro no cadastro da moeda"


def listarMoedas():
    banco = BancoMoedas()
    try:
        c = banco.conexao.cursor()

        query = """select * from moedas"""
        c.execute(query)
        dados = c.fetchall()
        return dados

    except:
        return "Erro ao listar moedas"


moeda = Moeda("dolar", "USD", 5.06, "08/03/2022 - 22:52:30")
listaMoedas = listarMoedas()


camera = Produto("Celular Samsung S22", "799", "USD", "10", "3")
