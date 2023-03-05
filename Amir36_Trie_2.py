class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode("*")

    def add_word(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode(letter)
            curr = curr.children[letter]
        curr.end_of_word = True

    def is_word(self,word):
        if word == "":
            return True
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.end_of_word


trie = Trie()
words = ["shop", "shopper", "wait", "waiter", "Amir"]

for word in words:
    trie.add_word(word)

print(trie.is_word("shop")) #True
print(trie.is_word("shopp")) #False
print(trie.is_word("shopper")) #True
print(trie.is_word("wwait")) #False
print(trie.is_word("wait")) #True
print(trie.is_word("waits")) #False
print(trie.is_word("waiter")) #True
print(trie.is_word("Amir")) #True
