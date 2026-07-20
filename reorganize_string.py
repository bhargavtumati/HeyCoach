"""### Problem Statement: Reorganize String

Given a string `s`, rearrange the characters of the string so that **no two adjacent characters are the same**.

Return any valid rearranged string. If it is impossible to rearrange the string such that no two adjacent characters are different, return an empty string `""`.

---

### Example 1

**Input:**

```
s = "aab"
```

**Output:**

```
"aba"
```

**Explanation:**

The characters can be rearranged as `"aba"` where no two adjacent characters are the same.

---

### Example 2

**Input:**

```
s = "aaab"
```

**Output:**

```
""
```

**Explanation:**

The character `'a'` appears 3 times, but there are only 4 positions. It is impossible to place all `a` characters without having two `a`s next to each other.

---

### Example 3

**Input:**

```
s = "vvvlo"
```

**Output:**

```
"vovlv"
```

**Explanation:**

The rearranged string has no two adjacent characters that are identical.

---

### Constraints

```
1 <= s.length <= 500

s consists of lowercase English letters.
```

---

### Function Signature

Python:

```python
def reorganizeString(self, s: str) -> str:
```

Return:

* A reorganized string where adjacent characters are different.
* `""` if no such arrangement exists.
"""


class Solution:
    def reorganizeString(self, s: str) -> str:
        dic = {}
        max_value=None
        max_key=None
        for i in s:
            dic[i] = dic.get(i,0)+1     
            if max_value is None or dic[i] > max_value:
                max_value = dic[i]
                max_key = i

        if max_value > ((len(s)+1)//2):
            return ""

        res = (len(s)) * ['']
        idx = 0
        while(max_value):
            res[idx] = max_key
            idx+=2
            max_value-=1

        for key, value in dic.items():
            if key not in res:
                val = value
                while(value):
                    if idx >= len(s):
                        idx=1
                    res[idx] = key
                    idx+=2
                    value-=1
        return "".join(res)
        
if __name__ == "__main__":
    solution = Solution()
    input_string = "vvloogfhgdjgfhtrhg"
    result = solution.reorganizeString(input_string)
    print(f"Reorganized string: {result}")