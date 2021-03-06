import sqlite3


class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect("databases/bancoClientes.db")
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists usuarios (
                     idCliente integer primary key autoincrement,
                     nome text,
                     cpf text,
                     nascimento text,
                     email text,
                     senha text,
                     telefone text,
                     logradouro text,
                     bairro text,
                     cidade text,
                     cep text,
                     estado text,
                     complemento text,
                     numero integer)""")
        self.conexao.commit()
        c.close()
