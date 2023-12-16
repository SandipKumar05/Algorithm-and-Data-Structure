class TrieNode:
    def __init__(self):
        self.child={}
        self.end=False

class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        node=self.root
        for c in word:
            if c in node.child:
                node=node.child[c]
            else:
                node.child[c]=TrieNode()
                node=node.child[c]
        node.end=True
    def search(self,word):
        node=self.root
        for c in word:
            if c in node.child:
                node=node.child[c]
            else:
                return False
        return node.end

obj=Trie()
obj.insert('geeksforgeek')
obj.insert('geeks')
obj.insert('geek')
obj.insert('geezer')

node=obj.root
ans=""
while True:
    print(len(node.child.keys()))
    if len(node.child.keys())==1:
        print(node.child.items())
        for key, value in node.child.items():
            node=node.child[key]
            ans=ans+key
    else:
        break
print(ans)
