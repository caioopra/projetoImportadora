from tkinter import *
from Administrador import Administrador
from Cliente import Cliente
from Endereco import Endereco
from Funcionario import Funcionario


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
        self.titulo["font"] = ("Century Gothic", "15", "bold")
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

        email = self.txtEmail.get()
        senha = self.txtSenha.get()

        self.lblMsg["text"] = funcionario.login(email, senha)


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
            "Century Gothic", "12", "bold"), width=50)
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
        self.titulo["font"] = ("Century Gothic", "12", "bold")
        self.titulo.pack(side=LEFT, padx=60)

        self.vazio = Label(self.container1, text="",
                           font=fontePadrao, width=30)
        self.vazio.pack(side=LEFT)

        # botao voltar
        self.btnVoltar = Button(
            self.container1, text="Voltar", font=fontePadrao, width=10)
        self.btnVoltar["command"] = self.voltarPagina
        self.btnVoltar.pack(side=LEFT, padx=40)

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
        self.titulo.pack(side=LEFT, padx=30)

        # botao para voltar a selecao de tipo de usuario
        self.btnVoltar = Button(
            self.container1, text="Voltar", font=fontePadrao, width=10)
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

        # botao de login TODO: criar login (Cliente possui metodo login)
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
        self.master.title("Seleção cliente")
        centralizarJanela(self.master, 600, 200)
        ContaCliente(self.master)
        self.master.mainloop()

    def loginFuncionario(self):
        cliente = Cliente()

        email = self.txtEmail.get()
        senha = self.txtSenha.get()

        self.lblMsg["text"] = cliente.login(email, senha)

        # TODO: criar próxima tela (primeiro criar Funcionario/Adm e produtos/moeda)


class ClienteLogado():
    pass


class FuncionarioLogado():
    def __init__(self, master=None):
        self.master = master


        # TODO: continuar a criar a tela
            # botões: conta, produtos, ?moedas?

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
