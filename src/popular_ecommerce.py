
def inicializar_dados(grafo):
    print("Carregando catálogo e histórico de compras...") 

    # Categorias (3)
    grafo.adicionar_no("Eletrônicos", "Categoria")
    grafo.adicionar_no("Livros", "Categoria")
    grafo.adicionar_no("Esporte", "Categoria")

    # Marcas (3)
    grafo.adicionar_no("Apple", "Marca")
    grafo.adicionar_no("Samsung", "Marca")
    grafo.adicionar_no("Nike", "Marca")

    # Produtos (8)
    grafo.adicionar_no("iPhone 13", "Produto", {"preco": 5000})
    grafo.adicionar_no("MacBook Air", "Produto", {"preco": 8000})
    grafo.adicionar_no("Galaxy S21", "Produto", {"preco": 4000})
    grafo.adicionar_no("Galaxy Buds", "Produto", {"preco": 900})
    grafo.adicionar_no("Clean Code", "Produto", {"autor": "Uncle Bob"})
    grafo.adicionar_no("O Hobbit", "Produto", {"autor": "Tolkien"})
    grafo.adicionar_no("Tênis Air Jordan", "Produto", {"tamanho": 40})
    grafo.adicionar_no("Camisa DryFit", "Produto", {"tamanho": "M"})

    # Clientes (7)
    grafo.adicionar_no("João", "Cliente", {"vip": True})
    grafo.adicionar_no("Maria", "Cliente")
    grafo.adicionar_no("Carlos", "Cliente")
    grafo.adicionar_no("Ana", "Cliente")
    grafo.adicionar_no("Pedro", "Cliente")
    grafo.adicionar_no("Lucas", "Cliente")
    grafo.adicionar_no("Julia", "Cliente")


    # --- 2. CRIAR RELACIONAMENTOS ---

    # Hierarquia de Produtos
    grafo.adicionar_relacionamento("iPhone 13", "Eletrônicos", "PERTENCE_A")
    grafo.adicionar_relacionamento("iPhone 13", "Apple", "FABRICADO_POR")
    grafo.adicionar_relacionamento("MacBook Air", "Apple", "FABRICADO_POR")
    grafo.adicionar_relacionamento("Galaxy S21", "Samsung", "FABRICADO_POR")
    grafo.adicionar_relacionamento("Tênis Air Jordan", "Nike", "FABRICADO_POR")
    grafo.adicionar_relacionamento("Clean Code", "Livros", "PERTENCE_A")

    # Histórico de Compras (Cenário para recomendação)
    
    # Perfil Apple Lovers
    grafo.adicionar_relacionamento("João", "iPhone 13", "COMPROU")
    grafo.adicionar_relacionamento("João", "MacBook Air", "COMPROU")
    
    # Maria comprou iPhone, mas ainda não tem o Mac (O sistema deve recomendar o Mac para ela)
    grafo.adicionar_relacionamento("Maria", "iPhone 13", "COMPROU") 

    # Perfil Leitores
    grafo.adicionar_relacionamento("Carlos", "Clean Code", "COMPROU")
    grafo.adicionar_relacionamento("Carlos", "O Hobbit", "COMPROU")
    
    # Ana só leu O Hobbit (Sistema deve recomendar Clean Code se usar lógica simples, ou nada se for estrito)
    grafo.adicionar_relacionamento("Ana", "O Hobbit", "COMPROU")

    # Perfil Esportista
    grafo.adicionar_relacionamento("Pedro", "Tênis Air Jordan", "COMPROU")
    grafo.adicionar_relacionamento("Pedro", "Camisa DryFit", "COMPROU")
    
    # Lucas comprou só a camisa
    grafo.adicionar_relacionamento("Lucas", "Camisa DryFit", "COMPROU")

    print("Dados carregados com sucesso!")