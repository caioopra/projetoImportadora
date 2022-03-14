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
            self.disponivel = "True"
        else:
            self.disponivel = "False"

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

    def comprar(self):
        banco = BancoProdutos()
        try:
            c = banco.conexao.cursor()

            disponibilidade = self.getDisponibilidade()
            # print(disponibilidade)
            self.qtdDisponivel = disponibilidade[0][1]
            self.disponivel = disponibilidade[0][2]

            if int(self.qtdDisponivel) - 1 == 0:
                self.disponivel = "False"
            self.qtdDisponivel = int(self.qtdDisponivel) - 1

            if self.disponivel == "True":
                query = """update produtos set qtdDisponivel = ?, disponivel = ? where produto = ?"""
                c.execute(query, (self.qtdDisponivel,
                                  self.disponivel, self.produto, ))

                banco.conexao.commit()
                c.close()
            
                return f"{self.produto} comprado com sucesso!"
            else:
                return f"{self.produto} indisponível no momento"
        except:
            return f"Erro ao comprar {self.produto}"

    def adicionar(self):
        banco = BancoProdutos()
        try:
            atualizarCotacoes()

            disponibilidade = self.getDisponibilidade()
            # print(disponibilidade)
            self.qtdDisponivel = disponibilidade[0][1]
            self.disponivel = disponibilidade[0][2]


            if self.disponivel == "False":
                self.disponivel = "True"
            self.qtdDisponivel = int(self.qtdDisponivel) + 1

            c = banco.conexao.cursor()

            query = """update produtos set qtdDisponivel = ?, disponivel = ? where produto = ?"""
            c.execute(query, (str(self.qtdDisponivel),
                        self.disponivel, self.produto, ))
            banco.conexao.commit()
            c.close()

            return "Quantidade atualizada com sucesso"
        except:
            return "Erro ao atualizar a quantidade"

    def remover(self):
        banco = BancoProdutos()
        try:
            atualizarCotacoes()

            disponibilidade = self.getDisponibilidade()
            # print(disponibilidade)
            self.qtdDisponivel = disponibilidade[0][1]
            self.disponivel = disponibilidade[0][2]


            if self.disponivel == "False":
                return
            else:
                self.qtdDisponivel = int(self.qtdDisponivel) - 1
                if self.qtdDisponivel == 0:
                    self.disponivel = "False"

            c = banco.conexao.cursor()

            query = """update produtos set qtdDisponivel = ?, disponivel = ? where produto = ?"""
            c.execute(query, (str(self.qtdDisponivel),
                        self.disponivel, self.produto, ))
            banco.conexao.commit()
            c.close()

            return "Quantidade atualizada com sucesso"
        except:
            return "Erro ao atualizar a quantidade"

    # função que retorna a quantidade disponível no banco de dados e bool da disponibilidade
    def getDisponibilidade(self):
        try:
            banco = BancoProdutos()

            c = banco.conexao.cursor()
            query = """select produto, qtdDisponivel, disponivel from produtos where produto = ?"""
            c.execute(query, (self.produto,))
            disponibilidade = c.fetchall()

            c.close()

            return disponibilidade
        except:
            return "Erro ao coletar disponibilidade"

    def comprarComDesconto(self, desconto):
        banco = BancoProdutos()
        try:
            c = banco.conexao.cursor()

            disponibilidade = self.getDisponibilidade()
            self.qtdDisponivel = disponibilidade[0][1]
            self.disponivel = disponibilidade[0][2]

            if int(self.qtdDisponivel) - 1 == 0:
                self.disponivel = "False"
            self.qtdDisponivel = int(self.qtdDisponivel) - 1

            if self.disponivel == "True":
                query = """update produtos set qtdDisponivel = ?, disponivel = ? where produto = ?"""
                c.execute(query, (self.qtdDisponivel,
                                  self.disponivel, self.produto, ))

                banco.conexao.commit()
                c.close()
            
                return f"{self.produto} comprado com sucesso!"
            else:
                return f"{self.produto} indisponível no momento"
        except:
            return f"Erro ao comprar {self.produto}"


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

        listaAtualizada = []
        for tupla in listaMoedas:
            codigo = tupla[2]
            novoValor = round(CurrencyRates().get_rate(codigo, "BRL"), 5)
            atualizacao = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

            listaAtualizada.append(
                (tupla[0], tupla[1], codigo, novoValor, atualizacao))

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
            # print(porcentagem, variacao)
        # print("Analise das moedas: ", analiseMoedas)

        listaProdutos = atualizarPrecos()

        return ("Moedas e preços atualizadas com sucesso", listaProdutos)
    except:
        return "Erro ao atualizar cotações"


def atualizarPrecos():
    banco = BancoProdutos()

    c = banco.conexao.cursor()
    c.execute("""select * from produtos""")
    # cada linha dos dados é um produto diferente
    dados = c.fetchall()

    listaProdutos = []
    for linha in dados:
        produto = Produto(linha[1], linha[2], linha[3], linha[4], linha[6])
        listaProdutos.append(produto)
    # print("Lista produtos: ", listaProdutos)

    c.close()

    return listaProdutos


listaMoedas = listarMoedas()

