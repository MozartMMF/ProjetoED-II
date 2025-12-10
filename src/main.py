from grafo import GrafoEcommerce
from popular_ecommerce import inicializar_dados

def main():
    loja = GrafoEcommerce()
    inicializar_dados(loja)

    while True:
        print("\n=== E-COMMERCE KNOWLEDGE GRAPH ===")
        print("1. Ver catálogo completo (Dump do Grafo)")
        print("2. Consultar Cliente/Produto")
        print("3. Fazer Recomendação para Cliente")
        print("4. Adicionar Compra (Relacionamento)")
        print("5. Remover Nó")
        print("0. Sair")

        escolha = input("Opção: ")

        if escolha == "1":
            loja.exibir_grafo()

        elif escolha == "2":
            nome = input("Digite o nome: ")
            dados = loja.buscar_detalhes(nome)
            if dados:
                print(f"\nTipo: {dados['tipo']}")
                print(f"Propriedades: {dados['dados']}")
                print("Conexões:")
                for a in dados["arestas"]:
                    print(f"  --[{a['tipo']}]--> {a['alvo']}")
            else:
                print("Não encontrado.")

        elif escolha == "3":
            cliente = input("Nome do cliente para recomendação: ")
            sugestoes = loja.recomendar_para_cliente(cliente)
            print(f"\n--- Recomendação Inteligente para {cliente} ---")
            if sugestoes:
                print("Baseado em clientes com gosto parecido, sugerimos:")
                for s in sugestoes:
                    print(f" -> {s}")
            else:
                print("Sem recomendações no momento (ou histórico insuficiente).")
        
        elif escolha == "4":
            cli = input("Cliente: ")
            prod = input("Produto: ")
            if loja.adicionar_relacionamento(cli, prod, "COMPROU"):
                print("Compra registrada!")
            else:
                print("Erro: Cliente ou Produto não existem.")

        elif escolha == "5":
            nome = input("Nome para deletar: ")
            loja.remover_no(nome)

        elif escolha == "0":
            break

if __name__ == "__main__":
    main()