from BancoFuncionarios import BancoFuncionarios


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

    def atualizarDados(self):
        pass

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
                print(dados)
                return "Login efetuado com sucesso"
        except:
            return "Erro no login do funcionario"
