from Funcionario import Funcionario
from Endereco import Endereco
from BancoFuncionarios import BancoClientesFuncionarios


class ClienteFuncionario():
    def __init__(self, funcionario, desconto, logradouro, bairro, cidade, cep, estado, complemento, numero):
        self.funcionario = funcionario
        self.desconto = desconto
        self.endereco = Endereco(
            logradouro, bairro, cidade, cep, estado, complemento, numero)

    def atualizarDados(self):
        pass

    def cadastrarFuncionario(self):
        banco = BancoClientesFuncionarios()

        try:
            c = banco.conexao.cursor()

            c.execute("insert into usuarios (funcionario, desconto, logradouro, bairro, cidade, cep, estado, complemento, numero) values ('" + self.funcionario + "', '" + self.desconto + "', '" + self.endereco.logradouro + "', '" + self.endereco.bairro + "', '" + self.endereco.cidade + "', '" + self.endereco.cep + "', '" + self.endereco.estado + "', '"+self.endereco.complemento+"', '"+self.endereco.numero +"')")

            banco.conexao.commit()
            c.close()

            return "Cliente cadastrado com sucesso!"
        except:
            return "Erro no cadastro do cliente"


