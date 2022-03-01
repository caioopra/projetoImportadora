class Funcionario():
    def __init__(self, nome, idFuncionario, cpf, email, senha, nascimento, telefone):
        self.nome = nome
        self.id = idFuncionario
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.admin = False
        self.nascimento = nascimento
        self.telefone = telefone

    def atualizarDados(self):
        pass

    def login(self, email, senha):
        pass
