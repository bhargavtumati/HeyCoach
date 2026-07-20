
"""
### Problem Statement

Given two strings `sequence` and `word`, find the **maximum number of times `word` can be repeated consecutively** as a substring inside `sequence`.

Return the maximum `k` such that:

```text
word + word + word + ... (k times)
```

is a substring of `sequence`.

### Example

**Input:**

```text id="3f6u8v"
sequence = "ababc"
word = "ab"
```

**Output:**

```text id="qf5n2q"
2
```

### Explanation:

`word = "ab"`

Repeated forms:

```text id="5b5u8x"
ab       → exists
abab     → exists
ababab   → does not exist
```

Maximum repetitions = `2`.

### Approach

* Start with count `0`.
* Check if `word` exists in the remaining part of `sequence`.
* If found:

  * Increase the count.
  * Move the pointer forward after the matched word.
* Continue until no more matches are found.

### Complexity

Let:

* `n` = length of sequence
* `m` = length of word

**Time Complexity:** `O(n × m)`
(Substring searching can take `O(m)`)

**Space Complexity:** `O(1)`

### Key Idea

The answer is the number of consecutive occurrences of `word` that can be extracted from `sequence`.
"""
class maxRepeating:
    def Solution(self, sequence: str, word: str) -> int:
        count=0
        l=0
        while l<len(sequence):
          if word in sequence[l:]:
            count+=1
            l+=sequence[l:].index(word)+len(word)
            l+=len(word)
          else:
             break
            
          
        return count
    
if __name__ =="__main__":
   sequence="aaabaaaabaaabaaaabaaaabaaaabaaaaba"
   word="aaaba"
   al=maxRepeating()
   print(al.Solution(sequence,word))