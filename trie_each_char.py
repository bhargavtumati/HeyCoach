"""### Problem Statement: Longest Word in Dictionary

Given an array of strings `words`, find the **longest word** that can be built one character at a time by other words in the same array.

A word is valid if:

* Every prefix of the word must exist in the dictionary.
* If multiple valid words have the same length, return the **lexicographically smallest** word.

Return the longest valid word. If no such word exists, return an empty string `""`.

---

### Example 1

**Input:**

```text
words = ["w","wo","wor","worl","world"]
```

**Output:**

```text
"world"
```

**Explanation:**

The word can be built as:

```
w
wo
wor
worl
world
```

All prefixes exist in the dictionary.

---

### Example 2

**Input:**

```text
words = ["a","banana","app","appl","ap","apply","apple"]
```

**Output:**

```text
"apple"
```

**Explanation:**

`apple` can be built:

```
a
ap
app
appl
apple
```

`banana` is not valid because `"b"` does not exist.

---

### Example 3

**Input:**

```text
words = ["abc","ab","a"]
```

**Output:**

```text
"abc"
```

---

### Example 4

**Input:**

```text
words = ["yo","y","yod","yodn"]
```

**Output:**

```text
"yodn"
```

**Explanation:**

Prefixes:

```
y
yo
yod
yodn
```

all exist.

---

### Constraints

```text
1 <= words.length <= 10^5

1 <= words[i].length <= 30

words[i] contains only lowercase English letters.
```

---

### Function Signature

Python:

```python
def longestWord(self, words: List[str]) -> str:
```

Return the longest word that satisfies the prefix condition.

---

## Approach

This problem can be solved using a **Trie (Prefix Tree)**.

### Steps:

1. Insert all words into a Trie.
2. While traversing the Trie:

   * A node can be used only if all previous characters form a valid word.
   * Track the longest valid word.
3. If two words have the same length, choose the lexicographically smaller one.

---

### Example Trie

For:

```text
words = ["a","ap","app","apple"]
```

Trie:

```
        root
          |
          a *
          |
          p *
          |
          p *
          |
          l
          |
          e *
```

`*` indicates a complete word.

Since every prefix exists:

```
a → ap → app → apple
```

Answer:

```
apple
```

---

### Complexity Analysis

Let:

* `N` = number of words
* `L` = maximum word length

### Time Complexity:

```
O(N * L)
```

Each word is inserted and checked character by character.

### Space Complexity:

```
O(N * L)
```

For storing Trie nodes.
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.val = None
        self.children = {}
        self.isWord = False

    def addword(self, word, appe, already, word2):
        ro = self
        if not word:
            ro.isWord = True
            return

        if ro.val is not None and not ro.isWord and len(word) > 1:
            appe = True

        if len(word) == 1 and not appe:
            already.append(word2)

        if word[0] not in ro.children:
            ro.children[word[0]] = {}

        ro.val = word[0]
        ro = ro.children[word[0]]
        self.addword(word[1:], appe, already, word2)

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        already = []
        appe = False

        words.sort(key=len)

        for word in words:
            root.addword(word, appe, already, word)
        already.sort(key=len)

        # Filter out words that are not valid (e.g., "ew" when "e" is not a word)
        valid_already = [word for word in already if word in words]

        valid_already.sort()

        return valid_already[-1] if valid_already else ""

if __name__ == "__main__":
    s = Solution()
    words = ['z', 'y', 'yo', 'ew', 'fc', 'qm', 'zrc', 'fcm', 'qmo', 'ewq', 'yod', 'yodn', 'fcmz', 'ewqz']
    print(s.longestWord(words))
