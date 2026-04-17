anotação = input("Digite u,a anotação: \n")
with open ("anotação.txt", "a") as arquivo:
    arquivo.write(anotação + "\n")
    print("Anotação gravada com sucesso!")

with open("anotaçao.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(f"Anotação Recuperada: {conteudo}")