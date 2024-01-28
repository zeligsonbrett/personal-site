
# class Node:
#     def __init__(self, val, next, prev):
#         self.val = val
#         self.next = next
#         self.prev = prev

# class Queue:
#     def __init__(self):
#         self.start = None
#         self.end = None
#         self.size = 0

#     def enqueue(self, val):
#         if self.size == 0:
#             new = Node(val, None, None)
#             self.start = new
#             self.end = new

#         else:
#             new = Node(val, self.start, None)
#             self.start.prev = new
#             self.start = new       

#         self.size += 1     

#     def dequeue(self):
#         if self.size <= 0:
#             print("Empty Queue")
#             return
        
#         val = self.end.val
#         self.end = self.end.prev
        
#         if self.end:
#             self.end.next = None
#         self.size -= 1

#         if self.size == 1:
#             self.start = self.end

#         return val


class Node:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

class Queue:
    def __init__(self):
        self.start = None
        self.end = None
        self.count = 0

    def enqueue(self, val):
        if self.count == 0:
            newNode = Node(val, None, None)
            self.start = newNode
            self.end = self.start
        else:
            self.start.prev = Node(val, self.start, None)
            self.start = self.start.next

        self.count += 1
        return

    def dequeue(self):
        if self.count == 0:
            print("Nothing Left!!")
            return

        val = self.end.val

        if self.count == 1:
            self.start = None
            self.end = None
        else:
            self.end = self.end.prev
            self.end.next = None

        self.count -= 1
        return val
    


hi = Queue()
print(hi)
hi.enqueue(10)
hi.enqueue("hello")
print(hi.dequeue())
print(hi.dequeue())
print(hi.dequeue())

