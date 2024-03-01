from sys import argv #chama a função para entrada de dados no prompt

script, filename = argv #armazena nome do arquivo e texto do prompt nestas variávies

print(f"We're going to erase {filename}.")        # chama a atenção ao usuário e da
print("If you don't want that hit CTRL + C(^C).") # a opção de canceler o processo
print("If you do want that, hit Return.")         # de escrita no arquivo
input("?")                                        # espera a resposta do usuário

print("Opening the file...") # informa que o arquivo esta sendo aberto
target = open(filename,'w') # parametro w: informa para realizar a abertura do arquivo no modo de gravação

print("Truncating the file. Goodbye!") # texto para usuario
target.truncate() # edita o arquivo e tira tudo o que tem nele

print("Now I'm going to ask you for three lines.") #pede para usuário inserir tres linhas de texto

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1) 
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close() 