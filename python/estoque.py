import os

def LimparTela():
    os.system('cls')
# Função para limpar a tela do terminal

# Declarações das variáveis que serão usadas
produtos = []
categorias = []
movimentacao = []
contador_de_produtos = 0
contador_de_categorias = 0
movimentacoes = 0

# Função para cadastrar um produto
def CadastrarDeProduto():
    global contador_de_produtos
    contador_de_produtos = contador_de_produtos + 1

    nome = input("Nome do Produto: ")
    id = int(input("ID da Categoria: "))
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))

    ProdutoNovo = {
        "id": contador_de_produtos,
        "nome": nome,
        "categoria_id": id,
        "quantidade": quantidade,
        "preco": preco
    }
    
    LimparTela()

    global produtos

    produtos.append(ProdutoNovo)
    print("O produto foi cadastrado")


def CasdastroDeCategoria():
    global contador_de_categorias
    contador_de_categorias = contador_de_categorias + 1

    NomeDaCategoria = input("Nome da Categoria: ")

    CategoriaNova = {
        "id": contador_de_categorias,
        "nome": NomeDaCategoria
    }

    LimparTela()

    global categorias

    categorias.append(CategoriaNova)
    print(f"A categoria {NomeDaCategoria} foi adicionada, O ID da categoria é {contador_de_categorias}")

def EncontrarProdutoPorID(id):
    global produtos
    
    for produto in produtos:
        if produto["id"] == id:
            print(produto)
            return # Sai da função
        
    # Se nem um produto for encontrado
    print("Produto não encontrado")

def EncontrarProdutoPorNome(nome):
    global produtos

    for produto in produtos:
        if produto["nome"].lower() == nome.lower()