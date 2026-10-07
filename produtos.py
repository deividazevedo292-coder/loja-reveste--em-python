produtos={

"calça_flear_reveste":180,
"casaco_reveste2":250,
"moletom_reveste":350,
"bermuda_reveste":120,
"shorts__reveste":159,
"camiseta_reveste":99,

}

def listar_produtos():
 
 print("\n----- PRODUTOS DISPONÍVEIS -----")
 for produto, preco in produtos.items():
        print(f"{produto}: R${preco:.2f}")

def cadastrar_produto():
  print("\n=========CADASTRO DE PRODUTOS======")


 
  nome = input("nome do produto:")
  preco = float(input("preço do produto: R$").replace(",", "."))

  produtos [nome] = preco 

  print("\nProduto cadastrado com sucesso!")


