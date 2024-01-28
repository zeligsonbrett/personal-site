import sys

class Edge:
    def __init__(self, frm, to, wgt):
        self.frm = frm
        self.to = to
        self.wgt = wgt

class Digraph:
    def __init__(self):
        self.graph = {}

    def insert(self, frm, to, wgt):
        new = Edge(frm, to, wgt)

        if frm not in self.graph:
            self.graph[frm] = []
        self.graph[frm].append(new)

        if to not in self.graph:
            self.graph[to] = []

    def dfs(self, curr):
        if len(self.graph[curr]) == 0:
            return
        
        self.visited[curr] = True

        for neighb in self.graph[curr]:
            if not self.visited[neighb.to]:
                self.dfs(neighb.to)

    def call_dfs(self, start):
        self.visited = [False for i in range(len(self.graph))]
        self.dfs(start)

    def bfs(self, start):
        self.visited = [False for i in range(len(self.graph))]
        
        queue = [start]
        distTo = {}
        pathTo = {}
        distTo[start] = 0
        pathTo[start] = start

        while len(queue) > 0:
            curr = queue.pop(0)
            self.visited[curr] = True

            for neighb in self.graph[curr]:
                if not self.visited[neighb.to]:
                    queue.append(neighb.to)
                    distTo[neighb.to] = distTo[curr] + 1
                    pathTo[neighb.to] = curr

        path = [curr]
        while not pathTo[curr] == curr:
            path.append(pathTo[curr])
            curr = pathTo[curr]

    def relax(self, edge):
        if self.distTo[edge.to] > self.distTo[edge.frm] + edge.wgt:
            self.distTo[edge.to] = self.distTo[edge.frm] + edge.wgt
            self.pathTo[edge.to] = edge.frm

    def bellman(self, start):
        self.distTo = {}
        self.pathTo = {}

        for key in self.graph:
            self.distTo[key] = sys.maxsize

        self.pathTo[start] = start
        self.distTo[start] = 0

        for _ in range(len(self.graph) - 1):
            for key in self.graph:
                for edge in self.graph[key]:
                    self.relax(edge)
