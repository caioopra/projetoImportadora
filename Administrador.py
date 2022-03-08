from Funcionario import Funcionario
from BancoAdministradores import BancoAdministradores


class Administrador(Funcionario):
    def __init__(self, nome="", cpf="", email="", senha="", nascimento="", telefone="", emailNotificacoes="", idAdministrador=""):
        Funcionario.__init__(self, nome, cpf, nascimento,
                             email, senha, telefone, idAdministrador)
        self.emailNotificacoes = emailNotificacoes
        self.admin = True

    def atualizarDados(self):
        pass
