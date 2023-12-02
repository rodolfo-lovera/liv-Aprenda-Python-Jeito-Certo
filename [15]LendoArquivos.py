from sys import argv # faz a importação dde uma função para entrada de dados
script, filename = argv #indica quais serão as variáveis que receberão os valores de entrada

txt = open(filename) # maneira de realizar a abertura de uma arquivo de texto

print(f"Here's your file {filename}:") # imprime o nome do arquivo
print(txt.read()) # método da função que realiza s leitura de arquivo de texto

print("Type the filename again:") # imprime o nome do arquivo
"""file_again = input("> ") #pede para usuário entrar com o nome do arquivo a ser aberto e lido

txt_again = open(file_again) #abre arquivo

print(txt_again.read()) #realiza a leitura do texto
"""