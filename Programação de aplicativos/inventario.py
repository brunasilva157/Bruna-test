# Dicionário para busca rápida por chave (nome do produto) [cite: 63, 64]
estoque = {
    'maçã': [50, 0.5],
    'banana': [45, 0.5],
    'laranja': [60, 0.7]
}

# Lista para armazenar o log de transações (mutável e ordenada) [cite: 13, 179]
historico_vendas = []

# 2. Cadastrando Novos Produtos
def cadastra_produto():
    print("\n--- CADASTRO DE PRODUTO ---")
    nome = input("Digite o nome do produto: ").strip().lower()
    
    # Validação para não sobrescrever dados existentes [cite: 183, 184]
    if nome in estoque:
        print(f"Erro: O produto '{nome}' já existe no estoque!")
    else:
        quantidade = int(input(f"Quantidade inicial de {nome}: "))
        preco = float(input(f"Preço unitário de {nome}: "))
        
        # O valor é uma lista aninhada: [quantidade, preço] [cite: 178]
        estoque[nome] = [quantidade, preco]
        print(f"Produto '{nome}' cadastrado com sucesso!")

# 3. Simulando a Venda (Lógica Principal)
def realizar_venda():
    print("\n--- REALIZAR VENDA ---")
    produto_venda = input("Nome do produto desejado: ").strip().lower()
    
    # Verifica se a chave existe no dicionário [cite: 188]
    if produto_venda in estoque:
        qtd_desejada = int(input(f"Quantidade para compra: "))
        
        # Acesso aos dados aninhados via índice [cite: 159, 189]
        qtd_disponivel = estoque[produto_venda][0]
        preco_unitario = estoque[produto_venda][1]
        
        if qtd_desejada <= qtd_disponivel:
            # Atualização do estoque (subtração) [cite: 189]
            estoque[produto_venda][0] -= qtd_desejada
            
            # Cálculo e registro da transação [cite: 190]
            valor_total = qtd_desejada * preco_unitario
            transacao = {
                "produto": produto_venda,
                "quantidade": qtd_desejada,
                "total": valor_total
            }
            historico_vendas.append(transacao) # Adiciona ao final da lista [cite: 31]
            
            print(f"Venda confirmada! Valor total: R$ {valor_total:.2f}")
        else:
            print(f"Saldo insuficiente! Temos apenas {qtd_disponivel} unidades.")
    else:
        print("Erro: Produto não encontrado no inventário.")

# 4. Exibindo o Relatório de Inventário
def exibir_relatorio():
    print("\n--- RELATÓRIO DE INVENTÁRIO ATUALIZADO ---")
    # O método .items() retorna pares de chave e valor [cite: 85, 194]
    for nome, dados in estoque.items():
        quantidade = dados[0]
        preco = dados[1]
        print(f"Produto: {nome:10} | Qtd: {quantidade:3} | Preço: R$ {preco:5.2f}")

# MENU DE EXECUÇÃO (Para testar o sistema)
while True:
    print("\n--- SISTEMA DE LOJA ---")
    print("1. Cadastrar Produto")
    print("2. Realizar Venda")
    print("3. Exibir Inventário")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        cadastra_produto()
    elif opcao == '2':
        realizar_venda()
    elif opcao == '3':
        exibir_relatorio()
    elif opcao == '4':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")