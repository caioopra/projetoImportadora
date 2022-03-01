class Funcionario():
    def __init__(self, nome, id, cpf, email, senha, admin, nascimento, telefone):
        self.nome = nome
        self.id = id
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.admin = admin
        self.nascimento = nascimento
        self.telefone = telefone

    def atualizarDados(self):
        pass

    def login(self, email, senha):
        pass
