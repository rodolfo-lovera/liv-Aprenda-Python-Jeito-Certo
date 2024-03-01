import sys  # importação de funcionalidades
script, encoding, error = sys.argv # para entrada de prompts


def main(language_file, encoding, errors): #declaração da função principal do códig
    line = language_file.readline() # faz a leitura do arquivo informado

    if line: # comdicional que executa o código caso a linha esteja preenchida
        print_line(line, encoding, errors) # chama a função que realiza a impressão da linha mencionada
        return main(language_file, encoding, errors) # executa a repetição da função principal enquanto a linha tiver algum texto


def print_line(line, encoding, errors): # função que faz a impressão da linha do arquivo
    next_lang = line.strip() # retirar o \n da linha lida anteriormente
    raw_bytes = next_lang.encode(encoding, errors=errors) #codificação da string na variável nest_lang em bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors) #decodifica os bytes na variável raw_bytes em strings

    print(raw_bytes, "<===>", cooked_string) #imprime os bytes e a string


languages = open("languages.txt", encoding="utf-8") # abertura do arquivo

main(languages, encoding, error) #chamada da função principal