def chamar_funçao():
    quantidade = 3 
    lista_empresas = []

    for i in range(quantidade):
        nome = input(f"Digite a {i+1}º empresa: ")
        lista_empresas.append(nome)

    print("\nLista de empresas:")
    for nome in lista_empresas:
        print(nome)

chamar_funçao()