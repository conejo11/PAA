
class Graph:

    def __init__(self, directed = False):
        self.adjList = dict()
        self.directed = directed

    def addVertice(self, vertice):
        self.adjList[vertice] = list()

    def addEdge(self, v1, v2):
        self.adjList[v1].append(v2)

        if not self.directed:
            self.adjList[v2].append(v1)

    def removeEdge(self, v1, v2):
        self.adjList[v1].remove(v2)

        if not self.directed:
            self.adjList[v2].remove(v1)

    def degree(self, vertice):
        return len(self.adjList[vertice])

    def numEdges(self):
        cont = 0
        for i in self.getVertices():
            cont = cont + self.degree(i)

        return cont

    def getVertices(self):
        return list(self.adjList.keys())

    def numVertices(self):
        return len(self.getVertices())

    def dfs(self, v, s):
        for v1 in self.adjList[v]:
            if v1 not in s:
                s.add(v1)
                self.dfs(v1, s)

    def isEuler(self):
        for i in list(self.adjList.keys()):
            if self.degree(i) % 2 == 1:
                return False
        return True

    def isConnected(self):
        ini = self.getVertices()[0]
        s = set()
        s.add(ini)
        self.dfs(ini, s)

        return len(s) == self.numVertices()

    def dfsFleury(self, ini, v, ciclo):
        if v == ini:
            if self.numEdges() == 0:
                return True

        if len(self.adjList[v]) > 0:
            for v1 in self.adjList[v]:
                self.removeEdge(v, v1)
                ciclo.append(v1)
                fechou = self.dfsFleury(ini, v1, ciclo)
                if not fechou:
                    self.addEdge(v, v1)
                    ciclo.pop()
                else:
                    return True

    def fleury(self):
        if not self.isConnected() or not self.isEuler():
            return []
        ini = list(self.adjList.keys())[0]
        ciclo = [ini]
        self.dfsFleury(ini, ini, ciclo)

        return ciclo


# Exemplo

graph = Graph()

graph.addVertice(0)
graph.addVertice(1)
graph.addVertice(2)
graph.addVertice(3)
graph.addVertice(4)
graph.addVertice(5)
graph.addVertice(6)

graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 4)
graph.addEdge(2, 3)
graph.addEdge(2, 5)
graph.addEdge(3, 4)
graph.addEdge(3, 5)
graph.addEdge(4, 5)
graph.addEdge(4, 6)
graph.addEdge(5, 6)

graph2 = Graph()

graph2.addVertice(0)
graph2.addVertice(1)
graph2.addVertice(2)
graph2.addVertice(3)
graph2.addVertice(4)
graph2.addVertice(5)
graph2.addVertice(6)
graph2.addVertice(7)

graph2.addEdge(0, 1)
graph2.addEdge(1, 2)
graph2.addEdge(3, 2)
graph2.addEdge(3, 0)

graph2.addEdge(4, 5)
graph2.addEdge(4, 7)
graph2.addEdge(5, 6)
graph2.addEdge(7, 6)


print(graph.fleury())
print(graph2.fleury())
