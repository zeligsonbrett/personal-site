import sys

class Edge:
    def __init__(self, frm, to):
        self.frm = frm
        self.to = to

class Digraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, frm, to):
        if frm in self.graph:
            self.graph[frm].append(Edge(frm, to))

        else:
            self.graph[frm] = [Edge(frm, to)]

    def dfs(self, curr, to):
        if curr == to:
            return True
        
        if not curr in self.graph or len(self.graph[curr]) == 0:
            return False
        
        self.visited[curr] = True

        for edge in self.graph[curr]:
            if not self.visited[edge.to]:
                self.dfs(edge.to, to)

    def bfs(self, frm):
        pathTo = {}
        distTo = {}
        visited = {}
        queue = [frm]

        for key in self.graph:
            distTo[key] = sys.maxsize
            visited[key] = False
        
        pathTo[frm] = frm
        distTo[frm] = 0

        while len(queue) > 0:
            curr = queue.pop(0)
            self.visited[curr] = True

            for edge in self.graph[curr]:
                if not visited[edge.to]:
                    queue.append(edge.to)
                    pathTo[edge.to] = curr
                    distTo[edge.to] = distTo[edge.frm] + 1

    def bellman(self):
        
                    

test = Digraph()
test.add_edge(0, 1)
test.add_edge(0, 2)
test.add_edge(2, 1)
test.add_edge(1, 2)
test.dfs(0, 2)