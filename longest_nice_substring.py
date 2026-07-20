"""### Problem Statement

Given a string `s`, find the **longest nice substring**.

A substring is called **nice** if for every alphabet character present in it, **both lowercase and uppercase versions** of that character exist.

Return the longest nice substring. If multiple answers exist, return any one. If no nice substring exists, return an empty string.

### Example

**Input:**

```text
s = "aArRk"
```

**Output:**

```text
"aArR"
```

### Explanation:

Substring:

```text
a A r R
```

contains:

```text
a and A
r and R
```

Both cases exist, so it is a nice substring.

Character:

```text
k
```

has no uppercase `K`, so it cannot be included.

### Approach

* Generate all possible substrings.
* For each substring:

  * Store its characters in a set.
  * Check whether every character has both lowercase and uppercase forms.
* Keep the longest valid substring.

### Complexity

Let `n` be the length of the string.

* **Time Complexity:** `O(n³)`

  * `O(n²)` substrings
  * `O(n)` validation for each substring

* **Space Complexity:** `O(n)` for storing characters in the set.

### Key Idea

A substring is nice only when:

```text
lowercase character exists AND uppercase character exists
```

For example:

```
aA → Nice
aB → Not Nice
```
"""


class longestNiceSubstring:
    def Solution (self, s: str) -> str:
        N = len(s)
        best = ""
        def good(start,end):
            t=set(s[start:end])

            for x in t:
               if(x.lower() in t) != (x.upper() in t):
                  return False
            return True
        for start in range(N):
            for end in range(start +1,N+1):
                    if good(start,end) and end-start >len(best):
                          best = s[start:end]
        return best
if __name__ == "__main__":
     s="aArRk"
     ls=longestNiceSubstring()
     print(ls.Solution(s))