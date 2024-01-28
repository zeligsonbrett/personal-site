import sys

class Edge:
    def __init__(self, frm, to, wgt):
        self.frm = frm
        self.to = to
        self.wgt = wgt

class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, frm, to, wgt):
        newEdge = Edge(frm, to, wgt)
        
        if frm in self.graph:
            self.graph[frm].append(newEdge)
        else: 
            self.graph[frm] = [newEdge]

        if to not in self.graph:
            self.graph[to] = []

        # newEdge2 = Edge(to, frm, 1/wgt)
        # self.graph[to].append(newEdge2)

    def bfs(self, curr):
        track = [curr]
        paths = {}
        dist = {}
        visited = {}
        for i in range(len(self.graph)):
            visited[i] = False
            dist[i] = 0

        dist[curr] = 0
        paths[curr] = curr
        visited[curr] = True
        while len(track) > 0:
            curr_node = track.pop(0)

            for edge in self.graph[curr_node]:
                if not visited[edge.to]:
                    visited[edge.to] = True
                    track.append(edge.to)
                    paths[edge.to] = edge.frm
                    dist[edge.to] = dist[edge.frm] + 1

        return (dist, paths)

    def relax(self, edge):
        if(self.distTo[edge.to] > self.distTo[edge.frm] * edge.wgt):
            self.distTo[edge.to] = self.distTo[edge.frm] * edge.wgt
            self.pathTo[edge.to] = edge.frm

        
    def shortest_path(self, start):
        self.distTo = {}
        self.pathTo = {}

        for vertex in self.graph:
            self.distTo[vertex] = sys.maxsize

        self.distTo[start] = 1
        self.pathTo[start] = start

        for i in range(1, len(self.graph)):
            for vertex in self.graph:
                for edge in self.graph[vertex]:
                    self.relax(edge)

        return (self.distTo, self.pathTo)



my_graph = Graph()
my_graph.addEdge(0, 1, 5)
my_graph.addEdge(0, 2, 10)
my_graph.addEdge(0, 3, 15)
my_graph.addEdge(1, 3, 10)
my_graph.addEdge(2, 3, 20)
my_graph.addEdge(3, 2, 30)
my_graph.addEdge(1, 4, 100)
print(my_graph.bfs(2))
print()
print(my_graph.shortest_path(1))



