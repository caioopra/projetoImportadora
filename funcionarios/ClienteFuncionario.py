from Funcionario import Funcionario
from clientes.Endereco import Endereco


class ClienteFuncionario(Funcionario):
    def __init__(self, nome, id, cpf, email, senha, admin, nascimento, telefone, desconto, logradouro, bairro, cidade, cep, estado, complemento, numero):
        Funcionario.__init__(self, nome, id, cpf, email,
                             senha, admin, nascimento, telefone)
        self.desconto = desconto
        self.endereco = Endereco(
            logradouro, bairro, cidade, cep, estado, complemento, numero)

    def atualizarDados(self):
        pass
