from Banco import Banco
from Endereco import Endereco


class Cliente():
    def __init__(self, nome="", cpf="", nascimento="", email="", senha="", telefone="", logradouro="", bairro="", cidade="", cep="", estado="", complemento="", numero="", idCliente=0):

        self.nome = nome
        self.idCliente = idCliente
        self.cpf = cpf
        self.nascimento = nascimento
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.endereco = Endereco(
            logradouro, bairro, cidade, cep, estado, complemento, numero)

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
        try:
            c = banco.conexao.cursor()

            c.execute("update usuarios set nome = '" + self.nome + "', cpf = '" +
                      self.cpf + "', nascimento = '" + self.nascimento + "', email = '" + self.email + "', senha = '" + self.senha + "', telefone = '" + self.telefone + "', logradouro = '" + self.endereco.logradouro + "', bairro = '" + self.endereco.bairro + "', cidade = '" + self.endereco.cidade + "', cep = '" + self.endereco.cep + "', estado = '" + self.endereco.estado + "', complemento = '" + self.endereco.complemento + "', numero = '" + self.endereco.numero + "' where idCliente = " + str(self.idCliente) + " ")

            banco.conexao.commit()
            c.close()

            return "Cliente atualizado com sucesso"
        except:
            return "Erro ao atualizar cliente"

    def deletarCliente(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from usuarios where idCliente = " +
                      str(self.idCliente) + " ")

            banco.conexao.commit()
            c.close()

            return "Cliente excluído com sucesso"
        except:
            return "Ocorreu um erro na exclusão do cliente"

    def login(self, idCliente, email, senha):  # usar com email e senha
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select * from usuarios where idCliente = " +
                      str(idCliente) + " ")

            for linha in c:
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

            if not (email == self.email and senha == self.senha):
                print("Email ou senha inválido, tente novamente")
            else:
                print("Login efetuado com sucesso")

            return "Busca feita com sucesso"
        except:
            return "Ocorreu um erro na busca do usuário"
