# definição da função, que irá imprimir textos na tela
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")  
    print("Get a blanket.\n")

# 1ª forma de usar argumentos com uma função: usando numeros
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# 2ª forma de usar argumentos com uma função: usando variáveis
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 3ª forma de usar argumentos com uma função: usando expressões aritméticas
print("We can even do math inside too: ")
cheese_and_crackers(10 +20, 5 + 6)

# 4ª forma de usar argumentos com uma função: usando expressões aritméticas com variáveis
print("And we can combine the two, variable and math: ")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)