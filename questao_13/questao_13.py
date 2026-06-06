# CLASSE ALUNO
# atributos privados com prefixo __ (convencao Python para privacidade).
# acesso e modificacao feitos exclusivamente pelos metodos get/set.
# ------------------------------------------------------------------
class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.__nome  = nome
        self.__nota1 = nota1
        self.__nota2 = nota2

    def getNome(self):   return self.__nome
    def getNota1(self):  return self.__nota1
    def getNota2(self):  return self.__nota2

    def setNome(self, nome):    self.__nome  = nome
    def setNota1(self, nota1):  self.__nota1 = nota1
    def setNota2(self, nota2):  self.__nota2 = nota2

    def media(self):
        # media ponderada: nota1 com peso 2 e nota2 com peso 3
        return (self.__nota1 * 2 + self.__nota2 * 3) / 5

    def __str__(self):
        return (f"  {self.__nome:<20} | "
                f"Nota1: {self.__nota1:.1f} | "
                f"Nota2: {self.__nota2:.1f} | "
                f"Media: {self.media():.2f}")


# ------------------------------------------------------------------
# BUBBLE SORT - O(n^2)
# percorre a lista comparando pares adjacentes e trocando quando
# necessario. Recebe uma funcao 'chave' para definir o criterio
# de comparacao, tornando o metodo reutilizavel para qualquer campo.
# ------------------------------------------------------------------
def bubbleSort(lista, chave):
    n = len(lista)
    i = 0
    while i < n:
        j = 0
        while j < n - 1:
            if chave(lista[j]) > chave(lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            j += 1
        i += 1


# ------------------------------------------------------------------
# SELECTION SORT - O(n^2)
# a cada iteracao, encontra o menor elemento a partir da posicao i
# e o coloca na posicao correta. Realiza no maximo n-1 trocas,
# independentemente da ordem inicial dos elementos.
# ------------------------------------------------------------------
def selectionSort(lista, chave):
    n = len(lista)
    i = 0
    while i < n - 1:
        min_idx = i
        j = i + 1
        while j < n:
            if chave(lista[j]) < chave(lista[min_idx]):
                min_idx = j
            j += 1
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
        i += 1


# ------------------------------------------------------------------
# INSERTION SORT - O(n^2)
# insere cada elemento na posicao correta dentro da subsequencia
# ja ordenada, deslocando os maiores para a direita. Eficiente
# para listas pequenas ou quase ordenadas.
# ------------------------------------------------------------------
def insertionSort(lista, chave):
    n = len(lista)
    i = 1
    while i < n:
        atual = lista[i]
        j = i - 1
        while j >= 0 and chave(lista[j]) > chave(atual):
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = atual
        i += 1


def exibir(titulo, lista):
    print(f"\n{titulo}")
    print("-" * 62)
    for aluno in lista:
        print(aluno)
    print("-" * 62)


# cadastro dos 8 alunos
alunos = [
    Aluno("Carlos Silva",    7.5, 6.0),
    Aluno("Ana Souza",       9.0, 8.5),
    Aluno("Bruno Lima",      4.0, 3.5),
    Aluno("Diana Oliveira",  6.0, 7.0),
    Aluno("Eduardo Santos",  5.5, 4.0),
    Aluno("Fernanda Costa",  8.0, 9.0),
    Aluno("Gabriel Pereira", 3.0, 2.5),
    Aluno("Helena Martins",  7.0, 7.5),
]

# parte I: ordem crescente por media ponderada usando Bubble Sort
lista1 = list(alunos)
bubbleSort(lista1, lambda a: a.media())
exibir("I. Ordem crescente por media ponderada (Bubble Sort)", lista1)

# parte II: ordem crescente por nota1 usando Selection Sort
lista2 = list(alunos)
selectionSort(lista2, lambda a: a.getNota1())
exibir("II. Ordem crescente por nota1 (Selection Sort)", lista2)

# parte III: filtra os reprovados (media < 7) e os ordena
# alfabeticamente usando Insertion Sort
reprovados = [a for a in alunos if a.media() < 7.0]
insertionSort(reprovados, lambda a: a.getNome().lower())
exibir("III. Reprovados (media < 7) em ordem alfabetica (Insertion Sort)", reprovados)
