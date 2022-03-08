import sqlite3


class BancoAdministradores():
    def __init__(self):
        self.conexao = sqlite3.connect("databases/bancoAdministradores.db")
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists usuarios (
                     idAdministrador integer primary key autoincrement,
                     nome text,
                     cpf text,
                     email text,
                     senha text,
                     nascimento text,
                     telefone text,
                     emailNotificacoes text,
                     admin text)""")
        self.conexao.commit()
        c.close()
