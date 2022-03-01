from Funcionario import Funcionario


class Administrador(Funcionario):
    def __init__(self, nome, idFuncionario, cpf, email, senha, nascimento, telefone, emailNotificacoes):
        Funcionario.__init__(self, nome, idFuncionario, cpf,
                             email, senha, nascimento, telefone)
        self.emailNotificacoes = emailNotificacoes
        self.admin = True

    def atualizarDados(self):
        pass
