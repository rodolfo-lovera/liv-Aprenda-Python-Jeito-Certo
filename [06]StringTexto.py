#atribuição de inteiro em variável
type_of_people = 10
#atribuição de string com variável embutida
x = f"There are {type_of_people} type of people."
#atribuição de valor textual a uma variável
binary = "binary"
#atribuição de valor textual a uma variável
do_not = "don't"
#atribuição de string com variável embutida
y = f"Those who know {binary} and those who {do_not}."

print(x) #imprime o valor da variável
print(y) #imprime o valor da variável

print(f"I' said: {x}") #imprime um texto com uma variável embutida
print(f"I also said: '{y}'") #imprime um texto com uma variável embutida

hilarious = False #criação de variável com valor booleano
joke_evaluetion = "Isn't that joke so funny?! {}" ##criação de variável com texto e espaço para embutir uma variável sem defini-lá

print(joke_evaluetion.format(hilarious)) #uma forma de imprimir a variável textual com uma variável embituda, que eu posso escolher

w = "This is left side of..." #criação de variável com valor textual
e = "a string with a right side." #criação de variável com valor textual

print(w + e) #concatena os valores textuais armazenado nas variáveis