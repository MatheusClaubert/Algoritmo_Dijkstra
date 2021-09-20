import math


class HeapMin:

    def __init__(self):
        self.nos = 0
        self.heap = []

    def adiciona_no(self, u, indice): #u- peso
        self.heap.append([u, indice]) #adicionamos o peso e o indice no heap nessa lista
        self.nos += 1
        f = self.nos
        while True:
            if f == 1:
                break
            p = f // 2
            if self.heap[p - 1][0] <= self.heap[f - 1][0]: #passando o peso com o indice para verificar
                break
            else:
                self.heap[p - 1], self.heap[f - 1] = self.heap[f - 1], self.heap[p - 1]
                f = p

    def mostra_heap(self):
        print('A estrutura heap é a seguinte:')
        nivel = int(math.log(self.nos, 2))
        a = 0
        for i in range(nivel):
            for j in range(2 ** i):
                print(f'{self.heap[a]}', end='  ')
                a += 1
            print('')
        for i in range(self.nos - a):
            print(f'{self.heap[a]}', end='  ')
            a += 1
        print('')

    def remove_no(self):
        x = self.heap[0]
        self.heap[0] = self.heap[self.nos - 1]
        self.heap.pop()
        self.nos -= 1
        p = 1
        while True:
            f = 2 * p
            if f > self.nos:
                break
            if f + 1 <= self.nos:                         #elemento 0 do f elemento 0 do f-1 o elemento 1 do f é o indice utilizado no dijkstra abaixo
                if self.heap[f][0] < self.heap[f - 1][0]: #novamente esses 0 é pra se oritentar nos indices no caso infomar qual posição foi removido
                    f += 1
            if self.heap[p - 1][0] <= self.heap[f - 1][0]:
                break
            else:
                self.heap[p - 1], self.heap[f - 1] = self.heap[f - 1], self.heap[p - 1]
                p = f
        return x

    def tamanho(self):
        return self.nos

    def menor_elemento(self):
        if self.nos != 0:
            return self.heap[0]
        return 'A árvore está vazia'

    def filho_esquerda(self, u):
        if self.nos >= 2 * u:
            return self.heap[2 * u - 1]
        return 'Esse nó não tem filho'

    def filho_direita(self, u):
        if self.nos >= 2 * u + 1:
            return self.heap[2 * u]
        return 'Esse nó não tem filho da direita'

    def pai(self, u):
        return self.heap[u // 2]


class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v, peso):
        self.grafo[u - 1][v - 1] = peso
        self.grafo[v - 1][u - 1] = peso

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.grafo[i])

    def dijkstra(self, origem):
        custo_vem = [[-1, 0] for i in range(self.vertices)] # o custo sera 0 ou positivo o -1 expressa o custo infinito onde todo mundo -1 com custo 0 inicialmente
        custo_vem[origem - 1] = [0, origem] #saindo da origem e vindo da propria origem
        h = HeapMin()
        h.adiciona_no(0, origem) #primeiro elemento adicionado no heap
        while h.tamanho() > 0:  #rodar todos os valores no heap e tirar esses valores se o heap for 0 eu encerro o while
            dist, v = h.remove_no() # retorna o menor valor da distancia e seu indice
            for i in range(self.vertices):
                if self.grafo[v - 1][i] != 0:   #self.grafos é a matriz de distâncias
                    if custo_vem[i][0] == -1 or custo_vem[i][0] > dist + self.grafo[v - 1][i]:
                        custo_vem[i] = [dist + self.grafo[v - 1][i], v]
                        h.adiciona_no(dist + self.grafo[v - 1][i], i + 1)
        return custo_vem


g = Grafo(7)

g.adiciona_aresta(1, 2, 5)
g.adiciona_aresta(1, 3, 6)
g.adiciona_aresta(1, 4, 10)
g.adiciona_aresta(2, 5, 13)
g.adiciona_aresta(3, 4, 3)
g.adiciona_aresta(3, 5, 11)
g.adiciona_aresta(3, 6, 6)
g.adiciona_aresta(4, 5, 6)
g.adiciona_aresta(4, 6, 4)
g.adiciona_aresta(5, 7, 3)
g.adiciona_aresta(6, 7, 8)

print("")

g.mostra_matriz()

resultado_dijkstra = g.dijkstra(1)

print("\nResultado dos vertices para Dijkstra: ")
print(resultado_dijkstra)
