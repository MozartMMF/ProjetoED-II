import streamlit as st
import graphviz
from grafo import GrafoEcommerce
from popular_ecommerce import inicializar_dados

# --- Configuração da Página ---
st.set_page_config(page_title="Knowledge Graph E-commerce", layout="wide")

st.title("🛒 E-commerce Knowledge Graph")
st.markdown("Visualização e manipulação de grafo semântico para recomendações.")

# --- 1. Persistência de Dados (Session State) ---
# Garante que o grafo não seja apagado a cada clique
if 'loja' not in st.session_state:
    st.session_state.loja = GrafoEcommerce()
    inicializar_dados(st.session_state.loja)

# Atalho
kg = st.session_state.loja

# --- 2. Menu Lateral ---
menu = st.sidebar.radio(
    "Escolha uma ação:",
    ["Visualizar Grafo", "Consultar Detalhes", "Fazer Recomendação", "Adicionar Compra"]
)

# --- 3. Funcionalidades ---
if menu == "Visualizar Grafo":
    st.header("🕸️ Visualização do Grafo")
    st.markdown("Aqui você vê todos os nós e como eles se conectam.")
    
    # Cria um objeto de grafo direcionado ('digraph')
    graph = graphviz.Digraph()
    graph.attr(rankdir='LR') # LR = Left to Right (Desenha da esquerda pra direita)

    # 1. Desenhar os Nós (Bolinhas)
    for id_no, dados in kg.nos.items():
        tipo = dados['tipo']
        
        # Lógica de Cores
        cor = "white"
        formato = "ellipse"
        
        if tipo == "Cliente":
            cor = "#add8e6"    # Azul claro
            formato = "circle"
        elif tipo == "Produto":
            cor = "#ffffe0"    # Amarelo claro
            formato = "box"
        elif tipo == "Marca":
            cor = "#d3d3d3"    # Cinza
        elif tipo == "Categoria":
            cor = "#90ee90"    # Verde claro

        # Adiciona o nó ao desenho
        # label: O texto que aparece dentro
        # style: filled (preenchido com cor)
        # fillcolor: a cor que definimos acima
        graph.node(id_no, label=f"{id_no}\n({tipo})", shape=formato, style='filled', fillcolor=cor)

    # 2. Desenhar as Arestas (Setas)
    for id_no, dados in kg.nos.items():
        for aresta in dados['arestas']:
            # Cria uma linha de 'id_no' até 'aresta['alvo']'
            # label é o nome do relacionamento (ex: COMPROU)
            graph.edge(id_no, aresta['alvo'], label=aresta['tipo'], fontsize="10")

    # 3. Exibir na tela do Streamlit
    st.graphviz_chart(graph)
    
    st.info(f"Total de Nós: {len(kg.nos)}")


elif menu == "Consultar Detalhes":
    st.header("🔍 Consultar Nó")
    lista_nos = list(kg.nos.keys())
    escolha = st.selectbox("Selecione uma entidade:", lista_nos)
    
    if escolha:
        dados = kg.buscar_detalhes(escolha)
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Dados")
            st.json(dados["dados"])
            st.metric("Tipo", dados["tipo"])
        with col2:
            st.subheader("Conexões (Sai de...)")
            for aresta in dados["arestas"]:
                st.write(f"➡️ **{aresta['tipo']}** ➡️ {aresta['alvo']}")

elif menu == "Fazer Recomendação":
    st.header("💡 Sistema de Recomendação")
    st.markdown("Algoritmo: *Filtragem Colaborativa baseada em Vizinhos*")
    
    clientes = [k for k, v in kg.nos.items() if v['tipo'] == "Cliente"]
    cliente_selecionado = st.selectbox("Escolha o Cliente:", clientes)
    
    if st.button("Gerar Recomendação"):
        sugestoes = kg.recomendar_para_cliente(cliente_selecionado)
        if sugestoes:
            st.success(f"Produtos sugeridos para {cliente_selecionado}:")
            cols = st.columns(len(sugestoes))
            for i, produto in enumerate(sugestoes):
                with cols[i]:
                    st.warning(f"⭐ {produto}")
        else:
            st.info("Nenhuma recomendação encontrada (ou cliente já tem tudo).")

elif menu == "Adicionar Compra":
    st.header("➕ Registrar Nova Compra")
    c1, c2 = st.columns(2)
    with c1:
        clientes = [k for k, v in kg.nos.items() if v['tipo'] == "Cliente"]
        cli = st.selectbox("Cliente:", clientes)
    with c2:
        produtos = [k for k, v in kg.nos.items() if v['tipo'] == "Produto"]
        prod = st.selectbox("Produto:", produtos)
        
    if st.button("Confirmar"):
        if kg.adicionar_relacionamento(cli, prod, "COMPROU"):
            st.success(f"Relação criada: {cli} -> COMPROU -> {prod}")
            st.balloons()
        else:
            st.error("Erro ao criar relação.")