while True:
    print("Menu:\n(1) Soma,\n(2) Subtração,\n(3) Multiplicação,\n(4) Divisão, \n(5) Sair.")
    opcao = float(input("\nDigite a opção desejada:"))
    
    if opcao == 1:
        num1 = float(input("\nDigite o primeiro número:"))
        num2 = float(input("\nDigite o segundo número:"))
        resultado = num1 + num2
        print(f"Resultado: ", resultado, "\n----------------------")

    elif opcao == 2:
        num1 = float(input("\nDigite o primeiro número:"))
        num2 = float(input("\nDigite o segundo número:"))
        resultado = num1 - num2
        print(f"Resultado: ", resultado, "\n----------------------")

    elif opcao == 3:

        num1 = float(input("\nDigite o primeiro número:"))
        num2 = float(input("\nDigite o segundo número:"))
        resultado = num1 * num2
        print(f"Resultado: ", resultado, "\n----------------------")
        
    elif opcao == 4:
        num1 = float(input("\nDigite o primeiro número:"))
        num2 = float(input("\nDigite o segundo número:"))
        resultado = num1 / num2
        print(f"Resultado: ", resultado, "\n----------------------")

    elif opcao > 5:
        print("--Função Invalida.--")
    elif opcao < 1:
        print("--Função Invalida.--")

    elif opcao == 5:
        print("Saindo do Sistema...")
        break