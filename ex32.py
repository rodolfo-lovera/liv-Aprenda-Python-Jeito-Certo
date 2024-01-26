the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# esse primeiro tipo de loop percorre uma lista
for number in the_count:
    print(f"This is count {number}.", end = ' ')

#mesma coisa que o código acima
print("\n")
for fruit in fruits:
    print(f"A fruit of type: {fruit}.", end = ' ')

# também podemos percorrer listas mistas
# perceba que temos que usar um {} uma vez que não sabemos o que há nela
print("\n")
for i in change:
    print(f"I got {i}.", end = ' ')

# também podemos construir listas, primeiro comece com uma vazia
elements = []

#então use a função range para fazer a contagem de 0 a 5
print("\n")
for i in range(0, 6):
    print(f"Adding {i} to the list.", end = ' ')
    #append é uma função que as listas entendem
    elements.append(i)

#agora podemos imprimi-la também
print("\n")
for i in elements:
    print(f"Element was: {i}.", end = ' ')