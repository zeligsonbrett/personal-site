# class UF:
#     def __init__(self):
#         self.parent = {}

#     def insert(self, thing):
#         self.parent[thing] = thing

#     def find(self, thing):
#         while (self.parent[thing] != thing):
#             thing = self.parent[thing]

#         return thing
    
#     def union(self, thing1, thing2):
#         par1 = self.find(thing1)
#         par2 = self.find(thing2)

#         self.parent[par2] = par1

#     def parents(self):
#         return self.parent


class UF:
    def __init__(self):
        self.parents1 = {}

    def parents(self):
        return self.parents1

    def insert(self, val):
        self.parents1[val] = val
        return

    def find(self, val):
        curr = val

        while not self.parents1[curr] == curr:
            curr = self.parents1[curr]

        return curr

    def union(self, val1, val2):
        val2_parent = self.find(val2)
        val1_parent = self.find(val1)
        self.parents1[val1_parent] = val2_parent

        return
    
    
print('hiiiiii')
struct = UF()
print(struct.parents())
struct.insert("hello")
struct.insert("bye")
struct.insert("hi")
print(struct.parents())
struct.union("hi", "bye")
struct.union("hello", "hi")

if struct.find("hi") == struct.find("hello"):
    print("Connected")

if struct.find("hi") == struct.find("bye"):
    print("Connected")
print(struct.parents())
