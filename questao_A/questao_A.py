import matplotlib.pyplot as plt
import random
import time
import sys

sys.setrecursionlimit(100000)

def geraLista(tam):
    # gera uma lista de inteiros aleatorios entre 1 e tam
    random.seed()
    lista = []
    i = 0
    while i < tam:
        lista.append(random.randint(1, tam))
        i += 1
    return lista


# ------------------------------------------------------------------
# BUBBLE SORT - O(n^2)
# percorre a lista repetidamente comparando pares adjacentes e
# trocando-os quando estao fora de ordem. A cada passagem, o maior
# elemento nao ordenado "sobe" para sua posicao correta.
# ------------------------------------------------------------------
def bubbleSort(lista):
    n = len(lista)
    i = 0
    while i < n:
        j = 0
        while j < n - 1:
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            j += 1
        i += 1


# ------------------------------------------------------------------
# INSERTION SORT - O(n^2)
# constroi a parte ordenada da lista um elemento por vez. A cada
# iteracao, o elemento atual e inserido na posicao correta dentro
# da subsequencia ja ordenada, deslocando os maiores para a direita.
# ------------------------------------------------------------------
def insertionSort(lista):
    n = len(lista)
    i = 1
    while i < n:
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
        i += 1


# ------------------------------------------------------------------
# SELECTION SORT - O(n^2)
# divide a lista em parte ordenada e nao ordenada. A cada passo,
# encontra o menor elemento da parte nao ordenada e o coloca na
# primeira posicao disponivel da parte ordenada.
# ------------------------------------------------------------------
def selectionSort(lista):
    n = len(lista)
    i = 0
    while i < n - 1:
        min_idx = i
        j = i + 1
        while j < n:
            if lista[j] < lista[min_idx]:
                min_idx = j
            j += 1
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
        i += 1


# ------------------------------------------------------------------
# MERGE SORT - O(n log n)
# divide recursivamente a lista ao meio ate obter sublistas de um
# elemento, depois as mescla em ordem. A funcao merge combina duas
# sublistas ja ordenadas em uma unica lista ordenada.
# ------------------------------------------------------------------
def merge(esq, dir):
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    # adiciona os elementos restantes de cada metade
    while i < len(esq):
        resultado.append(esq[i])
        i += 1
    while j < len(dir):
        resultado.append(dir[j])
        j += 1
    return resultado


def mergeSort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esq = mergeSort(lista[:meio])
    dir = mergeSort(lista[meio:])
    return merge(esq, dir)


def mergeSortWrapper(lista):
    # aplica mergeSort e copia o resultado de volta para a lista original
    resultado = mergeSort(lista)
    i = 0
    while i < len(lista):
        lista[i] = resultado[i]
        i += 1


# ------------------------------------------------------------------
# QUICK SORT - O(n log n) medio / O(n^2) pior caso
# escolhe um elemento como pivo (aqui, o ultimo) e particiona a
# lista de forma que os menores fiquem a esquerda e os maiores a
# direita. Aplica o processo recursivamente em cada metade.
# ------------------------------------------------------------------
def particionar(lista, inicio, fim):
    pivo = lista[fim]
    i = inicio - 1  # indice do ultimo elemento menor que o pivo
    j = inicio
    while j < fim:
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
        j += 1
    # coloca o pivo na posicao correta
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1


def quickSortRec(lista, inicio, fim):
    if inicio < fim:
        p = particionar(lista, inicio, fim)
        quickSortRec(lista, inicio, p - 1)
        quickSortRec(lista, p + 1, fim)


def quickSort(lista):
    quickSortRec(lista, 0, len(lista) - 1)


# ------------------------------------------------------------------
# COUNTING SORT - O(n + k), onde k e o valor maximo da lista
# conta quantas vezes cada valor aparece e reconstroi a lista
# em ordem a partir dessas contagens. Nao faz comparacoes entre
# elementos, por isso e mais rapido para inteiros em faixa limitada.
# ------------------------------------------------------------------
def countingSort(lista):
    if not lista:
        return
    max_val = lista[0]
    i = 1
    while i < len(lista):
        if lista[i] > max_val:
            max_val = lista[i]
        i += 1

    contagem = [0] * (max_val + 1)
    i = 0
    while i < len(lista):
        contagem[lista[i]] += 1
        i += 1

    # reconstroi a lista inserindo cada valor de acordo com sua contagem
    idx = 0
    i = 0
    while i <= max_val:
        j = 0
        while j < contagem[i]:
            lista[idx] = i
            idx += 1
            j += 1
        i += 1


# ------------------------------------------------------------------
# RADIX SORT - O(n * k), onde k e o numero de digitos
# ordena os elementos digito a digito, do menos ao mais
# significativo, usando Counting Sort em cada passagem.
# estavel: preserva a ordem relativa de elementos com mesmo digito.
# ------------------------------------------------------------------
def countingSortDigito(lista, exp):
    # ordena a lista com base no digito representado por exp (1, 10, 100...)
    n = len(lista)
    saida = [0] * n
    contagem = [0] * 10  # digitos de 0 a 9

    i = 0
    while i < n:
        digito = (lista[i] // exp) % 10
        contagem[digito] += 1
        i += 1

    # acumulacao para determinar posicoes finais
    i = 1
    while i < 10:
        contagem[i] += contagem[i - 1]
        i += 1

    # percurso reverso para manter estabilidade
    i = n - 1
    while i >= 0:
        digito = (lista[i] // exp) % 10
        saida[contagem[digito] - 1] = lista[i]
        contagem[digito] -= 1
        i -= 1

    i = 0
    while i < n:
        lista[i] = saida[i]
        i += 1


def radixSort(lista):
    if not lista:
        return
    max_val = lista[0]
    i = 1
    while i < len(lista):
        if lista[i] > max_val:
            max_val = lista[i]
        i += 1

    exp = 1
    while max_val // exp > 0:
        countingSortDigito(lista, exp)
        exp *= 10


# ------------------------------------------------------------------
# BUCKET SORT - O(n + k) caso medio
# distribui os elementos em baldes de acordo com o valor,
# ordena cada balde individualmente (usando Insertion Sort) e
# concatena os baldes ao final. Eficiente quando os dados
# estao distribuidos de forma uniforme.
# ------------------------------------------------------------------
def bucketSort(lista):
    if not lista:
        return

    min_val = lista[0]
    max_val = lista[0]
    i = 1
    while i < len(lista):
        if lista[i] < min_val:
            min_val = lista[i]
        if lista[i] > max_val:
            max_val = lista[i]
        i += 1

    n = len(lista)
    intervalo = (max_val - min_val + 1) / n

    baldes = []
    i = 0
    while i < n:
        baldes.append([])
        i += 1

    # distribui cada elemento no balde correspondente
    i = 0
    while i < n:
        idx = int((lista[i] - min_val) / intervalo)
        if idx >= n:
            idx = n - 1
        baldes[idx].append(lista[i])
        i += 1

    # ordena cada balde e concatena
    for balde in baldes:
        insertionSort(balde)

    idx = 0
    for balde in baldes:
        for val in balde:
            lista[idx] = val
            idx += 1


# ------------------------------------------------------------------
# SHELL SORT - O(n log^2 n) com sequencia de gaps n/2
# extensao do Insertion Sort que compara elementos distantes por
# um gap decrescente. Isso move elementos deslocados rapidamente
# para perto de sua posicao correta antes do refinamento final.
# ------------------------------------------------------------------
def shellSort(lista):
    n = len(lista)
    gap = n // 2  # gap inicial
    while gap > 0:
        i = gap
        while i < n:
            temp = lista[i]
            j = i
            # insertion sort com passo gap
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
            i += 1
        gap //= 2  # reduz o gap pela metade a cada passagem


# ------------------------------------------------------------------
# HEAP SORT - O(n log n)
# transforma a lista em um max-heap (arvore binaria onde cada pai
# e maior que seus filhos) e extrai repetidamente o maior elemento
# (raiz) para o final da lista. Implementacao iterativa do heapify
# para evitar limite de recursao.
# ------------------------------------------------------------------
def heapify(lista, n, raiz):
    # garante a propriedade de max-heap a partir do no raiz
    while True:
        maior = raiz
        esq = 2 * raiz + 1
        dir = 2 * raiz + 2
        if esq < n and lista[esq] > lista[maior]:
            maior = esq
        if dir < n and lista[dir] > lista[maior]:
            maior = dir
        if maior == raiz:
            break  # propriedade ja satisfeita
        lista[raiz], lista[maior] = lista[maior], lista[raiz]
        raiz = maior  # desce para o filho trocado


def heapSort(lista):
    n = len(lista)
    # fase 1: constroi o max-heap de baixo para cima
    i = n // 2 - 1
    while i >= 0:
        heapify(lista, n, i)
        i -= 1
    # fase 2: extrai o maior elemento e reconstroi o heap
    i = n - 1
    while i > 0:
        lista[0], lista[i] = lista[i], lista[0]
        heapify(lista, i, 0)  # heap reduzido de tamanho i
        i -= 1


# ------------------------------------------------------------------
# MEDICAO DE TEMPO
# faz uma copia da lista para nao alterar o original e mede o
# tempo de execucao do algoritmo com perf_counter (alta precisao).
# ------------------------------------------------------------------
def medirTempo(algoritmo, lista):
    copia = list(lista)
    inicio = time.perf_counter()
    algoritmo(copia)
    return time.perf_counter() - inicio


tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]

algoritmos = [
    ("Bubble Sort",    bubbleSort),
    ("Insertion Sort", insertionSort),
    ("Selection Sort", selectionSort),
    ("Merge Sort",     mergeSortWrapper),
    ("Quick Sort",     quickSort),
    ("Counting Sort",  countingSort),
    ("Radix Sort",     radixSort),
    ("Bucket Sort",    bucketSort),
    ("Shell Sort",     shellSort),
    ("Heap Sort",      heapSort),
]

tempos = {nome: [] for nome, _ in algoritmos}

for tamanho in tamanhos:
    lista = geraLista(tamanho)
    for nome, func in algoritmos:
        t = medirTempo(func, lista)
        tempos[nome].append(t)
        print(f"{nome} - tamanho {tamanho}: {t:.4f}s")

# ------------------------------------------------------------------
# FIGURA 1 - grafico geral com todos os algoritmos
# permite comparar visualmente o crescimento do tempo de execucao
# de cada metodo conforme o tamanho do vetor aumenta.
# ------------------------------------------------------------------
cores = ['#1f77b4', '#d62728', '#2ca02c', '#7f7f7f', '#e377c2',
         '#ff7f0e', '#bcbd22', '#17becf', '#9467bd', '#8c564b']
marcadores = ['o', 's', 'D', '^', 'v', 'P', '*', 'X', 'h', 'd']

fig, ax = plt.subplots(figsize=(12, 7))
for i, (nome, _) in enumerate(algoritmos):
    ax.plot(tamanhos, tempos[nome], label=nome,
            color=cores[i], marker=marcadores[i], linewidth=1.5, markersize=5)

ax.set_title("Ordering Algorithms Timing Analysis")
ax.set_xlabel("List size (elements)")
ax.set_ylabel("Time (seconds)")
ax.legend(loc='upper left', fontsize=9, shadow=True)
ax.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------
# FIGURA 2 - graficos por grupo de desempenho semelhante
# separa os algoritmos em tres grupos para facilitar a analise:
# O(n^2), O(n log n) e lineares. Sem essa separacao, as curvas
# dos algoritmos eficientes ficam achatadas perto do zero no grafico
# geral e sao dificeis de comparar entre si.
# ------------------------------------------------------------------
grupos = [
    ("O(n^2): Bubble, Insertion, Selection",
     ["Bubble Sort", "Insertion Sort", "Selection Sort"]),
    ("O(n log n): Merge, Quick, Shell, Heap",
     ["Merge Sort", "Quick Sort", "Shell Sort", "Heap Sort"]),
    ("Lineares: Counting, Radix, Bucket",
     ["Counting Sort", "Radix Sort", "Bucket Sort"]),
]

fig2, axes = plt.subplots(1, 3, figsize=(18, 5))
fig2.suptitle("Ordering Algorithms Timing Analysis")
for ax, (titulo, nomes) in zip(axes, grupos):
    for nome in nomes:
        ax.plot(tamanhos, tempos[nome], label=nome, marker='o', linewidth=1.5, markersize=5)
    ax.set_title(titulo, fontsize=9)
    ax.set_xlabel("List size (elements)")
    ax.set_ylabel("Time (seconds)")
    ax.legend(fontsize=8, shadow=True)
    ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
