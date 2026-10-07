clientes = []

def listar_clientes():
    print("\n----- CLIENTES CADASTRADOS -----")

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in clientes:
        print(f"Nome: {cliente['nome']}")
        print(f"Telefone: {cliente['telefone']}")
        print(f"E-mail: {cliente['email']}")
        print("-----------------------------")


def cadastrar_cliente():
    print("\n----- CADASTRO DE CLIENTE -----")

    nome = input("Nome do cliente: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    cliente = {
        "nome": nome,
        "telefone": telefone,
        "email": email
     }

    clientes.append(cliente)
    print("\nCliente cadastrado com sucesso!")