from Banco import Banco
from BancoFuncionarios import BancoFuncionarios, BancoClientesFuncionarios


class Funcionario():
    def __init__(self, nome="",  cpf="", nascimento="", email="", senha="", telefone="", idFuncionario=""):

        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.admin = False
        self.nascimento = nascimento
        self.telefone = telefone
        self.idFuncionario = idFuncionario

    # TODO: usar essa função dentro do admin para cadastrar um funcionario
    # def cadastrarFuncionario(self):
    #     banco = BancoFuncionarios()

    #     try:
    #         c = banco.conexao.cursor()

    #         c.execute("insert into usuarios (nome, cpf, nascimento, email, senha, telefone, admin) values ('" +
    #                   self.nome + "', '" + self.cpf + "', '" + self.nascimento + "', '" + self.email + "', '" + self.senha + "', '" + self.telefone + "', '" + str(self.admin) + "' )")

    #         banco.conexao.commit()
    #         c.close()

    #         return "Cliente cadastrado com sucesso!"
    #     except:
    #         return "Erro no cadastro do cliente"

    def atualizarFuncionario(self):
        banco = BancoFuncionarios()
        try:
            c = banco.conexao.cursor()
            
            query = """update usuarios set nome = ?, cpf = ?, nascimento = ?, email = ?, senha = ?, telefone = ?, admin = ? where email = ?"""
            c.execute(query, (self.nome, self.cpf, self.nascimento, self.email, self.senha, self.telefone, self.admin, self.email))

            banco.conexao.commit()
            c.close()

            return "Funcionário atualizado com sucesso"
        except:
            return "Erro ao atualizar"

    def login(self, email, senha):
        banco = BancoFuncionarios()
        try:
            c = banco.conexao.cursor()

            query = """select * from usuarios where email = ?"""
            c.execute(query, (email,))
            dados = c.fetchall()

            for linha in dados:
                self.idFuncionario = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.nascimento = linha[3]
                self.email = linha[4]
                self.senha = linha[5]
                self.telefone = linha[6]
                self.admin = linha[7]

            c.close()
            if self.email == "":
                return "Conta funcionario não encontrada"
            elif not(email == self.email and senha == self.senha):
                return "Email ou senha funcionario incorretos, tente novamente"
            else:
                return "Login efetuado com sucesso"
        except:
            return "Erro no login do funcionario"

    def verificarCliente(self, email):  # verifica se um dado funcionario é também cliente
        bancoFuncionariosClientes = BancoClientesFuncionarios()

        c = bancoFuncionariosClientes.conexao.cursor()

        query = """select funcionario from usuarios where funcionario = ?"""

        c.execute(query, (email,))
        emailC = c.fetchall()
        c.close()

        if emailC == []:
            return "Não é cliente"
        elif emailC[0][0] == email:
            return "Cliente"
        else:
            return "Não é cliente"

    def selecionarFuncionario(self, emailLogado):
        banco = BancoFuncionarios()

        try:
            c = banco.conexao.cursor()

            query = """select * from usuarios where email = ?"""
            c.execute(query, (emailLogado,))
            dados = c.fetchall()

            for linha in dados:
                self.idFuncionario = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.nascimento = linha[3]
                self.email = linha[4]
                self.senha = linha[5]
                self.telefone = linha[6]
                self.admin = linha[7]
            
            c.close()

            return "Funcionário buscado com sucesso"
        except:
            return "Erro ao buscar funcionaio"
