from Funcionario import Funcionario
from clientes.Endereco import Endereco


class ClienteFuncionario():
    def __init__(self, funcionario, desconto, logradouro, bairro, cidade, cep, estado, complemento, numero):
        self.funcionario = funcionario
        self.desconto = desconto
        self.endereco = Endereco(
            logradouro, bairro, cidade, cep, estado, complemento, numero)

    def atualizarDados(self):
        pass
