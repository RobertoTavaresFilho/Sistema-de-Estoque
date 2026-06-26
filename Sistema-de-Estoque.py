import json

class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def valor_total(self):
        return self.quantidade * self.preco
    
    def __str__(self):
        return (f"Nome : {self.nome} | quantidade : {self.quantidade} | valor : {self.preco} | valor total :{self.valor_total():.2f}  ")
    
    def repor_estoque(self, quantidade_adicional):
        self.quantidade += quantidade_adicional 
    
        


def cadastrar_produto():
    nome = input("Nome do produto: ").lower()
    if nome == "":
        print("Nome não pode ser vazio. Cadastro cancelado.")
        return
    quantidade = pedir_numero_inteiro("Quantidade: ")
    preco = pedir_numero_decimal("Preço: ")
                    
    novo_produto = Produto(nome, quantidade, preco)
    estoque.append(novo_produto)
    print(f"{nome} cadastrado com sucesso!")
    

def remover_produto():
    nome = input("Digite o nome do produto para remover :").lower()
    encontrado = False
    
    for produto in estoque:
        if produto.nome == nome :
            estoque.remove(produto)
            encontrado = True
            break
    if not encontrado:
        print("Produto não encontrado.")

    
def salvar_estoque():
    dados = []
    for produto in estoque:
        dados.append({
            "nome": produto.nome,
            "quantidade": produto.quantidade,
            "preco": produto.preco
        })
    
    with open("estoque.json", "w") as arquivo:
        json.dump(dados, arquivo)
    print("Estoque salvo com sucesso!")
    
    
def carregar_estoque():
    try:
        with open("estoque.json", "r") as arquivo:
            dados = json.load(arquivo)
        
        for item in dados:
            produto = Produto(item["nome"], item["quantidade"], item["preco"])
            estoque.append(produto)
        
        print("Estoque carregado com sucesso!")
    except FileNotFoundError:
        print("Nenhum estoque salvo ainda. Começando do zero.")    
        
def pedir_numero_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

def pedir_numero_decimal(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Digite um número flutuante.")

estoque = [] 

def listar_produtos():
    if not estoque:
        print("Estoque vazio.")
        return
    for produto in estoque:
        print(produto)    
        
carregar_estoque()              
while True:   
    print("\n1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Sair")
    print("4 - Remover produto")
    print("5 - Salvar estoque!")
    opcao = input("Escolha uma opção: ")
        
    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        break
    elif opcao == "4":
        remover_produto()
    elif opcao == "5":
        salvar_estoque()
    else:
        print("Opção inválida.")

