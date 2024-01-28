# class Edge:
#     def __init__(self, frm, to, weight):
#         self.frm = frm
#         self.to = to
#         self.weight = weight

# class UnitConversion:
#     def __init__(self):
#         self.graph = {}

#     def addEdge(self, frm, to, weight):
#         newEdge = Edge(frm, to, weight)
#         if frm in self.graph:
#             self.graph[frm].append(newEdge)
#         else:
#             self.graph[frm] = [newEdge]

#         if to not in self.graph:
#             self.graph[to] = []

#     def dfs(self, curr, dest, multiplier):
#         self.visited[curr] = True

#         if curr == dest:
#             self.multiplyBy = multiplier
#             return

#         for edge in self.graph[curr]:
#             if not self.visited[edge.to]:
#                 self.dfs(edge.to, dest, multiplier * edge.weight)


#     def convert(self, amount, start, dest):
#         self.visited = {}

#         for key in self.graph:
#             self.visited[key] = False

#         self.dfs(start, dest, 1)
        
#         return amount * self.multiplyBy
    
# converter = UnitConversion()
# converter.addEdge("m", "cm", 0.1)
# converter.addEdge("cm", "mm", 0.1)
# print(converter.convert(2000, "m", "mm"))


import sys


class Edge:
    def __init__(self, frm, to, weight):
        self.frm = frm
        self.to = to
        self.weight = weight

class Graph:
    def __init__(self):
        self.graph = {}

    def insert(self, frm, to, weight):
        if not frm in self.graph:
            self.graph[frm] = []

        self.graph[frm].append(Edge(frm, to, weight))

        if not to in self.graph:
            self.graph[to] = []

        self.graph[to].append(Edge(to, frm, weight))

    def dfs(self, curr, to):
        self.visited[curr] = True

        if curr.to == to:
            return True
        
        for edge in self.graph[curr]:
            if not self.visited[edge.to]:
                self.dfs(edge.frm, to)

    def bfs(self, frm, to):
        queue = [frm]
        self.pathTo[frm] = frm
        self.distTo[frm] = 0

        while len(queue) > 0:
            curr = queue.pop(0)

            for edge in self.graph[curr]:
                if not self.visited[edge.to]:
                    queue.append(edge.to)
                    self.distTo[edge.to] = self.distTo[edge.frm] + 1
                    self.pathTo[edge.to] = edge.frm

            self.visited[curr] = True

    def relax(self, edge):
        if(self.distTo[edge.to] > self.distTo[edge.frm] + edge.weight):
            self.distTo[edge.to] = self.distTo[edge.frm] + edge.weight
            self.pathTo[edge.to] = edge.frm
        
        return


    def bellman(self, start):
        self.distTo = {}
        self.pathTo = {}

        for node in self.graph:
            self.distTo[node] = sys.maxsize

        self.distTo[start] = 0
        self.pathTo[start] = start

        for _ in range(1, len(self.graph)):
            for node in self.graph:
                for edge in self.graph[node]:
                    self.relax(edge)
    

