from sys import argv # importação de função para entrada comando no prompt

script, input_file = argv # enviar textos digitados no prompt de abertura para variáveis

def print_all(f): # função para leitura de arquivos
    print(f.read())

def rewind(f): # função para colocar o cursor no início do arquivo aberto
    f.seek(0)

def print_a_line(line_count, f): # função para imprimir uma linha selecionada de um arquivos de texto
    print(line_count, f.readline())

current_file = open(input_file) # abertura de arquivo através de uma variável

print("First let's print the whole file:\n")

print_all(current_file) # realiza a impressão do arquivo completo

print("Now let's rewind, kind of like a tape.")

rewind(current_file) # coloca o cursos no início do arquivo

print("Let's print three lines:")

current_line = 1 
print_a_line(current_line, current_file) # imprime a 1ª linha

current_line = current_line + 1
print_a_line(current_line, current_file) # imprime a 2ª linha

current_line = current_line + 1
print_a_line(current_line, current_file) # imprime a 3ª linha