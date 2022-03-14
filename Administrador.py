from Funcionario import Funcionario
from BancoAdministradores import BancoAdministradores


class Administrador(Funcionario):
    def __init__(self, nome="", cpf="", email="", senha="", nascimento="", telefone="", emailNotificacoes="", idAdministrador=""):
        Funcionario.__init__(self, nome, cpf, nascimento,
                             email, senha, telefone, idAdministrador)

        self.idAdministrador = idAdministrador
        self.emailNotificacoes = emailNotificacoes
        self.admin = True

    def atualizarFuncionario(self):
        banco = BancoAdministradores()
        try:
            c = banco.conexao.cursor()

            query = """update usuarios set nome=?, cpf=?, email=?, senha=?, nascimento=?, telefone=?, emailNotificacoes=? where email = ?"""
            c.execute(query, (self.nome, self.cpf, self.email, self.senha, self.nascimento, self.telefone, self.emailNotificacoes, self.email))

            banco.conexao.commit()
            c.close()

            return "Administrador atualizado"
        except:
            return "Erro ao atualizar administrador"

    def cadastrarAdmin(self):
        banco = BancoAdministradores()

        try:
            c = banco.conexao.cursor()

            c.execute("insert into usuarios (nome, cpf, nascimento, email, senha, telefone, admin, emailNotificacoes) values ('" +
                      self.nome + "', '" + self.cpf + "', '" + self.nascimento + "', '" + self.email + "', '" + self.senha + "', '" + self.telefone + "', '" + str(self.admin) + "', '" + self.emailNotificacoes + "' )")

            banco.conexao.commit()
            c.close()

            return "Admin cadastrado com sucesso!"
        except:
            return "Erro no cadastro do administrador"

    def login(self, email, senha):
        banco = BancoAdministradores()
        try:
            c = banco.conexao.cursor()

            query = """select * from usuarios where email = ?"""
            c.execute(query, (email,))
            dados = c.fetchall()

            for linha in dados:
                self.idAdministrador = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.email = linha[3]
                self.senha = linha[4]
                self.nascimento = linha[5]
                self.telefone = linha[6]
                self.emailNotificacoes = linha[7]
                self.admin = linha[8]

            c.close()
            if self.email == "":
                return "Conta admin não encontrada"
            elif not(email == self.email and senha == self.senha):
                return "Email ou senha admin incorretos, tente novamente"
            else:
                return "Login efetuado com sucesso"
        except:
            return "Erro no login do admin"

    def selecionarFuncionario(self, emailLogado):
        banco = BancoAdministradores()

        try:
            c = banco.conexao.cursor()

            query = """select * from usuarios where email = ?"""
            c.execute(query, (emailLogado,))
            dados = c.fetchall()

            for linha in dados:
                self.idAdministrador = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.email = linha[3]
                self.senha = linha[4]
                self.nascimento = linha[5]
                self.telefone = linha[6]
                self.emailNotificacoes = linha[7]
                self.admin = linha[8]   
            
            c.close()

            return "Administrador buscado com sucesso"
        except:
            return "Erro ao buscar administrador"