def break_words(stuff):
    """Esta função irá dividir palavras para nós."""
    words = stuff.split(' ') # transforma uma string em uma lista
    return words

def sort_words(words):
    """Ordenar as palavras."""
    return sorted(words) #função que ordena as palavras em ordem alfabética

def print_first_word(words):
    """Imprime a primeira palavra depois dew tirá-la do conjunto."""
    word = words.pop(0) # retira o item da lista e retorna ele para a variável
    return(word)

def print_last_word(words):
    """Imprime a última palavra depois de tirá-la do conjunto."""
    word = words.pop(-1) # retira o item da lista e retorna ele para a variável
    print(word)

def sort_sentence(sentence):
    """Recebe uma frase completa e retorna as palavras ordenadas."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Imprime a primeira e a última palavra de uma frase."""   
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Ordena as palavras e então imprime a primeira e a última."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)