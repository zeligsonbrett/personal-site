import sys

class Edge:
    def __init__(self, to, frm, wgt):
        self.to = to
        self.frm = frm
        self.wgt = wgt

class Digraph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, to, frm, wgt):
        if frm in self.graph:
            self.graph[frm].append(Edge(to, frm, wgt))
        else:
            self.graph[frm] = [Edge(to, frm, wgt)]

        if to not in self.graph:
            self.graph[to] = []

    def search_dfs(self, curr, goal, multiplier):
        if curr == goal:
            self.multiplier = multiplier
            return

        self.visited[curr] = True
        for edge in self.graph[curr]:
            if not self.visited[edge.to]:
                self.search_dfs(edge.to, goal, multiplier * edge.wgt)

    
    def run_dfs(self, start, goal):
        self.visited = {}

        for key in self.graph:
            self.visited[key] = False
        self.search_dfs(start, goal, 1)

    def run_bfs(self, start, goal):
        self.visited = {}

        for key in self.graph:
            self.visited[key] = False
        self.search_bfs(start, goal, 1)

    def search_bfs(self, curr):
        queue = []
        pathTo = {}
        distTo = {}
        queue.append(curr)
        pathTo[curr] = curr
        distTo[curr] = 0
        self.visited[curr] = True

        while len(queue) > 0:
            curr = queue.pop(0)

            for edge in self.graph[curr]:
                if not self.visited[edge.to]:
                    self.visited[edge.to] = True
                    queue.append(edge.to)
                    pathTo[edge.to] = edge.frm
                    distTo[edge.to] = distTo[edge.frm] + 1

    def relax(self, edge):
        if self.distTo[edge.to] > self.distTo[edge.frm] + edge.wgt:
            self.distTo[edge.to] = self.distTo[edge.frm] + edge.wgt
            self.pathTo[edge.to] = edge.frm

    def bellman(self, start):
        self.distTo = {}
        self.pathTo = {}
        self.distTo[start] = 0
        self.pathTo[start] = start

        for key in self.graph:
            self.distTo[key] = sys.maxsize

        for _ in range(1, len(self.graph)):
            for node in self.graph:
                for edge in self.graph[node]:
                    self.relax(edge)

        return self.distTo