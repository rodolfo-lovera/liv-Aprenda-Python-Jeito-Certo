people = 30 # atribui valores as variáveis para usar nas operações lógicas
cars = 40
trucks = 15


if cars > people: # compara duas variáveis,
    print("We should take the cars.") # como a condição é verdadeira, esse bloco será mostrado
elif cars < people: # se a primeira condição fosse falsa, esta operação seria testada
    print("We should not take the cars.") # codigos que seriam executados caso operação anterior fosse avaliada como verdadeira
else: # casso as duas operações anteiores fosse falsa, os códigos desse bloco seriam executados
    print("We can't decide.")

if trucks > cars: # repete a mesma coisa do bloco condicional anterior
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")