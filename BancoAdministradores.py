import sqlite3


class BancoAdministradores():
    def __init__(self):
        self.conexao = sqlite3.connect("bancoAdministradores.db")
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists usuarios (
                     idAdministrador integer primary key autoincrement,
                     nome text,
                     cpf text,
                     nascimento text,
                     email text,
                     senha text,
                     telefone text,
                     emailNotificacoes text,
                     admin text""")
        self.conexao.commit()
        c.close()
