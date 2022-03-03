from tkinter import *
from Banco import Banco
from Cliente import Cliente
from Endereco import Endereco


cliente = Cliente("Caio", "123123123", "18-06-2003", "caioprsilva@gmail.com", "caiopra", "48999154099",
                  "Rua do Caçador", "Caçador", "Capivari de Baixo", "88745000", "SC", "casa", "1030")

# print(cliente.cadastrarCliente())

# cliente = Cliente("Caio Pra", "456456456", "18-06-2003", "caioprsilva@gmail.com", "caiopra", "48999154099",
#                   "Rua do Caçador", "Caçador", "Capivari de Baixo", "88745000", "SC", "casa", "1030", "8")
# print(cliente.atualizarCliente())

print(cliente.login(3, "caioprsilva@gmail.com", "caio"))


class Application():
    def __init__(self, master=None):
        self.fonte = ("Century Gothic", "10")

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

        # TODO: remodelar textos
        # Titulo
        self.titulo = Label(self.container1, text="Entrar/cadastrar conta: ")
        self.titulo["font"] = ("Century Gothic", "12", "bold")
        self.titulo.pack()

        # input IdCliente
        self.lblIdCliente = Label(
            self.container2, text="idCliente", font=self.fonte, width=10)
        self.lblIdCliente.pack(side=LEFT)

        self.txtIdCliente = Entry(self.container2)
        self.txtIdCliente["width"] = 12
        self.txtIdCliente["font"] = self.fonte
        self.txtIdCliente.pack(side=LEFT)

        # botao de buscar ao lado do IdCliente
        self.btnBuscar = Button(
            self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarUsuario
        self.btnBuscar.pack(side=RIGHT)

        # input nome do usuario
        self.lblNome = Label(self.container3, text="Nome: ",
                             font=self.fonte, width=10)
        self.lblNome.pack(side=LEFT)

        self.txtNome = Entry(self.container3)
        self.txtNome["width"] = 25
        self.txtNome["font"] = self.fonte
        self.txtNome.pack(side=LEFT)

        # input CPF
        self.lblCpf = Label(
            self.container4, text="CPF: ", font=self.fonte, width=10)
        self.lblCpf.pack(side=LEFT)

        self.txtCpf = Entry(self.container4)
        self.txtCpf["width"] = 25
        self.txtCpf["font"] = self.fonte
        self.txtCpf.pack(side=LEFT)

        # input nascimento
        # TODO: adicionar placeholder aos campos
        self.lblNascimento = Label(
            self.container5, text="Data de \nNascimento: ", font=self.fonte, width=10)
        self.lblNascimento.pack(side=LEFT)

        self.txtDia = Entry(self.container5)
        self.txtDia["width"] = 5
        self.txtDia["font"] = self.fonte
        self.txtDia.pack(side=LEFT, padx=5)

        self.txtMes = Entry(self.container5)
        self.txtMes["width"] = 5
        self.txtMes["font"] = self.fonte
        self.txtMes.pack(side=LEFT, padx=5)

        self.txtAno = Entry(self.container5)
        self.txtAno["width"] = 6
        self.txtAno["font"] = self.fonte
        self.txtAno.pack(side=LEFT, padx=5)

        # input email
        self.lblEmail = Label(
            self.container6, text="Email: ", font=self.fonte, width=10)
        self.lblEmail.pack(side=LEFT)

        self.txtEmail = Entry(self.container6)
        self.txtEmail["width"] = 25
        self.txtEmail["font"] = self.fonte
        self.txtEmail.pack(side=LEFT)

        # input senha
        self.lblSenha = Label(
        self.container7, text="Senha: ", font=self.fonte, width=10)
        self.lblSenha.pack(side=LEFT)

        self.txtSenha = Entry(self.container7)
        self.txtSenha["width"] = 25
        self.txtSenha["font"] = self.fonte
        self.txtSenha["show"] = "*"
        self.txtSenha.pack(side=LEFT)

    def buscarUsuario(self):  # TODO: implementar botão
        print("Clique do botão")


root = Tk()
Application(root)
root.mainloop()
