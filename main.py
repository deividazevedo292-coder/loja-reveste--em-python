from clientes import cadastrar_cliente, listar_clientes
from produtos import listar_produtos, cadastrar_produto

while True:
 print("\n =======RESVESTE=======")
 print("1 - Cadastrar cliente")
 print("2 - Listar clientes")
 print("3 - Listar produtos")
 print("4 - Cadastrar produto")
 print("0 - sair")

 opcao = input("Escolha uma opção: ")
 
 if opcao == "1":
    
    cadastrar_cliente()

 elif opcao == "2":
    listar_clientes()

    
 elif opcao == "3":
    listar_produtos()
 elif opcao == "4":
    cadastrar_produto()
   

 elif opcao == "0":
    print("saindo do sistema.....")
    break
 
 else:
    print("Opção inválida!") 


