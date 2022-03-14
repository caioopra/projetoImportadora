from Funcionario import Funcionario
from Endereco import Endereco
from BancoFuncionarios import BancoClientesFuncionarios


class ClienteFuncionario():
    def __init__(self, funcionario="", desconto="", logradouro="", bairro="", cidade="", cep="", estado="", complemento="", numero=""):
        self.funcionario = funcionario
        self.desconto = desconto
        self.endereco = Endereco(
            logradouro, bairro, cidade, cep, estado, complemento, numero)

    def atualizarDados(self):
        banco = BancoClientesFuncionarios()
        try:
            c = banco.conexao.cursor()

            query = """update usuarios set funcionario = ?, desconto = ?, logradouro = ?, bairro = ?, cidade = ?, cep = ?, estado = ?, complemento = ?, numero = ? where funcionario = ?"""
            c.execute(query, (self.funcionario, self.desconto, self.endereco.logradouro, self.endereco.bairro, self.endereco.cidade, self.endereco.cep, self.endereco.estado, self.endereco.complemento, self.endereco.numero, self.funcionario,))

            banco.conexao.commit()
            c.close()

            return "Funcionário atualizado"
        except:
            return "Erro ao atualizar funcionário"

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

    def getDados(self, emailLogado):
        banco = BancoClientesFuncionarios()

        try:
            c = banco.conexao.cursor()

            query = """select * from usuarios where funcionario = ?"""
            c.execute(query, (emailLogado,))
            dados = c.fetchall()

            for linha in dados:
                self.idClienteFuncionario = linha[0]
                self.funcionario = linha[1]
                self.desconto = linha[2]
                self.logradouro = linha[3]
                self.bairro = linha[4]
                self.cidade = linha[5]
                self.cep = linha[6]
                self.estado = linha[7]
                self.complemento = linha[8]
                self.numero = linha[9]
            
            c.close()

            return "Desconto encontrado"
        except:
            return "Erro ao buscar desconto"



