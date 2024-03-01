from sys import argv # importa biblioteca para entrada de dados
from os.path import exists # não sei que biblioteca importa

script, from_file, to_file = argv # variáveis que recebem as duas entradas pelo prompt

print(f"Copying from {from_file} to {to_file}") # imprime mensagem avisando que haverá a cópia dos arquivos

# poderíamos fazer esses dois com uma linha, como? resp.: in_file = open(from_file); indata = in_file.read()
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")# informa o tamanho do arquivo original

print(f"Does the output file exist? {exists(to_file)}") # verifica a existência do arquivo destino
print("Ready, hit RETURN to continue, CTRL+C to abort.") # pergunta se deseja continuar com o processo
input("???")

out_file = open(to_file, 'w') # abre o arquivo destino para escrever nele
out_file.write(indata) # faz a escrita no arquivo destino

print("Alright, all done.") # informa que o processo foi concluído

out_file.close()# fecha o arquivo destino
in_file.close()# fecha o arquivo de origem