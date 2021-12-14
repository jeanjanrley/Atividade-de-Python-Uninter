#Definindo função de continuar ou interromper o programa.
def continuar():	
	option = input("Deseja continuar? (S/N): ").upper()	
	if (option == "S"):
		main()
	elif (option == "N"):
		print("Obrigado por utilizar o programa!")
		exit()
	else:
		print("Opção inválida! você precisa escolher entre (S/N)")
		continuar()

def main():
	global continar
	nome = input("Digite seu nome: ").upper()

	# Altera as vogais do nome
	nomeAlterado = nome.replace("A", "@")
	nomeAlterado = nomeAlterado.replace("E", "&")
	nomeAlterado = nomeAlterado.replace("I", "!")
	nomeAlterado = nomeAlterado.replace("O", "#")
	nomeAlterado = nomeAlterado.replace("U", "*")
	print(nomeAlterado)

	continuar()

main()

