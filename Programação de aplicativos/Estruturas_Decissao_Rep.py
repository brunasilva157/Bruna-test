#Estruturas de Decissão e Repetição!
saldo_inicial = 1000.00

while True:
    print("Menu:\n(1) Ver Saldo,\n(2) Depositar,\n(3) Sacar,\n(4) Sair.")
    opcao = float(input("\nDigite a opção desejada:"))
    
    if opcao == 1:
        print(f"\nSeu saldo atual é: R$ {saldo_inicial:.2f}")

    elif opcao == 2:
        valor_deposito = float(input("Digite o valor de deposito: "))
        saldo_inicial += valor_deposito
        print(f"Deposito realizado com sucesso! Novo saldo: R$ {saldo_inicial:.2f}")

    elif opcao == 3:

        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque <= 0:
            print("[ERRO] Valor inválido para saque.")
        elif valor_saque > saldo_inicial:
            print("[ERRO] Saldo insuficiente.")
        else:
            saldo_inicial -= valor_saque
            print(f"Saque realizado com sucesso! Novo saldo: R$ {saldo_inicial:.2f}")
    
    elif opcao == 4:
        print("Saindo do Sistema...")
        break