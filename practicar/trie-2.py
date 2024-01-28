class Trienode:
    def __init__ (self, char, isWord):
        self.char = char
        self.children = {}
        self.isWord = isWord


class Trie:
    def __init__(self):
        self.root = Trienode(self, "", False)

    def insert(self, word):
        curr = self.root

        for i, char in enumerate(word):
            if i == len(word) - 1:
                curr.children[char] = Trienode(char, True)
            else: 
                if char not in curr.children:
                    curr.children[char] = Trienode(char, False)

            if char in curr.children:
                    curr = curr.children[char]
                    
    def isWord(self, word):
        curr = self.root

        for i, char in enumerate(word):
            if char in curr.children:
                curr = curr.children[char]

                if i == len(word) - 1:
                    return curr.isWord
                
            else: 
                return False
            

