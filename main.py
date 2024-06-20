# Lista de pessoas
pessoas = []

def inserir_pessoa():
    nome = input("Digite o nome da pessoa que deseja inserir: ")
    pessoas.append(nome)
    print(f"{nome} foi inserido na lista.")

def listar_pessoas():
    if pessoas:
        print("Pessoas cadastradas:")
        for pessoa in pessoas:
            print(pessoa)
    else:
        print("Não há pessoas cadastradas.")

def pesquisar_pessoa():
    nome = input("Digite o nome da pessoa que deseja pesquisar: ")
    encontrou = False
    for pessoa in pessoas:
        if pessoa.lower() == nome.lower():
            print(f"{nome} foi encontrad{'' if nome[-1] == 'a' else 'o'} na lista.")
            encontrou = True
            break
    if not encontrou:
        print(f"{nome} não encontrado na lista.")

def ordenar_lista():
    pessoas.sort()
    print("Lista ordenada por ordem alfabética.")

def atualizar_nome():
    nome_antigo = input("Digite o nome que deseja atualizar: ")
    index = -1
    for i, pessoa in enumerate(pessoas):
        if pessoa.lower() == nome_antigo.lower():
            index = i
            break
    if index != -1:
        novo_nome = input("Digite o novo nome: ")
        pessoas[index] = novo_nome
        print(f"Nome atualizado de {nome_antigo} para {novo_nome}.")
    else:
        print(f"{nome_antigo} não encontrado na lista.")

def deletar_nome():
    nome = input("Digite o nome que deseja deletar: ")
    if nome in pessoas:
        pessoas.remove(nome)
        print(f"{nome} foi removido da lista.")
    else:
        print(f"{nome} não encontrado na lista.")

# Função principal do programa
def main():
    while True:
        print("\nOpções:")
        print("1 - Inserir pessoa na lista")
        print("2 - Listar pessoas cadastradas")
        print("3 - Pesquisar pelo nome de uma pessoa")
        print("4 - Ordenar a lista por ordem alfabética")
        print("5 - Atualizar nome")
        print("6 - Deletar nome da lista")
        print("7 - Sair do programa")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            inserir_pessoa()
        elif opcao == '2':
            listar_pessoas()
        elif opcao == '3':
            pesquisar_pessoa()
        elif opcao == '4':
            ordenar_lista()
        elif opcao == '5':
            atualizar_nome()
        elif opcao == '6':
            deletar_nome()
        elif opcao == '7':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, digite um número de 1 a 7.")

# Execução do programa
if __name__ == "__main__":
    main()
