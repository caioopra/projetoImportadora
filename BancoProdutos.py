import sqlite3


class BancoProdutos():
    def __init__(self):
        self.conexao = sqlite3.connect("databases/bancoProdutos.db")
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists produtos (
                     idProduto integer primary key autoincrement,
                     produto text,
                     valorCompra real,
                     moeda text,
                     taxaLucro real,
                     valorVenda real,
                     qtdDisponivel integer,
                     disponivel text)""")
        self.conexao.commit()
        c.close()


class BancoMoedas():
    def __init__(self):
        self.conexao = sqlite3.connect("databases/bancoMoedas.db")
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists moedas(
                     idMoeda integer primary key autoincrement,
                     nome text,
                     sigla text,
                     cotacao real,
                     horarioAtualizacao text)""")
        self.conexao.commit()
        c.close()
