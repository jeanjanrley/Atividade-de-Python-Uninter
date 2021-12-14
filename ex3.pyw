# total de acertos
acertos = ["-", "-", "-", "-"]

# Função que vai para a próxima fase se o usuário quiser
def nextFase(fase):
    resposta = input(
        "Deseja continuar para a proxima fase mesmo assim? (S/N) ").upper()
    if(resposta == "S"):
        fase()
    else:
        tentarNovamente()

# Fases do jogo
def fase1():
    acertos = ["-", "-", "-", "-"]
    print("===>> BEM VINDO A PRIMEIRA FASE!!! <<===")
    print("=> Nesta fase você deve alocar o Gato e o Rato na seguinte matriz que representa os quartos." + "\n")

    print("[*,*,-,G]")
    print("[R,-,*,*]")
    gato, rato = 0, 0

    gato = int(input("Digite o número do Gato: "))
    rato = int(input("Digite o número do Rato: "))


    if (gato == rato):
        print("Erro: Você não pode alocar mais de um hóspede no mesmo quarto!")
        tentarNovamente(fase1)
    elif (gato | rato != 3 | 6):
        print("Erro: Você está tentando alocar os hóspede em quartos indispoiveis!")
        tentarNovamente(fase1)
    elif (gato == 3 and rato == 6):
        print("=> Parabéns, você passou para a próxima fase!" + "\n")
        acertos[0] = "X"
        fase2()
    else:
        print("=> Você perdeu! Tente novamente!")
        nextFase(fase2)


def fase2():
    print("===>> BEM VINDO A SEGUNDA FASE!!! <<===")
    print("=> Nesta fase você deve alocar dois Cães e um Osso na seguinte matriz que representa os quartos." + "\n")
    print("[-,*,*,*]")
    print("[*,C,-,-]")
    matriz = [0, 0, 0, 0, 0, "C", 0, 0, 0]
    cao1, cao2, osso = 0, 0, 0

    cao1 = int(input("Digite o número do primero Cão: "))
    cao2 = int(input("Digite o número do segundo Cão: "))
    osso = int(input("Digite o número do Osso: "))

    if (cao1 == cao2 or cao1 == osso or cao2 == osso):
        print("Erro: Você não pode alocar mais de um hóspede no mesmo quarto!")
        tentarNovamente(fase2)
    elif (cao1 | cao2 | osso != 1 | 7 | 8):
        print("Erro: Você está tentando alocar os hóspedes em quartos indispoiveis!")
        tentarNovamente(fase2)

    matriz[cao1] = "C"
    matriz[cao2] = "C"
    matriz[osso] = "O"

    if (matriz[matriz.index("O") - 1] == "C" or matriz[matriz.index("O") + 1] == "C"):
        print("=> Você perdeu!")
        nextFase(fase3)
        tentarNovamente(fase2)
    else:
        print("=> Parabéns, você passou para a próxima fase!" + "\n")
        acertos[1] = "X"
        fase3()


def fase3():
    print("===>> BEM VINDO A TERCEIRA FASE!!! <<===")
    print("=> Nesta fase você deve alocar um Gato um Rato e um Osso na seguinte matriz que representa os quartos." + "\n")
    print("[-,*,*,*]")
    print("[-,G,-,*]")
    matriz = [0, 0, 0, 0, 0, "G", 0, 0, 0]
    gato, rato, osso = 0, 0, 0

    gato = int(input("Digite o número do gato: "))
    rato = int(input("Digite o número do rato: "))
    osso = int(input("Digite o número do Osso: "))

    if (gato == rato or gato == osso or rato == osso):
        print("Erro: Você não pode alocar mais de um hóspede no mesmo quarto!")
        tentarNovamente(fase3)
    elif (gato | rato | osso != 1 | 5 | 7):
        print("Erro: Você está tentando alocar os hóspedes em quartos indispoiveis!")
        tentarNovamente(fase3)

    matriz[gato] = "G"
    matriz[rato] = "R"
    matriz[osso] = "O"

    if (matriz[matriz.index("G") - 1] == "R" or matriz[matriz.index("G") + 1] == "R"):
        print("=> Você perdeu!")
        tentarNovamente(fase1)
    elif (matriz[matriz.index("R") - 1] == "G" or matriz[matriz.index("R") + 1] == "G"):
        print("=> Você perdeu!")
        tentarNovamente(fase1)
    else:
        print("=> Parabéns, você passou para a próxima fase!" + "\n")
        acertos[2] = "X"
        fase4()


def fase4():
    print("===>> BEM VINDO A QUARTA FASE!!! <<===")
    print("=> Nesta fase você deve alocar dois Queijos e um Osso na seguinte matriz que representa os quartos." + "\n")
    print("[-,-,-,*]")
    print("[*,R,*,*]")
    matriz = [0, 0, 0, 0, 0, "R", 0, 0, 0]
    queijo1, queijo2, osso = 0, 0, 0

    queijo1 = int(input("Digite o número do primeiro queijo: "))
    queijo2 = int(input("Digite o número do segundo queijo: "))
    osso = int(input("Digite o número do Osso: "))

    if (queijo1 == queijo2 or queijo1 == osso or queijo2 == osso):
        print("Erro: Você não pode alocar mais de um hóspede no mesmo quarto!")
        tentarNovamente()
    elif (queijo1 | queijo2 | osso != 1 | 2 | 3):
        print("Erro: Você está tentando alocar os hóspedes em quartos indispoiveis!")
        tentarNovamente()

    matriz[queijo1] = "Q"
    matriz[queijo2] = "Q"
    matriz[osso] = "O"

    if (matriz[matriz.index("Q") - 1] == "R" or matriz[matriz.index("Q") + 1] == "R"):
        print("=> Você perdeu!")
        tentarNovamente(fase1)
    elif (matriz[matriz.index("R") - 1] == "Q" or matriz[matriz.index("R") + 1] == "Q"):
        print("=> Você perdeu!")
        tentarNovamente(fase1)
    else:
        print("=> Parabéns! Você venceu o jogo!")
        acertos[3] = "X"
        print("Total de acertos: " + str(acertos.count("X")))
        print("Acertos: ", acertos)
        resposta = input("Deseja jogar esta fase novamente? (S/N)").upper()
        if resposta == "S":
            fase4()
        tentarNovamente(fase1)

# Função para tentar novamente


def tentarNovamente(fase):
    resposta = input("Deseja tentar novamente? (S/N) ").upper()
    if(resposta == "S"):
        fase()
    else:
        print("Fim do jogo!")
        exit()


def main():
    print("HOTEL DOS ANIMAIS")
    print("=================")
    print("=> Bem-vindo ao Hotel dos Animais!\n")
    print("Regras do jogo:")
    print(" • O rato não pode ficar ao lado do gato.")
    print(" • O cão não pode ficar ao lado do osso.")
    print(" • O gato não pode ficar ao lado do cão.")
    print(" • O queijo não pode ficar ao lado do rato" + "\n")
    print("Especificando posições: ")
    print("[1,2,3,4]")
    print("[5,6,7,8]" + "\n")
    fase1()


main()
