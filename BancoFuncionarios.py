import sqlite3


class BancoFuncionarios():
    def __init__(self):
        self.conexao = sqlite3.connect("bancoFuncionarios.db")
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists usuarios (
                     idFuncionario integer primary key autoincrement,
                     nome text,
                     cpf text,
                     nascimento text,
                     email text,
                     senha text,
                     telefone text""")
        self.conexao.commit()
        c.close()


class BancoClientesFuncionarios():
    def __init__(self):
        self.conexao = sqlite3.connect("bancoClientesFuncionarios.db")
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists usuarios (
                     idClienteFuncionario integer primary key autoincrement,
                     funcionario text,
                     desconto integer,
                     logradouro text,
                     bairro text,
                     cidade text,
                     cep text,
                     estado text,
                     complemento text,
                     numero integer)""")
        self.conexao.commit()
        c.close()
