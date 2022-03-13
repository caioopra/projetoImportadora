from tkinter import *
from Administrador import Administrador
from Cliente import Cliente
from Endereco import Endereco
from Funcionario import Funcionario
from Produto import atualizarCotacoes


class PaginaInicial():
    def __init__(self, master=None):
        self.master = master

        # criacao dos containers para a pagina principal
        self.container1 = Frame(master)
        self.container1["padx"] = 40
        self.container1["pady"] = 35
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        # titulo e botoes de navegacao
        self.titulo = Label(self.container1, text="Tipo de usuário")
        self.titulo["font"] = ("Century Gothic", "16", "bold")
        self.titulo.pack()

        self.botaoFuncionario = Button(
            self.container2, text="Funcionário", font=fontePadrao, width=14)
        self.botaoFuncionario["command"] = self.clickLoginFuncionario
        self.botaoFuncionario.pack(side=LEFT, padx=26)

        self.botaoCliente = Button(
            self.container2, text="Cliente", font=fontePadrao, width=14)
        self.botaoCliente.pack(side=LEFT, padx=8)
        self.botaoCliente["command"] = self.clickContaCliente

    def clickLoginFuncionario(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title("Login Funcionário")
        centralizarJanela(self.master, 600, 250)
        LoginFuncionario(self.master)
        self.master.mainloop()

    def clickContaCliente(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title("Cliente")
        centralizarJanela(self.master, 600, 200)
        ContaCliente(self.master)
        self.master.mainloop()


class LoginFuncionario():
    def __init__(self, master=None):
        self.master = master

        self.container1 = Frame(master, pady=10)
        self.container1.pack()

        self.container2 = Frame(master, padx=35, pady=5)
        self.container2.pack()

        self.container3 = Frame(master, padx=35, pady=5)
        self.container3.pack()

        self.container4 = Frame(master, padx=20, pady=15)
        self.container4.pack()

        self.container5 = Frame(master, pady=15)
        self.container5.pack()

        # titulo da pagina
        self.titulo = Label(self.container1, text="Login Funcionário", font=(
            "Century Gothic", "12", "bold"))
        self.titulo.pack(side=LEFT, padx=30)

        # botao para voltar a selecao de tipo de usuario
        self.btnVoltar = Button(
            self.container1, text="Voltar", font=fontePadrao, width=10)
        self.btnVoltar["command"] = self.voltarPagina
        self.btnVoltar.pack(side=LEFT, padx=20)

        # email
        self.lblEmail = Label(
            self.container2, text="Email: ", font=fontePadrao, width=10)
        self.lblEmail.pack(side=LEFT)

        self.txtEmail = Entry(self.container2, width=30, font=fontePadrao)
        self.txtEmail.pack(side=LEFT)

        # senha
        self.lblSenha = Label(
            self.container3, text="Senha: ", font=fontePadrao, width=10)
        self.lblSenha.pack(side=LEFT)

        self.txtSenha = Entry(self.container3, width=30, font=fontePadrao)
        self.txtSenha.pack(side=LEFT)

        # botao de login
        self.btnLogin = Button(
            self.container4, text="Login", font=fontePadrao, width=15)
        self.btnLogin["command"] = self.loginFuncionario
        self.btnLogin.pack(side=LEFT)

        self.lblMsg = Label(self.container5, text="", font=(
            "Century Gothic", "11", "italic"))
        self.lblMsg.pack()

    def voltarPagina(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title("Importadora")
        centralizarJanela(self.master, 600, 200)
        PaginaInicial(self.master)
        self.master.mainloop()

    def loginFuncionario(self):
        funcionario = Funcionario()
        administrador = Administrador()

        email = self.txtEmail.get()
        senha = self.txtSenha.get()

        self.lblMsg["text"] = funcionario.login(email, senha)

        if funcionario.login(email, senha) == "Login efetuado com sucesso":
            self.master.destroy()
            self.master = Tk()
            self.master.title("Funcionário")
            centralizarJanela(self.master, 600, 200)
            FuncionarioLogado(self.master, email)
            self.master.mainloop()

        # nesse caso, não tem aquele email como funcionario, pode ser um admin
        if funcionario.login(email, senha) != "Conta não encontrada":
            self.lblMsg["text"] = administrador.login(email, senha)

            if administrador.login(email, senha) == "Login efetuado com sucesso":
                self.master.destroy()
                self.master = Tk()
                self.master.title("Administrador")
                centralizarJanela(self.master, 600, 300)
                AdministradorLogado(self.master, email)
                self.master.mainloop()


class ContaCliente():
    def __init__(self, master=None):
        self.master = master

        self.container1 = Frame(master, padx=30, pady=15)
        self.container1.pack()

        self.container2 = Frame(master, padx=40, pady=25)
        self.container2.pack()

        self.container3 = Frame(master, padx=35, pady=5)
        self.container3.pack()

        # titulo
        self.titulo = Label(self.container1, text="Já possui cadastro no sistema?", font=(
            "Century Gothic", "14", "bold"), width=50)
        self.titulo.pack(side=LEFT, padx=10)

        # botao voltar
        self.btnVoltar = Button(
            self.container1, text="Voltar", font=fontePadrao, width=15)
        self.btnVoltar["command"] = self.voltarPagina
        self.btnVoltar.pack(side=LEFT)

        # botoes de selecao
        self.btnCadastrar = Button(
            self.container2, text="Cadastrar-se\nagora", font=fontePadrao, width=14)
        self.btnCadastrar["command"] = self.clickCadastrarCliente
        self.btnCadastrar.pack(side=LEFT, padx=25)

        self.btnLogin = Button(
            self.container2, text="Login", font=fontePadrao, width=14, height=2)
        self.btnLogin["command"] = self.clickLoginCliente
        self.btnLogin.pack(side=LEFT, padx=5)

    def voltarPagina(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title("Importadora")
        centralizarJanela(self.master, 600, 200)
        PaginaInicial(self.master)
        self.master.mainloop()

    def clickCadastrarCliente(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title("Cadastro Cliente")
        centralizarJanela(self.master, 650, 400)
        CadastroCliente(self.master)
        self.master.mainloop()

    def clickLoginCliente(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title("Login Cliente")
        centralizarJanela(self.master, 600, 250)
        LoginCliente(self.master)
        self.master.mainloop()


class CadastroCliente():
    def __init__(self, master=None):
        self.master = master

        # containers
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        # Titulo
        self.titulo = Label(self.container1, text="Cadastrar conta: ")
        self.titulo["font"] = ("Century Gothic", "14", "bold")
        self.titulo.pack(side=LEFT, padx=60)

        self.vazio = Label(self.container1, text="",
                           font=fontePadrao, width=30)
        self.vazio.pack(side=LEFT)

        # botao voltar
        self.btnVoltar = Button(
            self.container1, text="Voltar", font=fontePadrao, width=10)
        self.btnVoltar["command"] = self.voltarPagina
        self.btnVoltar.pack(side=LEFT, padx=30)

        # input nome do usuario
        self.lblNome = Label(self.container2, text="Nome: ",
                             font=fontePadrao, width=10)
        self.lblNome.pack(side=LEFT)

        self.txtNome = Entry(self.container2)
        self.txtNome["width"] = 25
        self.txtNome["font"] = fontePadrao
        self.txtNome.pack(side=LEFT)

        # input CPF
        self.lblCpf = Label(
            self.container3, text="CPF: ", font=fontePadrao, width=10)
        self.lblCpf.pack(side=LEFT)

        self.txtCpf = Entry(self.container3)
        self.txtCpf["width"] = 25
        self.txtCpf["font"] = fontePadrao
        self.txtCpf.pack(side=LEFT)

        # input nascimento
        self.lblNascimento = Label(
            self.container4, text="Data de \nNascimento\n[Dia|Mes|Ano]: ", font=fontePadrao, width=13)
        self.lblNascimento.pack(side=LEFT)

        self.txtDia = Entry(self.container4)
        self.txtDia["width"] = 5
        self.txtDia["font"] = fontePadrao
        self.txtDia.pack(side=LEFT, padx=5)

        self.txtMes = Entry(self.container4)
        self.txtMes["width"] = 5
        self.txtMes["font"] = fontePadrao
        self.txtMes.pack(side=LEFT, padx=5)

        self.txtAno = Entry(self.container4)
        self.txtAno["width"] = 6
        self.txtAno["font"] = fontePadrao
        self.txtAno.pack(side=LEFT, padx=5)

        # input email
        self.lblEmail = Label(
            self.container5, text="Email: ", font=fontePadrao, width=10)
        self.lblEmail.pack(side=LEFT)

        self.txtEmail = Entry(self.container5)
        self.txtEmail["width"] = 25
        self.txtEmail["font"] = fontePadrao
        self.txtEmail.pack(side=LEFT)

        # input senha
        self.lblSenha = Label(
            self.container6, text="Senha: ", font=fontePadrao, width=10)
        self.lblSenha.pack(side=LEFT)

        self.txtSenha = Entry(self.container6)
        self.txtSenha["width"] = 25
        self.txtSenha["font"] = fontePadrao
        self.txtSenha.pack(side=LEFT)

        # input telefone
        self.lblTelefone = Label(
            self.container7, text="Telefone: ", font=fontePadrao, width=10)
        self.lblTelefone.pack(side=LEFT)

        self.txtTelefone = Entry(self.container7)
        self.txtTelefone["width"] = 25
        self.txtTelefone["font"] = fontePadrao
        self.txtTelefone.pack(side=LEFT)

        # botao de cadastro
        self.btnCadastrar = Button(
            self.container8, text="Enviar", font=fontePadrao, width=12)
        self.btnCadastrar["command"] = self.cadastrarCliente
        self.btnCadastrar.pack(side=LEFT, padx=81)

        # input logradouro
        self.lblLogradouro = Label(
            self.container2, text="Logradouro: ", font=fontePadrao, width=10)
        self.lblLogradouro.pack(side=LEFT, padx=34)

        self.txtLogradouro = Entry(self.container2)
        self.txtLogradouro["width"] = 25
        self.txtLogradouro["font"] = fontePadrao
        self.txtLogradouro.pack(side=LEFT)

        # input bairro
        self.lblBairro = Label(
            self.container3, text="Bairro: ", font=fontePadrao, width=10)
        self.lblBairro.pack(side=LEFT, padx=34)

        self.txtBairro = Entry(self.container3)
        self.txtBairro["width"] = 25
        self.txtBairro["font"] = fontePadrao
        self.txtBairro.pack(side=LEFT)

        # input cidade
        self.lblCidade = Label(
            self.container4, text="Cidade: ", font=fontePadrao, width=10)
        self.lblCidade.pack(side=LEFT, padx=34)

        self.txtCidade = Entry(self.container4)
        self.txtCidade["width"] = 25
        self.txtCidade["font"] = fontePadrao
        self.txtCidade.pack(side=LEFT)

        # input cep
        self.lblCep = Label(
            self.container5, text="CEP: ", font=fontePadrao, width=11)
        self.lblCep.pack(side=LEFT, padx=30)

        self.txtCep = Entry(self.container5)
        self.txtCep["width"] = 25
        self.txtCep["font"] = fontePadrao
        self.txtCep.pack(side=LEFT)

        # input estado
        self.lblEstado = Label(
            self.container6, text="Estado: ", font=fontePadrao, width=10)
        self.lblEstado.pack(side=LEFT, padx=34)

        self.txtEstado = Entry(self.container6)
        self.txtEstado["width"] = 25
        self.txtEstado["font"] = fontePadrao
        self.txtEstado.pack(side=LEFT)

        # input complemento
        self.lblComplemento = Label(
            self.container7, text="Complemento: ", font=fontePadrao, width=12)
        self.lblComplemento.pack(side=LEFT, padx=27)

        self.txtComplemento = Entry(self.container7)
        self.txtComplemento["width"] = 25
        self.txtComplemento["font"] = fontePadrao
        self.txtComplemento.pack(side=LEFT)

        # input numero
        self.lblNumero = Label(
            self.container8, text="Numero: ", font=fontePadrao, width=18)
        self.lblNumero.pack(side=LEFT)

        self.txtNumero = Entry(self.container8)
        self.txtNumero["width"] = 25
        self.txtNumero["font"] = fontePadrao
        self.txtNumero.pack(side=LEFT)

        # mensagem de sucesso/erro
        self.lblMsg = Label(self.container9, text="",
                            font=("Century Gothic", "11", "italic"))
        self.lblMsg.pack()

    def voltarPagina(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title("Importadora")
        centralizarJanela(self.master, 600, 200)
        ContaCliente(self.master)
        self.master.mainloop()

    def cadastrarCliente(self):
        cliente = Cliente()
        endereco = Endereco()

        cliente.nome = self.txtNome.get()
        cliente.cpf = self.txtCpf.get()
        cliente.nascimento = f"{self.txtDia.get()}-{self.txtMes.get()}-{self.txtAno.get()}"
        cliente.email = self.txtEmail.get()
        cliente.senha = self.txtSenha.get()
        cliente.telefone = self.txtTelefone.get()
        endereco.logradouro = self.txtLogradouro.get()
        endereco.bairro = self.txtBairro.get()
        endereco.cidade = self.txtCidade.get()
        endereco.cep = self.txtCep.get()
        endereco.estado = self.txtEstado.get()
        endereco.complemento = self.txtComplemento.get()
        endereco.numero = self.txtNumero.get()
        cliente.endereco = endereco

        if (cliente.nome == "") or (cliente.cpf == "") or (cliente.email == "") or (cliente.senha == ""):
            self.lblMsg["text"] = "Insira todos os dados"
        else:
            self.lblMsg["text"] = cliente.cadastrarCliente()

            self.txtNome.delete(0, END)
            self.txtCpf.delete(0, END)
            self.txtDia.delete(0, END)
            self.txtMes.delete(0, END)
            self.txtAno.delete(0, END)
            self.txtEmail.delete(0, END)
            self.txtSenha.delete(0, END)
            self.txtTelefone.delete(0, END)
            self.txtLogradouro.delete(0, END)
            self.txtBairro.delete(0, END)
            self.txtCidade.delete(0, END)
            self.txtCep.delete(0, END)
            self.txtEstado.delete(0, END)
            self.txtComplemento.delete(0, END)
            self.txtNumero.delete(0, END)

            # redireciona para a pagina de login
            self.master.destroy()
            self.master = Tk()
            self.master.title("Login Cliente")
            centralizarJanela(self.master, 600, 250)
            LoginCliente(self.master)
            self.master.mainloop()


class FuncionarioLogado(): # TODO: WIP
    def __init__(self, master=None, emailLogado=""):
        self.master = master
        self.emailLogado = emailLogado

        self.container1 = Frame(master, padx=30, pady=15)
        self.container1.pack()

        self.container2 = Frame(master, padx=40, pady=25)
        self.container2.pack()

        self.container3 = Frame(master, padx=35, pady=5)
        self.container3.pack()

        self.container4 = Frame(master, padx=70, pady=5)
        self.container4.pack()

        # conteudo da pagina
        self.titulo = Label(self.container1, text="Selecione a opção", font=(
            "Century Gothic", "13", "bold"))
        self.titulo.pack(side=LEFT, padx=28)

        self.btnlogout = Button(
            self.container1, text="Sair", font=fontePadrao, width=11)
        self.btnlogout["command"] = self.logout
        self.btnlogout.pack(side=LEFT)

        self.btnProdutos = Button(self.container2, text="Produtos", font=(
            "Century Gothic", "12", "bold"), width=13, height=5)
        self.btnProdutos["command"] = self.acessarProdutos
        self.btnProdutos.pack(side=LEFT, padx=20)

        self.btnConta = Button(self.container2, text="Conta", font=(
            "Century Gothic", "12", "bold"), width=13, height=5)
        self.btnConta["command"] = self.acessarConta
        self.btnConta.pack(side=LEFT)

    def logout(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title("Importadora")
        centralizarJanela(self.master, 600, 200)
        PaginaInicial(self.master)
        self.master.mainloop()

    def acessarProdutos(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title("Produtos disponíveis")

        funcionario = Funcionario()

        if funcionario.verificarCliente(self.emailLogado) == "Cliente":
            centralizarJanela(self.master, 1200, 600)
            FuncionarioClienteProdutos(self.master, self.emailLogado)
        else:
            centralizarJanela(self.master, 1000, 600)
            FuncionarioProdutos(self.master, self.emailLogado)
        self.master.mainloop()

    def acessarConta(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title("Configurações da conta")

        funcionario = Funcionario()
        if funcionario.verificarCliente(self.emailLogado) == "Cliente":
            centralizarJanela(self.master, 650, 400)
            FuncionarioClienteConfigurar(self.master, self.emailLogado)
        else:
            centralizarJanela(self.master, 500, 300)
            FuncionarioConfigurarConta(self.master, self.emailLogado)
        self.master.mainloop()


class FuncionarioProdutos():  # TODO: implementar
    def __init__(self, master=None, emailLogado=""):
        self.master = master
        self.emailLogado = emailLogado


class FuncionarioClienteProdutos(): # TODO: implementar
    def __init__(self, master=None, emailLogado=""):
        self.master = master
        self.emailLogado = emailLogado

class FuncionarioConfigurarConta():
    def __init__(self, master=None, emailLogado=""):
        self.master = master
        self.emailLogado = emailLogado

        # containers
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        # Titulo
        self.titulo = Label(self.container1, text="Atualizar conta: ")
        self.titulo["font"] = ("Century Gothic", "14", "bold")
        self.titulo.pack(side=LEFT, padx=60)

        self.vazio = Label(self.container1, text="",
                           font=fontePadrao, width=30)
        self.vazio.pack(side=LEFT)

        # botao voltar
        self.btnVoltar = Button(
            self.container1, text="Voltar", font=fontePadrao, width=10)
        self.btnVoltar["command"] = self.voltarPagina
        self.btnVoltar.pack(side=LEFT, padx=30)

        # input nome do usuario
        self.lblNome = Label(self.container2, text="Nome: ",
                             font=fontePadrao, width=10)
        self.lblNome.pack(side=LEFT)

        self.txtNome = Entry(self.container2)
        self.txtNome["width"] = 25
        self.txtNome["font"] = fontePadrao
        self.txtNome.pack(side=LEFT)

        # input CPF
        self.lblCpf = Label(
            self.container3, text="CPF: ", font=fontePadrao, width=10)
        self.lblCpf.pack(side=LEFT)

        self.txtCpf = Entry(self.container3)
        self.txtCpf["width"] = 25
        self.txtCpf["font"] = fontePadrao
        self.txtCpf.pack(side=LEFT)

        # input nascimento
        self.lblNascimento = Label(
            self.container4, text="Data de \nNascimento\n[Dia|Mes|Ano]: ", font=fontePadrao, width=13)
        self.lblNascimento.pack(side=LEFT)

        self.txtDia = Entry(self.container4)
        self.txtDia["width"] = 5
        self.txtDia["font"] = fontePadrao
        self.txtDia.pack(side=LEFT, padx=5)

        self.txtMes = Entry(self.container4)
        self.txtMes["width"] = 5
        self.txtMes["font"] = fontePadrao
        self.txtMes.pack(side=LEFT, padx=5)

        self.txtAno = Entry(self.container4)
        self.txtAno["width"] = 6
        self.txtAno["font"] = fontePadrao
        self.txtAno.pack(side=LEFT, padx=5)

        # input senha
        self.lblSenha = Label(
            self.container5, text="Senha: ", font=fontePadrao, width=10)
        self.lblSenha.pack(side=LEFT)

        self.txtSenha = Entry(self.container5)
        self.txtSenha["width"] = 25
        self.txtSenha["font"] = fontePadrao
        self.txtSenha.pack(side=LEFT)

        # input telefone
        self.lblTelefone = Label(
            self.container6, text="Telefone: ", font=fontePadrao, width=10)
        self.lblTelefone.pack(side=LEFT)

        self.txtTelefone = Entry(self.container6)
        self.txtTelefone["width"] = 25
        self.txtTelefone["font"] = fontePadrao
        self.txtTelefone.pack(side=LEFT)

        self.labelVazio = Label(self.container7, text="  ", width=37)
        self.labelVazio.pack(side=LEFT)

        # botao de atualizacao
        self.btnAtualizar = Button(
            self.container8, text="Atualizar", font=fontePadrao, width=12)
        self.btnAtualizar["command"] = self.atualizarClientePagina
        self.btnAtualizar.pack(side=LEFT, padx=81)

        # input logradouro
        self.lblLogradouro = Label(
            self.container2, text="Logradouro: ", font=fontePadrao, width=10)
        self.lblLogradouro.pack(side=LEFT, padx=34)

        self.txtLogradouro = Entry(self.container2)
        self.txtLogradouro["width"] = 25
        self.txtLogradouro["font"] = fontePadrao
        self.txtLogradouro.pack(side=LEFT)

        # input bairro
        self.lblBairro = Label(
            self.container3, text="Bairro: ", font=fontePadrao, width=10)
        self.lblBairro.pack(side=LEFT, padx=34)

        self.txtBairro = Entry(self.container3)
        self.txtBairro["width"] = 25
        self.txtBairro["font"] = fontePadrao
        self.txtBairro.pack(side=LEFT)

        # input cidade
        self.lblCidade = Label(
            self.container4, text="Cidade: ", font=fontePadrao, width=10)
        self.lblCidade.pack(side=LEFT, padx=34)

        self.txtCidade = Entry(self.container4)
        self.txtCidade["width"] = 25
        self.txtCidade["font"] = fontePadrao
        self.txtCidade.pack(side=LEFT)

        # input cep
        self.lblCep = Label(
            self.container5, text="CEP: ", font=fontePadrao, width=11)
        self.lblCep.pack(side=LEFT, padx=30)

        self.txtCep = Entry(self.container5)
        self.txtCep["width"] = 25
        self.txtCep["font"] = fontePadrao
        self.txtCep.pack(side=LEFT)

        # input estado
        self.lblEstado = Label(
            self.container6, text="Estado: ", font=fontePadrao, width=10)
        self.lblEstado.pack(side=LEFT, padx=34)

        self.txtEstado = Entry(self.container6)
        self.txtEstado["width"] = 25
        self.txtEstado["font"] = fontePadrao
        self.txtEstado.pack(side=LEFT)

        # input complemento
        self.lblComplemento = Label(
            self.container7, text="Complemento: ", font=fontePadrao, width=12)
        self.lblComplemento.pack(side=LEFT, padx=27)

        self.txtComplemento = Entry(self.container7)
        self.txtComplemento["width"] = 25
        self.txtComplemento["font"] = fontePadrao
        self.txtComplemento.pack(side=LEFT)

        # input numero
        self.lblNumero = Label(
            self.container8, text="Numero: ", font=fontePadrao, width=18)
        self.lblNumero.pack(side=LEFT)

        self.txtNumero = Entry(self.container8)
        self.txtNumero["width"] = 25
        self.txtNumero["font"] = fontePadrao
        self.txtNumero.pack(side=LEFT)

        # mensagem de sucesso/erro
        self.lblMsg = Label(self.container9, text="",
                            font=("Century Gothic", "11", "italic"))
        self.lblMsg.pack()

        self.buscarCliente()

    def voltarPagina(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title("Funcionario")
        centralizarJanela(self.master, 600, 200)
        FuncionarioLogado(self.master, self.emailLogado)
        self.master.mainloop()

    def buscarCliente(self):
        cliente = Cliente()

        cliente.selecionarCliente(self.emailLogado)

        self.txtNome.insert(INSERT, cliente.nome)
        self.txtCpf.insert(INSERT, cliente.cpf)
        nascimento = cliente.nascimento.split("-")
        self.txtDia.insert(INSERT, nascimento[0])
        self.txtMes.insert(INSERT, nascimento[1])
        self.txtAno.insert(INSERT, nascimento[2])
        self.txtSenha.insert(INSERT, cliente.senha)
        self.txtTelefone.insert(INSERT, cliente.telefone)
        self.txtLogradouro.insert(INSERT, cliente.logradouro)
        self.txtBairro.insert(INSERT, cliente.bairro)
        self.txtCidade.insert(INSERT, cliente.cidade)
        self.txtCep.insert(INSERT, cliente.cep)
        self.txtEstado.insert(INSERT, cliente.estado)
        self.txtComplemento.insert(INSERT, cliente.complemento)
        self.txtNumero.insert(INSERT, cliente.numero)

    def atualizarClientePagina(self):
        cliente = Cliente()
        endereco = Endereco()

        cliente.nome = self.txtNome.get()
        cliente.cpf = self.txtCpf.get()
        cliente.nascimento = f"{self.txtDia.get()}-{self.txtMes.get()}-{self.txtAno.get()}"
        cliente.email = self.emailLogado
        cliente.senha = self.txtSenha.get()
        cliente.telefone = self.txtTelefone.get()
        endereco.logradouro = self.txtLogradouro.get()
        endereco.bairro = self.txtBairro.get()
        endereco.cidade = self.txtCidade.get()
        endereco.cep = self.txtCep.get()
        endereco.estado = self.txtEstado.get()
        endereco.complemento = self.txtComplemento.get()
        endereco.numero = self.txtNumero.get()
        cliente.endereco = endereco

        self.lblMsg["text"] = cliente.atualizarCliente()

        # redireciona para a pagina padrão do cliente
        self.master.destroy()
        self.master = Tk()
        self.master.title("Login Cliente")
        centralizarJanela(self.master, 600, 200)
        ClienteLogado(self.master, self.emailLogado)
        self.master.mainloop()


class FuncionarioClienteConfigurar():  # TODO: copiar
    def __init__(self, master=None, emailLogado=""):
        self.master = master
        self.emailLogado = emailLogado


class AdministradorLogado():  # TODO: implementar/copiar
    def __init__(self, master=None, emailLogado=""):
        self.master = master
        self.emailLogado = emailLogado


class LoginCliente():
    def __init__(self, master=None):
        self.master = master

        self.container1 = Frame(master, pady=10)
        self.container1.pack()

        self.container2 = Frame(master, padx=35, pady=5)
        self.container2.pack()

        self.container3 = Frame(master, padx=35, pady=5)
        self.container3.pack()

        self.container4 = Frame(master, padx=20, pady=15)
        self.container4.pack()

        self.container5 = Frame(master, pady=15)
        self.container5.pack()

        # titulo da pagina
        self.titulo = Label(self.container1, text="Login Cliente", font=(
            "Century Gothic", "12", "bold"))
        self.titulo.pack(side=LEFT, padx=28)

        # botao para voltar a selecao de tipo de usuario
        self.btnVoltar = Button(
            self.container1, text="Voltar", font=fontePadrao, width=11)
        self.btnVoltar["command"] = self.voltarPagina
        self.btnVoltar.pack(side=LEFT)

        # email
        self.lblEmail = Label(
            self.container2, text="Email: ", font=fontePadrao, width=10)
        self.lblEmail.pack(side=LEFT)

        self.txtEmail = Entry(self.container2, width=30, font=fontePadrao)
        self.txtEmail.pack(side=LEFT)

        # senha
        self.lblSenha = Label(
            self.container3, text="Senha: ", font=fontePadrao, width=10)
        self.lblSenha.pack(side=LEFT)

        self.txtSenha = Entry(self.container3, width=30, font=fontePadrao)
        self.txtSenha.pack(side=LEFT)

        self.btnLogin = Button(
            self.container4, text="Login", font=fontePadrao, width=15)
        self.btnLogin["command"] = self.loginCliente
        self.btnLogin.pack(side=LEFT)

        self.lblMsg = Label(self.container5, text="", font=(
            "Century Gothic", "11", "italic"))
        self.lblMsg.pack()

    def voltarPagina(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title("Seleção cliente")
        centralizarJanela(self.master, 600, 200)
        ContaCliente(self.master)
        self.master.mainloop()

    def loginCliente(self):
        cliente = Cliente()

        email = self.txtEmail.get()
        senha = self.txtSenha.get()

        self.lblMsg["text"] = cliente.login(email, senha)

        if cliente.login(email, senha) == "Login efetuado com sucesso":
            self.master.destroy()
            self.master = Tk()
            self.master.title("Cliente")
            centralizarJanela(self.master, 600, 200)
            ClienteLogado(self.master, email)
            self.master.mainloop()


class ClienteLogado():
    def __init__(self, master=None, emailLogado=""):
        self.master = master
        self.emailLogado = emailLogado

        self.container1 = Frame(master, pady=10)
        self.container1.pack()

        self.container2 = Frame(master, padx=35, pady=15)
        self.container2.pack()

        self.container3 = Frame(master, padx=35, pady=5)
        self.container3.pack()

        # conteudo da pagina
        self.titulo = Label(self.container1, text="Selecione a opção", font=(
            "Century Gothic", "13", "bold"))
        self.titulo.pack(side=LEFT, padx=28)

        self.btnlogout = Button(
            self.container1, text="Sair", font=fontePadrao, width=11)
        self.btnlogout["command"] = self.logout
        self.btnlogout.pack(side=LEFT)

        self.btnProdutos = Button(self.container2, text="Produtos", font=(
            "Century Gothic", "12", "bold"), width=13, height=5)
        self.btnProdutos["command"] = self.acessarProdutos
        self.btnProdutos.pack(side=LEFT, padx=20)

        self.btnConta = Button(self.container2, text="Conta", font=(
            "Century Gothic", "12", "bold"), width=13, height=5)
        self.btnConta["command"] = self.acessarConta
        self.btnConta.pack(side=LEFT)

    def logout(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title("Importadora")
        centralizarJanela(self.master, 600, 200)
        PaginaInicial(self.master)
        self.master.mainloop()

    def acessarProdutos(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title("Produtos disponíveis")
        centralizarJanela(self.master, 1000, 600)
        ClienteProdutosDisponiveis(self.master, self.emailLogado)
        self.master.mainloop()

    def acessarConta(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title("Configurações da conta")
        centralizarJanela(self.master, 650, 400)
        ClienteConfigurarConta(self.master, self.emailLogado)
        print(self.emailLogado)
        self.master.mainloop()


class ClienteProdutosDisponiveis():
    def __init__(self, master=None, emailLogado=""):
        self.master = master
        self.emailLogado = emailLogado

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 5
        self.container8.pack()

        # conteudo da pagina
        self.titulo = Label(self.container1, text="Produtos", font=(
            "Century Gothic", "14", "bold"), width=65)
        self.titulo.pack(side=LEFT, padx=30)

        self.btnVoltar = Button(
            self.container1, text="Voltar", font=fontePadrao, width=15)
        self.btnVoltar["command"] = self.voltarPagina
        self.btnVoltar.pack(side=LEFT)

        # labels
        self.lblNome = Label(self.container2, text="Produto", font=(
            "Century Gothic", "12", "bold"), width=20)
        self.lblNome.pack(side=LEFT, padx=5, pady=25)

        self.lblQuantidade = Label(self.container2, text="Quantidade", font=(
            "Century Gothic", "12", "bold"), width=20)
        self.lblQuantidade.pack(side=LEFT, padx=5, pady=10)

        self.lblPreco = Label(self.container2, text="Preço (R$)", font=(
            "Century Gothic", "12", "bold"), width=20)
        self.lblPreco.pack(side=LEFT, padx=5, pady=15)

        self.lblVazia = Label(self.container2, text=" ",
                              font=fontePadrao, width=40)
        self.lblVazia.pack(side=LEFT, padx=5, pady=15)

        # puxar lista dos produtos disponiveis
        listaProdutos = atualizarCotacoes()[1]
        print("Lista de todos produtos: ", listaProdutos)

        if len(listaProdutos) % 4 == 0:
            quantidadeListas = len(listaProdutos) / 4
        else:
            quantidadeListas = (len(listaProdutos) // 4) + 1

        # cria matriz com listas de até 4 produtos em cada linha
        self.matrizProdutos = [0] * quantidadeListas
        for i in range(quantidadeListas):
            self.matrizProdutos[i] = listaProdutos[(4 * i):(4 * i + 4)]

        print(self.matrizProdutos)
        # TODO: criar tratamento para os produtos indisponiveis

        self.listaContainers = [self.container3,
                                self.container4, self.container5, self.container6]
        # mostra na tela os produtos daquela linha da matriz
        self.paginaAtual = 0
        self.objetosMostrados = self.mostrarProdutos(
            self.matrizProdutos[self.paginaAtual])

        # botoes de navegacao entre as paginas
        self.btnProxima = Button(
            self.container7, text="Próxima\nPágina", font=fontePadrao, width=16)
        self.btnProxima["command"] = lambda: self.paginaSeguinte(
            self.matrizProdutos[self.paginaAtual + 1], self.objetosMostrados)
        self.btnProxima.pack(side=RIGHT, padx=15)

        self.btnAnterior = Button(
            self.container7, text="Página\nAnterior", font=fontePadrao, width=16)
        self.btnAnterior["command"] = lambda: self.paginaAnterior(
            self.matrizProdutos[self.paginaAtual - 1], self.objetosMostrados)

        if self.paginaAtual == 0:
            self.btnAnterior["state"] = DISABLED
        else:
            self.btnAnterior["state"] = NORMAL
        self.btnAnterior.pack(side=RIGHT, padx=15)

        # mensagem ao comprar produto
        self.lblCompra = Label(self.container8, text="",
                               font=("Century Gothic", "10", "italic"))
        self.lblCompra.pack()

    def mostrarProdutos(self, lista):
        listaObjetosMostrados = []

        for j in range(len(lista)):  # coloca os elementos da mesma lista na tela (max = 4)
            self.labelNomeProduto = Label(
                self.listaContainers[j], text=lista[j].produto, font=fontePadrao, width=30)
            self.labelNomeProduto.pack(side=LEFT, pady=15)

            self.labelQuantidade = Label(
                self.listaContainers[j], text=lista[j].qtdDisponivel, font=fontePadrao, width=20)
            self.labelQuantidade.pack(side=LEFT, padx=5, pady=10)

            self.labelValorVenda = Label(
                self.listaContainers[j], text=f"R${lista[j].valorVenda}", font=fontePadrao, width=20)
            self.labelValorVenda.pack(side=LEFT, padx=5, pady=15)

            self.btnComprar = Button(
                self.listaContainers[j], text="Comprar!", font=fontePadrao, width=40)
            self.btnComprar["command"] = lista[j].comprar
            self.btnComprar.pack(side=LEFT, padx=5, pady=15)

            listaObjetosMostrados.append(self.labelNomeProduto)
            listaObjetosMostrados.append(self.labelQuantidade)
            listaObjetosMostrados.append(self.labelValorVenda)
            listaObjetosMostrados.append(self.btnComprar)

        self.objetosMostrados = listaObjetosMostrados.copy()
        return listaObjetosMostrados

    def removerDaTela(self, lista):
        for objeto in lista:
            objeto.destroy()

    def paginaSeguinte(self, listaProd, listaRemover):
        self.removerDaTela(listaRemover)

        if not (self.paginaAtual + 1 > len(self.matrizProdutos) - 1):
            self.paginaAtual += 1
            self.mostrarProdutos(listaProd)

        if self.paginaAtual == (len(self.matrizProdutos) - 1):
            self.btnProxima["state"] = DISABLED
        else:
            self.btnProxima["state"] = NORMAL

        if self.paginaAtual == 0:
            self.btnAnterior["state"] = DISABLED
        else:
            self.btnAnterior["state"] = NORMAL

    def paginaAnterior(self, listaProd, listaRemover):
        self.removerDaTela(listaRemover)

        if self.paginaAtual - 1 >= 0:
            self.paginaAtual -= 1
            self.mostrarProdutos(listaProd)

        if self.paginaAtual == 0:
            self.btnAnterior["state"] = DISABLED
        else:
            self.btnAnterior["state"] = NORMAL

        if self.paginaAtual == (len(self.matrizProdutos) - 1):
            self.btnProxima["state"] = DISABLED
        else:
            self.btnProxima["state"] = NORMAL

    def voltarPagina(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title("Cliente")
        centralizarJanela(self.master, 600, 200)
        ClienteLogado(self.master, self.emailLogado)


class ClienteConfigurarConta():
    def __init__(self, master=None, emailLogado=""):
        self.master = master
        self.emailLogado = emailLogado

        # containers
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        # Titulo
        self.titulo = Label(self.container1, text="Atualizar conta: ")
        self.titulo["font"] = ("Century Gothic", "14", "bold")
        self.titulo.pack(side=LEFT, padx=60)

        self.vazio = Label(self.container1, text="",
                           font=fontePadrao, width=30)
        self.vazio.pack(side=LEFT)

        # botao voltar
        self.btnVoltar = Button(
            self.container1, text="Voltar", font=fontePadrao, width=10)
        self.btnVoltar["command"] = self.voltarPagina
        self.btnVoltar.pack(side=LEFT, padx=30)

        # input nome do usuario
        self.lblNome = Label(self.container2, text="Nome: ",
                             font=fontePadrao, width=10)
        self.lblNome.pack(side=LEFT)

        self.txtNome = Entry(self.container2)
        self.txtNome["width"] = 25
        self.txtNome["font"] = fontePadrao
        self.txtNome.pack(side=LEFT)

        # input CPF
        self.lblCpf = Label(
            self.container3, text="CPF: ", font=fontePadrao, width=10)
        self.lblCpf.pack(side=LEFT)

        self.txtCpf = Entry(self.container3)
        self.txtCpf["width"] = 25
        self.txtCpf["font"] = fontePadrao
        self.txtCpf.pack(side=LEFT)

        # input nascimento
        self.lblNascimento = Label(
            self.container4, text="Data de \nNascimento\n[Dia|Mes|Ano]: ", font=fontePadrao, width=13)
        self.lblNascimento.pack(side=LEFT)

        self.txtDia = Entry(self.container4)
        self.txtDia["width"] = 5
        self.txtDia["font"] = fontePadrao
        self.txtDia.pack(side=LEFT, padx=5)

        self.txtMes = Entry(self.container4)
        self.txtMes["width"] = 5
        self.txtMes["font"] = fontePadrao
        self.txtMes.pack(side=LEFT, padx=5)

        self.txtAno = Entry(self.container4)
        self.txtAno["width"] = 6
        self.txtAno["font"] = fontePadrao
        self.txtAno.pack(side=LEFT, padx=5)

        # input senha
        self.lblSenha = Label(
            self.container5, text="Senha: ", font=fontePadrao, width=10)
        self.lblSenha.pack(side=LEFT)

        self.txtSenha = Entry(self.container5)
        self.txtSenha["width"] = 25
        self.txtSenha["font"] = fontePadrao
        self.txtSenha.pack(side=LEFT)

        # input telefone
        self.lblTelefone = Label(
            self.container6, text="Telefone: ", font=fontePadrao, width=10)
        self.lblTelefone.pack(side=LEFT)

        self.txtTelefone = Entry(self.container6)
        self.txtTelefone["width"] = 25
        self.txtTelefone["font"] = fontePadrao
        self.txtTelefone.pack(side=LEFT)

        self.labelVazio = Label(self.container7, text="  ", width=37)
        self.labelVazio.pack(side=LEFT)

        # botao de atualizacao
        self.btnAtualizar = Button(
            self.container8, text="Atualizar", font=fontePadrao, width=12)
        self.btnAtualizar["command"] = self.atualizarClientePagina
        self.btnAtualizar.pack(side=LEFT, padx=81)

        # input logradouro
        self.lblLogradouro = Label(
            self.container2, text="Logradouro: ", font=fontePadrao, width=10)
        self.lblLogradouro.pack(side=LEFT, padx=34)

        self.txtLogradouro = Entry(self.container2)
        self.txtLogradouro["width"] = 25
        self.txtLogradouro["font"] = fontePadrao
        self.txtLogradouro.pack(side=LEFT)

        # input bairro
        self.lblBairro = Label(
            self.container3, text="Bairro: ", font=fontePadrao, width=10)
        self.lblBairro.pack(side=LEFT, padx=34)

        self.txtBairro = Entry(self.container3)
        self.txtBairro["width"] = 25
        self.txtBairro["font"] = fontePadrao
        self.txtBairro.pack(side=LEFT)

        # input cidade
        self.lblCidade = Label(
            self.container4, text="Cidade: ", font=fontePadrao, width=10)
        self.lblCidade.pack(side=LEFT, padx=34)

        self.txtCidade = Entry(self.container4)
        self.txtCidade["width"] = 25
        self.txtCidade["font"] = fontePadrao
        self.txtCidade.pack(side=LEFT)

        # input cep
        self.lblCep = Label(
            self.container5, text="CEP: ", font=fontePadrao, width=11)
        self.lblCep.pack(side=LEFT, padx=30)

        self.txtCep = Entry(self.container5)
        self.txtCep["width"] = 25
        self.txtCep["font"] = fontePadrao
        self.txtCep.pack(side=LEFT)

        # input estado
        self.lblEstado = Label(
            self.container6, text="Estado: ", font=fontePadrao, width=10)
        self.lblEstado.pack(side=LEFT, padx=34)

        self.txtEstado = Entry(self.container6)
        self.txtEstado["width"] = 25
        self.txtEstado["font"] = fontePadrao
        self.txtEstado.pack(side=LEFT)

        # input complemento
        self.lblComplemento = Label(
            self.container7, text="Complemento: ", font=fontePadrao, width=12)
        self.lblComplemento.pack(side=LEFT, padx=27)

        self.txtComplemento = Entry(self.container7)
        self.txtComplemento["width"] = 25
        self.txtComplemento["font"] = fontePadrao
        self.txtComplemento.pack(side=LEFT)

        # input numero
        self.lblNumero = Label(
            self.container8, text="Numero: ", font=fontePadrao, width=18)
        self.lblNumero.pack(side=LEFT)

        self.txtNumero = Entry(self.container8)
        self.txtNumero["width"] = 25
        self.txtNumero["font"] = fontePadrao
        self.txtNumero.pack(side=LEFT)

        # mensagem de sucesso/erro
        self.lblMsg = Label(self.container9, text="",
                            font=("Century Gothic", "11", "italic"))
        self.lblMsg.pack()

        self.buscarCliente()

    def voltarPagina(self):
        self.master.destroy()
        self.master = Tk()
        self.master.title("Cliente")
        centralizarJanela(self.master, 600, 200)
        ClienteLogado(self.master, self.emailLogado)
        self.master.mainloop()

    def buscarCliente(self):
        cliente = Cliente()

        cliente.selecionarCliente(self.emailLogado)

        self.txtNome.insert(INSERT, cliente.nome)
        self.txtCpf.insert(INSERT, cliente.cpf)
        nascimento = cliente.nascimento.split("-")
        self.txtDia.insert(INSERT, nascimento[0])
        self.txtMes.insert(INSERT, nascimento[1])
        self.txtAno.insert(INSERT, nascimento[2])
        self.txtSenha.insert(INSERT, cliente.senha)
        self.txtTelefone.insert(INSERT, cliente.telefone)
        self.txtLogradouro.insert(INSERT, cliente.logradouro)
        self.txtBairro.insert(INSERT, cliente.bairro)
        self.txtCidade.insert(INSERT, cliente.cidade)
        self.txtCep.insert(INSERT, cliente.cep)
        self.txtEstado.insert(INSERT, cliente.estado)
        self.txtComplemento.insert(INSERT, cliente.complemento)
        self.txtNumero.insert(INSERT, cliente.numero)

    def atualizarClientePagina(self):
        cliente = Cliente()
        endereco = Endereco()

        cliente.nome = self.txtNome.get()
        cliente.cpf = self.txtCpf.get()
        cliente.nascimento = f"{self.txtDia.get()}-{self.txtMes.get()}-{self.txtAno.get()}"
        cliente.email = self.emailLogado
        cliente.senha = self.txtSenha.get()
        cliente.telefone = self.txtTelefone.get()
        endereco.logradouro = self.txtLogradouro.get()
        endereco.bairro = self.txtBairro.get()
        endereco.cidade = self.txtCidade.get()
        endereco.cep = self.txtCep.get()
        endereco.estado = self.txtEstado.get()
        endereco.complemento = self.txtComplemento.get()
        endereco.numero = self.txtNumero.get()
        cliente.endereco = endereco

        self.lblMsg["text"] = cliente.atualizarCliente()

        # redireciona para a pagina padrão do cliente
        self.master.destroy()
        self.master = Tk()
        self.master.title("Login Cliente")
        centralizarJanela(self.master, 600, 200)
        ClienteLogado(self.master, self.emailLogado)
        self.master.mainloop()


def centralizarJanela(janela, largura, altura):

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    coord_x = int((largura_tela/2) - largura/2)
    coord_y = int((altura_tela/2) - altura/2)
    janela.geometry(f"{largura}x{altura}+{coord_x}+{coord_y}")


fontePadrao = ("Century Gothic", "10")

root = Tk()
root.title("Importadora")
centralizarJanela(root, 600, 200)
PaginaInicial(root)
root.mainloop()
