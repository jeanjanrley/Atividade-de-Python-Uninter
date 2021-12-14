import random

class Pessoa:
    def __init__(self, nome, email, telefone, curso):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.curso = curso
        self.id = random.randrange(0, 20, 1)


pessoas = []


def main():
    print("## MENU DE OPÇÕES ##")
    print("1 - Cadastrar Pessoa")
    print("2 - Visualizar inscrições")
    print("3 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        telefone = input("Digite o telefone: ")
        curso = input("Digite o curso: ")

        pessoa = Pessoa(nome, email, telefone, curso)
        pessoas.append(pessoa)
        print("Pessoa cadastrada com sucesso!")
        main()
    elif opcao == 2:
        if len(pessoas) < 1:
            print("Não há pessoas cadastradas" + "\n")
        else:
            for pessoa in pessoas:
                print("====================")
                print("Nome: ", pessoa.nome)
                print("Email: ", pessoa.email)
                print("Telefone: ", pessoa.telefone)
                print("Curso: ", pessoa.curso)
                print("Id: ", pessoa.id)
                print("====================" + "\n")
        main()
    elif opcao == 3:
        print("Saindo...")
        exit()
    else:
        print("Opção inválida!")
        main()


main()
