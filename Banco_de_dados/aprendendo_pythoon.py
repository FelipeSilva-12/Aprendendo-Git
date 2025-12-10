
'''

print("Olá, Mundo!")
nome = input("Escreva algo aqui")

print(f"Parabéns {nome}, você está treinando.")

if nome == "Felipe":
    print("=======================Testando===========================")
else: print("Né não")


# Testando Listas e anotando no caderno.



idade = 24
saldo = 1513
logado = True

usuario = [nome, idade, 'felipe@gmail.com', saldo, logado]

print(usuario)
print(type(usuario))



# testando outra coisa



nome = input("Crie um nome")
senha = input ("Crie uma senha")

if len(nome) and len(senha) >= 3:
    email = nome + '@gmail.com'
    dados = [nome, senha, email]
    print(f"seu login, sua senha e seu novo e-mail são: {dados}")
else: print("Coloque mais que 2 caracteres")

'''

# Conjuntos

