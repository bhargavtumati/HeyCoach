"""### Trie Data Structure Problem Statement

Implement a Trie (Prefix Tree) with the following functions:

#### 1. `insert(word)`

Insert a word into the Trie.

#### 2. `search(word)`

Return `True` if the word exists in the Trie as a complete word; otherwise return `False`.

#### 3. `startsWith(prefix)`

Return `True` if there is at least one word in the Trie that starts with the given prefix; otherwise return `False`.

### Example

**Input:**

```
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");
trie.search("app");
trie.startsWith("app");
trie.insert("app");
trie.search("app");
```

**Output:**

```
true
false
true
true
```

### Explanation:

* Insert `"apple"` into the Trie.
* `"apple"` exists, so `search("apple")` returns `true`.
* `"app"` is only a prefix of `"apple"`, not a complete word, so `search("app")` returns `false`.
* `"app"` is a prefix of an inserted word, so `startsWith("app")` returns `true`.
* After inserting `"app"`, it becomes a complete word, so `search("app")` returns `true`.
"""


class Trie:

    def __init__(self):
        self._dict = {}
        

    def insert(self, word: str) -> None:
        if word[0] not in self._dict: 
            self._dict[word[0]] = {}
        lastChar = self._dict[word[0]]
        for c in word[1:]:
            if c not in lastChar:
                lastChar[c] = {}
            lastChar = lastChar[c]

        lastChar['|'] = True



    def search(self, word: str) -> bool:
        if word[0] not in self._dict:
            return False
        lastChar = self._dict[word[0]]
        for c in word[1:]:
            if c not in lastChar:
                return False
            lastChar = lastChar[c]
        return '|' in lastChar
            
        

    def startsWith(self, prefix: str) -> bool:
        if prefix[0] not in self._dict:
            return False
        lastChar = self._dict[prefix[0]]
        for c in prefix[1:]:
            if c not in lastChar:
                return False
            lastChar = lastChar[c]
        
        return lastChar
        


if __name__=="__main__":
   obj = Trie()
   obj.insert("cool")
   obj.insert("cold")
   obj.insert("pot")
   print(obj.search("cool"))
   print(obj.startsWith("co"))