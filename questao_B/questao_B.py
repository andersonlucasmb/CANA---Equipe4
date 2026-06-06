import matplotlib.pyplot as plt
import random
import time

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
# COUNTING SORT - O(n + k)
# utilizado para ordenar a lista antes das buscas binarias, pois
# estas exigem que o vetor esteja ordenado. Counting Sort foi
# escolhido por ser um algoritmo de ordenacao linear, sem comparacoes.
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
# BUSCA LINEAR - O(n)
# percorre a lista elemento por elemento ate encontrar a chave.
# nao exige ordenacao previa. No pior caso, percorre a lista inteira.
# ------------------------------------------------------------------
def buscaLinear(lista, chave):
    i = 0
    while i < len(lista):
        if lista[i] == chave:
            return i  # retorna o indice onde a chave foi encontrada
        i += 1
    return -1  # chave nao encontrada


# ------------------------------------------------------------------
# BUSCA LINEAR COM SENTINELA - O(n)
# variacao da busca linear que insere a chave ao final da lista
# (sentinela) antes de comecar a busca. Isso elimina a verificacao
# de limite do laco (i < len), reduzindo o numero de comparacoes
# por iteracao de 2 para 1, o que a torna ligeiramente mais rapida.
# ------------------------------------------------------------------
def buscaLinearSentinela(lista, chave):
    lista.append(chave)  # insere o sentinela
    i = 0
    while lista[i] != chave:
        i += 1
    lista.pop()  # remove o sentinela
    if i < len(lista):
        return i  # encontrou antes do sentinela
    return -1    # so encontrou o sentinela: chave nao estava na lista


# ------------------------------------------------------------------
# BUSCA BINARIA - O(log n)
# exige lista ordenada. A cada iteracao, compara a chave com o
# elemento do meio e descarta metade da lista. Usa 2 comparacoes
# por iteracao (verifica igualdade e direcao). Muito mais eficiente
# que a busca linear para listas grandes.
# ------------------------------------------------------------------
def buscaBinaria(lista, chave):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == chave:
            return meio           # chave encontrada
        elif lista[meio] < chave:
            inicio = meio + 1     # busca na metade direita
        else:
            fim = meio - 1        # busca na metade esquerda
    return -1


# ------------------------------------------------------------------
# BUSCA BINARIA RAPIDA (metodo de Knuth) - O(log n)
# otimizacao da busca binaria que usa apenas 1 comparacao por
# iteracao (somente o operador <), adiando a verificacao de
# igualdade para o final do laco. Reduz o numero total de
# comparacoes, sendo vantajosa especialmente em grandes volumes.
# ------------------------------------------------------------------
def buscaBinariaRapida(lista, chave):
    inicio = 0
    fim = len(lista)  # intervalo semi-aberto [inicio, fim)
    while inicio < fim:
        meio = (inicio + fim) // 2
        if lista[meio] < chave:
            inicio = meio + 1
        else:
            fim = meio
    # verifica igualdade apenas uma vez ao final
    if inicio < len(lista) and lista[inicio] == chave:
        return inicio
    return -1


def medirTempo(funcao, lista, chave):
    # executa a busca em uma copia da lista e retorna o tempo em segundos
    copia = list(lista)
    inicio = time.perf_counter()
    funcao(copia, chave)
    return time.perf_counter() - inicio


tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]

tempos_linear         = []
tempos_sentinela      = []
tempos_binaria        = []
tempos_binaria_rapida = []

for tamanho in tamanhos:
    lista = geraLista(tamanho)
    chave = random.randint(1, tamanho)

    # buscas lineares nao precisam de ordenacao previa
    tempos_linear.append(medirTempo(buscaLinear, lista, chave))
    tempos_sentinela.append(medirTempo(buscaLinearSentinela, lista, chave))

    # ordena com Counting Sort antes das buscas binarias
    lista_ord = list(lista)
    countingSort(lista_ord)
    tempos_binaria.append(medirTempo(buscaBinaria, lista_ord, chave))
    tempos_binaria_rapida.append(medirTempo(buscaBinariaRapida, lista_ord, chave))

    print(f"tamanho {tamanho} - chave {chave}")

# ------------------------------------------------------------------
# FIGURA 3 - ilustrativo: busca linear vs busca binaria
# mostra a diferenca de crescimento entre O(n) e O(log n).
# a busca linear cresce proporcionalmente ao tamanho do vetor,
# enquanto a binaria cresce de forma logaritmica e quase nao varia.
# ------------------------------------------------------------------
fig3, ax3 = plt.subplots(figsize=(8, 5))
ax3.plot(tamanhos, tempos_linear,  label="Busca Linear",  marker='o', linewidth=1.5)
ax3.plot(tamanhos, tempos_binaria, label="Busca Binaria", marker='s', linewidth=1.5)
ax3.set_title("Busca Linear vs Binaria")
ax3.set_xlabel("Numero de Elementos (N)")
ax3.set_ylabel("Comparacoes")
ax3.legend(shadow=True)
ax3.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------
# FIGURA 4 - comparativo entre os 4 metodos de busca
# as buscas lineares ficam claramente mais lentas conforme n cresce.
# as buscas binarias permanecem proximas de zero pois log2(24000) ~ 15,
# ou seja, sao necessarias no maximo 15 comparacoes independente do
# tamanho do vetor.
# ------------------------------------------------------------------
fig4, ax4 = plt.subplots(figsize=(10, 6))
ax4.plot(tamanhos, tempos_linear,         label="busca_linear",          marker='o', linewidth=1.5)
ax4.plot(tamanhos, tempos_sentinela,      label="busca_linear_sentinela", marker='s', linewidth=1.5)
ax4.plot(tamanhos, tempos_binaria,        label="busca_binaria",          marker='D', linewidth=1.5)
ax4.plot(tamanhos, tempos_binaria_rapida, label="busca_binaria_rapida",   marker='^', linewidth=1.5)
ax4.set_title("Comparativo entre o tempo de execucao das buscas")
ax4.set_xlabel("Tamanho do vetor")
ax4.set_ylabel("Tempo de execucao (s)")
ax4.legend(fontsize=9, shadow=True)
ax4.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
