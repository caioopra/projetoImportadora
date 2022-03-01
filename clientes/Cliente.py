from Endereco import Endereco

class Cliente():
    def __init__(self, nome="", idCliente=0, cpf="", nascimento="", email="", senha="", telefone="", logradouro="", bairro="", cidade="", cep="", estado="", complemento="", numero=""):

        self.nome = nome
        self.idCliente = idCliente
        self.cpf = cpf
        self.nascimento = nascimento
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.endereco = Endereco(logradouro, bairro, cidade, cep, estado, complemento, numero)

    def cadastrarCliente(self):
        pass

    def atualizarCliente(self):
        pass

    def deletarCliente(self):
        pass

    def login(self):  # usar com email e senha
        pass
