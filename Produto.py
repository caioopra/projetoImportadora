from BancoProdutos import BancoMoedas, BancoProdutos
from forex_python.converter import CurrencyRates
from datetime import datetime


class Produto():
    def __init__(self, produto="", valorCompra="", moeda="", taxaLucro="", qtdDisponivel="", idProduto=""):
        self.produto = produto
        self.valorCompra = valorCompra
        self.moeda = moeda
        self.taxaLucro = taxaLucro
        self.qtdDisponivel = qtdDisponivel
        self.idProduto = idProduto

        # cria o preco de venda automaticamente quando o objeto e instanciado
        for i in range(len(listaMoedas)):
            if listaMoedas[i][2] == self.moeda:
                self.valorVenda = round(float(
                    self.valorCompra) * (1 + float(self.taxaLucro) / 100) * listaMoedas[i][3], 2)
                break

        if int(qtdDisponivel) > 0:
            self.disponivel = True
        else:
            self.disponivel = False

    def atualizar_valor(self, valorCompra, taxaLucro, moeda):
        pass

    def cadastrarProduto(self):
        banco = BancoProdutos()

        try:
            c = banco.conexao.cursor()
            c.execute(
                "insert into produtos (produto, valorCompra, moeda, taxaLucro, valorVenda, qtdDisponivel, disponivel) values ('" + self.produto + "', '" + str(self.valorCompra) + "', '" + self.moeda + "', '" + str(self.taxaLucro) + "', '" + str(self.valorVenda) + "', '" + str(self.qtdDisponivel) + "', '" + str(self.disponivel) + "') ")

            banco.conexao.commit()
            c.close()

            return "Produto adicionado com sucesso!"
        except:
            return "Erro ao adicionar produto"


class Moeda():
    def __init__(self, nome="", sigla="", cotacao="", horarioAtualizacao="", idMoeda=""):

        self.nome = nome
        self.sigla = sigla
        self.cotacao = cotacao
        self.horarioAtualizacao = horarioAtualizacao
        self.idMoeda = idMoeda

    def cadastrarMoeda(self):
        banco = BancoMoedas()

        try:
            c = banco.conexao.cursor()

            c.execute("insert into moedas (nome, sigla, cotacao, horarioAtualizacao) values ('" + self.nome +
                      "', '" + self.sigla + "', '" + str(self.cotacao) + "', '" + self.horarioAtualizacao + "') ")
            banco.conexao.commit()
            c.close()

            return "Moeda cadastrada"
        except:
            return "Erro no cadastro da moeda"


# retorna lista com tuplas, com cada uma representando uma linha do banco de dados
def listarMoedas():
    banco = BancoMoedas()
    try:
        c = banco.conexao.cursor()

        query = """select * from moedas"""
        c.execute(query)
        dados = c.fetchall()
        return dados

    except:
        return "Erro ao listar moedas"


def atualizarCotacoes():
    try:
        valoresAntigos = {}

        for i in range(len(listaMoedas)):
            valoresAntigos[listaMoedas[i][2]] = listaMoedas[i][3]
        print("Valores antigos: ", valoresAntigos)

        listaAtualizada = []
        for tupla in listaMoedas:
            codigo = tupla[2]
            novoValor = round(CurrencyRates().get_rate(codigo, "BRL"), 5)
            atualizacao = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

            listaAtualizada.append(
                (tupla[0], tupla[1], codigo, novoValor, atualizacao))
        print("Lista atualizada: ", listaAtualizada)

        banco = BancoMoedas()

        for moeda in listaAtualizada:
            c = banco.conexao.cursor()
            c.execute("update moedas set nome = '" + moeda[1] + "', sigla = '" + moeda[2] +
                      "', cotacao = '" + str(moeda[3]) + "', horarioAtualizacao = '" + moeda[4] + "' where idMoeda = " + str(moeda[0]) + " ")
            banco.conexao.commit()
            c.close()

        # analises das moedas
        analiseMoedas = {}
        for i in range(len(listaMoedas)):
            sigla = listaMoedas[i][2]
            porcentagem = (
                (listaAtualizada[i][3] / valoresAntigos[sigla]) - 1) * 100
            variacao = listaAtualizada[i][3] - valoresAntigos[sigla]

            analiseMoedas[sigla] = {"Porcentagem": round(
                porcentagem, 2), "Variacao": round(variacao, 5)}
            print(porcentagem, variacao)
        print("Analise das moedas: ", analiseMoedas)

        listaProdutos = atualizarPrecos()

        return "Moedas e preços atualizadas com sucesso"
    except:
        return "Erro ao atualizar cotações"


def atualizarPrecos():
    banco = BancoProdutos()

    c = banco.conexao.cursor()
    c.execute("""select * from produtos""")
    dados = c.fetchall()
    # cada linha dos dados é um produto diferente

    listaProdutos = []
    for linha in dados:
        produto = Produto(linha[1], linha[2], linha[3], linha[4], linha[6])
        listaProdutos.append(produto)
    print("Lista produtos: ", listaProdutos)

    c.close()

    return listaProdutos


# TODO: fazer as moedas atualizarem apenas de 30 em 30 min

listaMoedas = listarMoedas()
print("Moedas: ", listaMoedas)

print(atualizarCotacoes())


celular = Produto("Celular Samsung S22", "799", "USD", "10", "3")
camera = Produto("Camera Nikon D5000", "699", "EUR", "8", "2")
