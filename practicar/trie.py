class TrieNode:
    def __init__(self, char, isWord):
        self.char = char
        self.isWord = isWord
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode("", False)

    def addWord(self, word):
        curr = self.root

        for i, char in enumerate(word):
            if i == len(word) - 1:
                curr.children[char] = TrieNode(char, True)

            else:
                if char not in curr.children:
                    curr.children[char] = TrieNode(char, False)

            curr = curr.children[char]
            
    def traverse(self, curr):
        for key in curr.children:
            print(key)
            self.traverse(curr.children[key])
    
    def inorderTraverse(self):
        track = [self.root]

        while(len(track) > 0):
            curr = track.pop(0)

            for key in curr.children:
                track.append(curr.children[key])
                print(key)
            print('')

    def find(self, val):
        curr = self.root

        for i, char in enumerate(val):
            if char not in curr.children:
                return False
            curr = curr.children[char]
            if i == len(val) - 1:
                if curr.isWord:
                    return True
                return False


mytrie = Trie()
mytrie.addWord("hello")
mytrie.addWord("hear")
mytrie.addWord("toot")
mytrie.addWord("poop")
mytrie.addWord("pipi")
mytrie.addWord("heal")
print(mytrie)
# mytrie.inorderTraverse()
print(mytrie.find("hi"))
print(mytrie.find("hear"))
print(mytrie.find("poop"))
print(mytrie.find("poo"))
