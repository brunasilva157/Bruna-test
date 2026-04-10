while True:
    print("Menu:\n(1) Potenciação,\n(2) Dobro,\n(3) N° Primo,\n(4) Fatorial,\n(5) Par ou Ímpar,\n(6) Sair.")
    opcao = float(input("\nDigite a opção desejada:"))
    
    if opcao == 1:
        base = float(input("\nDigite o a base:"))
        expoente = float(input("\nDigite o expoente:"))
        resultado = base ** expoente
        print(f"Resultado: ", resultado, "\n-"*30)

    elif opcao == 2:
        num1 = float(input("\nDigite o primeiro número:"))
        resultado = num1 * 2
        print(f"Resultado: ", resultado, "\n-"*30)

    elif opcao == 3:
        num = int(input("\nDigite um número inteiro para verificar se é primo: "))
        
        if num <= 1:
            eh_primo = False
        else:
            eh_primo = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    eh_primo = False
                    break
        
        if eh_primo:
            print(f"Resultado: O número {num} é primo.")
        else:
            print(f"Resultado: O número {num} não é primo.")
        print("-" * 30)
        
    elif opcao == 4:
        num = int(input("\nDigite um número inteiro para calcular o Fatorial: "))
        if num < 0:
            print("Não existe fatorial de número negativo.")
        else:
            resultado = 1
            contador = num
            while contador > 1:
                resultado *= contador
                contador -= 1
            print(f"Resultado: O fatorial de {num} é {resultado}")
        print("-" * 30)
    
    elif opcao == 5:
        num = int(input("\nDigite um número inteiro: "))
        if num % 2 == 0:
            print(f"Resultado: O número {num} é PAR.")
        else:
            print(f"Resultado: O número {num} é ÍMPAR.")
        print("-" * 30)

    elif opcao == 6:
        print("Saindo do Sistema...")
        break

    else:
        print("--Função Invalida.--")