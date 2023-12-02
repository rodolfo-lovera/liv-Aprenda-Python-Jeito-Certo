from sys import argv # importa função para entrada via prompt

script, input_file = argv # variaveis para as entradas via prompt

def print_all(f): #função que imprime todo o arquivo
    print(f.read())

def rewind(f): #função para colocar o cursor no inicio do arquivo
    f.seek(0) #método que direciona o cursor no byte indicado

#def print_a_line(line_count, f): # função que imprime apenas uma linha do arquivo
#    print(line_count, f.readline())

current_file = open(input_file) #armazena a abertura do arquivo na variável

print("First let's print the whole file:\n") #informa que irá imprimir todo o arquivo

print_all(current_file) #imprime todo o arquivo

print("Now let's rewind, kind of like a tape.") #informa que irá rebobinar o texto

rewind(current_file) #usa função REWIND para ir para a posição inicial do arquivo

print("Let's print three lines:") #informa que irá imprimir apenas 3 linhas

current_line = 1 #atribui o valor da linha deseja na variável
#print_a_line(current_line, current_file)# usa função PRINT_A_LINE para imprimir apenas a linha desejada
print(current_line, current_file.readline())

current_line += current_line #incrementa valor da linha
#print_a_line(current_line, current_file)# usa função PRINT_A_LINE para imprimir apenas a linha desejada
print(current_line, current_file.readline())

current_line = current_line + 1 #incrementa valor da linha
#print_a_line(current_line, current_file)# usa função PRINT_A_LINE para imprimir apenas a linha desejada
print(current_line, current_file.readline())