from sys import argv # importa um módulo para entrada de dados na execução do arquivo
#leia a seção 0 que você deve ver para saber como executar isso
script, first, second, third = argv # irá transformar os dados digitados em uma lista.

print("The script is called:", script)
print("Your first variable is:", first)
print("Your seconf variable is: ", second)
print("Your third variable is:", third)

"""
para executar, precisa estar no CMD digitar o comando para executar
arquivos Python junto com o nome do arquivo mais 
3 valores de entrada
python [13]Parametro.py valor1 valor 2 valor 3

o resultado será que argv será uma lista com esses valores:
['[13]Parametro.py','valor1','valor 2','valor 3']
"""
