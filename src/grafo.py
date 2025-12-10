class GrafoEcommerce:
    def __init__(self):
        self.nos = {}

    def adicionar_no(self, id_no, tipo, atributos=None):
        if id_no not in self.nos:
            self.nos[id_no] = {
                "tipo": tipo,
                "dados": atributos if atributos else{},
                "arestas": []
            }
            return True
        return False
    
    def adicionar_relacionamento(self, origem, destino, relacao):
        if origem in self.nos and destino in self.nos:
            self.nos[origem]["arestas"].append({
                "alvo": destino,
                "tipo": relacao
            })
            return True
        return False

    def remover_no(self, id_no):
        if id_no in self.nos:
            del self.nos[id_no]

            for outro_no in self.nos:
                self.nos[outro_no]["arestas"] = [
                    a for a in self.nos[outro_no]["arestas"] if a ["alvo"] != id_no
                ]
            return True
        return False
    
    def consultar_vizinhos(self, id_no, tipo_relacao=None):
        if id_no in self.nos:
            arestas = self.nos[id_no]["arestas"]
            if tipo_relacao:
                return [a["alvo"] for a in arestas if a["tipo"] == tipo_relacao]
            return []
        
    def buscar_detalhes(self, id_no):
        return self.nos.get(id_no)
    
    def recomendar_para_cliente(self, id_cliente):
        if id_cliente not in self.nos: return []
        
        produtos_do_cliente = self.consultar_vizinhos(id_cliente, "COMPROU")
        recomendacoes = set()

        # Varre todo o grafo
        for outro_user, dados in self.nos.items():
            # [CORREÇÃO] Tudo o que acontece aqui dentro precisa estar indentado
            if dados["tipo"] == "Cliente" and outro_user != id_cliente:
                
                # 1. Cria a variável
                compras_outro = self.consultar_vizinhos(outro_user, "COMPROU")
                
                # 2. Usa a variável (Este IF deve estar ALINHADO com a linha de cima)
                if any(p in produtos_do_cliente for p in compras_outro):
                    for prod in compras_outro:
                        if prod not in produtos_do_cliente:
                            recomendacoes.add(prod)
        
        return list(recomendacoes)
        
    
    def exibir_grafo(self):
        print("\n Estado do Grafo E-commerce")
        for id_no, dados in self.nos.items():
            print(f"[{dados['tipo']}] {id_no}")
            for a in dados["arestas"]:
                print(f"   |--({a['tipo']})--> {a['alvo']}")