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
                        self.cpf + "', nascimento = '" + self.nascimento + "', email = '" + self.email + "', senha = '" + self.senha + "', telefone = '" + self.telefone + "', logradouro = '" + self.endereco.logradouro + "', bairro = '" + self.endereco.bairro + "', cidade = '" + self.endereco.cidade + "', cep = '" + self.endereco.cep + "', estado = '" + self.endereco.estado + "', complemento = '" + self.endereco.complemento + "', numero = '" + self.endereco.numero + "' where idCliente = " + str(self.idCliente) +" ")

            banco.conexao.commit()
            c.close()

            return "Cliente atualizado com sucesso"
        except:
            return "Erro ao atualizar cliente"


    def deletarCliente(self):
        pass

    def login(self):  # usar com email e senha
        pass
