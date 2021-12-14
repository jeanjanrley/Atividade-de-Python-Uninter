#Definindo função de continuar ou interromper o programa.
def continuar():	
	option = input("Deseja continuar? (S/N): ").upper()	
	if (option == "S"):
		mainProgram()
	elif (option == "N"):
		print("Obrigado por utilizar o programa!")
		exit()
	else:
		print("Opção inválida! você precisa escolher entre (S/N)")
		continuar()

def mainProgram():
	global continuar
	nome = input("Digite o nome da criança: ")

	#Verifica se o usuário inserio um valor numerico.
	try: 
		idade = int(input("Digite a idade do aluno(a): "))
	except ValueError:
		print("Você precisa fornecer um valor numerico para a idade do aluno!")
		continuar()

	#condicionais que categorizam a idade do aluno.
	if (idade > 0  and idade <= 5):
		print("O aluno(a): ", nome, "tem ", idade, "anos e está no ensino infantil.")
		continuar()
	elif (idade >= 6  and idade <= 10):
		print("O aluno(a): ", nome, "tem ", idade, "anos e está no ensino fundamental I.")
		continuar()
	elif (idade >= 11  and idade <= 14):
		print("O aluno(a): ", nome, "tem ", idade, "anos e está no ensino fundamental II.")
		continuar()
	elif (idade >= 15):
		print("O aluno(a): ", nome, "tem ", idade, "anos e está no ensino médio.")
		continuar()

#invocação da função principal.
mainProgram()