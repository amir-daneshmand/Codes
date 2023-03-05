class Trie():
    def __init__(self):
        self.root = {"*":"*"}

    def add_word(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr["*"] = "*"

    def is_word(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr:
                return False
            curr = curr[letter]
        return "*" in curr



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

print(trie.root)

