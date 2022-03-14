from Banco import Banco
from Endereco import Endereco


class Cliente():
    def __init__(self, nome="", cpf="", nascimento="", email="", senha="", telefone="", logradouro="", bairro="", cidade="", cep="", estado="", complemento="", numero="", idCliente=0):

        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.endereco = Endereco(
            logradouro, bairro, cidade, cep, estado, complemento, numero)
        self.idCliente = idCliente

    def cadastrarCliente(self):
        banco = Banco()

        try:
            c = banco.conexao.cursor()

            c.execute("insert into usuarios (nome, cpf, nascimento, email, senha, telefone, logradouro, bairro, cidade, cep, estado, complemento, numero) values ('" +
                      self.nome + "', '" + self.cpf + "', '" + self.nascimento + "', '" + self.email + "', '" + self.senha + "', '" + self.telefone + "', '" + self.endereco.logradouro + "', '" + self.endereco.bairro + "', '" + self.endereco.cidade + "','" + self.endereco.cep + "', '" + self.endereco.estado + "', '" + self.endereco.complemento + "', '" + self.endereco.numero + "' )")

            banco.conexao.commit()
            c.close()

            return "Cliente cadastrado com sucesso!"
        except:
            return "Erro no cadastro do cliente"

    def atualizarCliente(self):
        banco = Banco()
        # try:
        c = banco.conexao.cursor()

        query = ("""update usuarios set nome = ?, cpf = ?, nascimento = ?, email = ?, senha = ?, telefone = ?, logradouro = ?, bairro = ?, cidade = ?, cep = ?, estado = ?, complemento = ?, numero = ? where email = ?""")

        c.execute(query, (self.nome, self.cpf, self.nascimento, self.email, self.senha, self.telefone, self.endereco.logradouro, self.endereco.bairro, self.endereco.cidade, self.endereco.cep, self.endereco.estado, self.endereco.complemento, self.endereco.numero, self.email))

        banco.conexao.commit()
        c.close()

        return "Cliente atualizado com sucesso"
        # except:
        #     return "Erro ao atualizar cliente"

    def login(self, email, senha):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            query = """select * from usuarios where email = ?"""
            c.execute(query, (email,))
            dados = c.fetchall()

            for linha in dados:
                self.idCliente = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.nascimento = linha[3]
                self.email = linha[4]
                self.senha = linha[5]
                self.telefone = linha[6]
                self.logradouro = linha[7]
                self.bairro = linha[8]
                self.cidade = linha[9]
                self.cep = linha[10]
                self.estado = linha[11]
                self.complemento = linha[12]
                self.numero = linha[13]

            c.close()

            if self.email == "":
                return "Conta não encontrada"
            elif not (email == self.email and senha == self.senha):
                return "Email ou senha incorretos, tente novamente"
            else:
                return "Login efetuado com sucesso"
        except:
            return "Ocorreu um erro no login do cliente"

    def selecionarCliente(self, emailLogado):
        banco = Banco()

        try:
            c = banco.conexao.cursor()

            query = """select * from usuarios where email = ?"""
            c.execute(query, (emailLogado, ))
            dados = c.fetchall()

            for linha in dados:
                self.idCliente = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.nascimento = linha[3]
                self.email = linha[4]
                self.senha = linha[5]
                self.telefone = linha[6]
                self.logradouro = linha[7]
                self.bairro = linha[8]
                self.cidade = linha[9]
                self.cep = linha[10]
                self.estado = linha[11]
                self.complemento = linha[12]
                self.numero = linha[13]

            c.close()

            return "Cliente buscado  com sucesso"
        except:
            return "Ocorreu um erro no login do cliente"
