# essa aqui é como seus scripts com argv
def print_two(*args): #permite a entrada de muitos argumento, semelhantes a uma lista
    arg1, arg2 = args # descompacta os argumentos: separa e envia os conteúdos da lista em duas variáveis
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, aquele *args é desnecessário, podemos simplesmente fazer isso
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#essa recebe apenas um argumento
def print_one(arg1):
    print(f"arg1: {arg1}")

#essa não recebe argumento nenhum
def print_none():
    print("I got nothin'.")


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()