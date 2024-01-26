# crie um mapeamento entre estados e siglas
states = {
    'Oregon': 'OR',
    'Florida':'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan':'MI'
}

# crie um conjunto básico de estados e algumas cidades deles 
cities = {
    'CA': 'San Frascisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# adicione mais algumas cidades
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# imprima algumas cidades
print('-' * 100)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

# imprima alguns estados
print('-' * 100)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# faça isso usando o dic state e depois o cities
print('-' * 100)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# imprima todas as siglas dos estados
print('-' * 100)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# imprima cada cidade no estado
print('-' * 100)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# agora faça ambos ao mesmo tempo
print('-' * 100)
for state, abbrec in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 100)
#com segurança. obtenha uma silga de um estado que pode não estar ali
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

#obtenha uma cidade com um valor padrão
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")