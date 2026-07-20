"""### Problem Statement

You are given:

* A list of words.
* A list of available letters.
* A score value for each alphabet character.

Find the **maximum total score** that can be obtained by selecting a subset of words.

Rules:

* A word can be selected only if all its characters are available in the given letters.
* Each letter can be used only as many times as it appears in `letters`.
* The score of a word is the sum of scores of its characters.

Return the maximum possible score.

### Example

**Input:**

```text
words = ["da","ac","aba","abcc","cadc"]

letters = ["a","a","a","a","b","c","c","c","d","d","d"]

score = [3,7,9,3,...]
```

**Output:**

```text
50
```

### Explanation:

Choosing:

```text
"aba" + "cadc"
```

Uses available letters:

```
aba → a,b,a
cadc → c,a,d,c
```

Total score:

```
aba  = 3+7+3 = 13
cadc = 9+3+3+3 = 18
```

The algorithm finds the combination with the maximum score.

### Approach

* Use **backtracking** to explore two choices for every word:

  1. Skip the word.
  2. Include the word (if possible).

* Maintain a frequency count of available letters.

* Before choosing a word:

  * Check whether enough characters exist.

* Temporarily reduce letter counts.

* After recursion, restore the letters (**backtracking**).

### Complexity

Let:

* `n` = number of words.
* `m` = maximum length of a word.

Each word has two choices:

```
take / skip
```

Worst case:

**Time Complexity:**

```
O(2^n × m)
```

**Space Complexity:**

```
O(n + 26)
```

* `n` recursion depth.
* `26` character frequency storage.

### Key Idea

Backtracking tries all possible combinations of words while maintaining the available letters. The best score among all valid combinations is returned.
"""

from collections import Counter
from typing import List
class Solution:
    def can_form_word(self, w, letter_cnt):
            word_cnt=Counter(w)
            for c in word_cnt:
               if word_cnt[c]>letter_cnt[c]:
                   return False
            return True
    def get_score(self,w,score):
            res=0
            for c in w:
                res+=score[ord(c)-ord('a')]
            return res
    def max_score_words(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        letter_cnt = Counter(letters)
        def backtrack(i):
            if i == len(words):   # base logic
                return 0
            res = backtrack(i+1)  # skip the word
            if self.can_form_word(words[i],letter_cnt):  #include word  (when possible) 
                for c in words[i]:
                    letter_cnt[c] -= 1
                res = max(res, self.get_score(words[i], score) + backtrack(i+1))
                for c in words[i]:
                    letter_cnt[c] += 1
            return res
        return backtrack(0)         #https://www.youtube.com/watch?v=1cV8Hq9IAk4
    
if __name__=="__main__":
    words=["da","ac","aba","abcc","cadc"]
    letters=["a","a","a","a","b","c","c","c","d","d","d"]
    score=[3,7,9,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    c = Solution()
    print(c.max_score_words(words,letters,score))