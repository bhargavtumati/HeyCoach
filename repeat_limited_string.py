"""### Problem Statement: Construct String With Repeat Limit

You are given a string `s` and an integer `repeatLimit`.

Your task is to **construct the lexicographically largest possible string** using the characters of `s` such that:

* No character appears **more than `repeatLimit` times consecutively**.
* You can use each character from `s` at most as many times as it appears.
* If a character reaches the repeat limit, you must use a smaller character (if available) to break the sequence.

Return the resulting string.

---

### Example 1

**Input:**

```text
s = "cczazcc"
repeatLimit = 3
```

**Output:**

```text
"zzcccac"
```

**Explanation:**

Character frequencies:

```
z -> 2
c -> 4
a -> 1
```

The largest character `z` can be used twice:

```
zz
```

Then `c` can be used up to 3 times:

```
ccc
```

Another `c` cannot be placed immediately, so `a` is used as a separator:

```
a
```

Remaining `c` is added:

```
c
```

Result:

```
zzcccac
```

No character appears more than 3 times consecutively.

---

### Example 2

**Input:**

```text
s = "aababab"
repeatLimit = 2
```

**Output:**

```text
"bbabaa"
```

---

### Constraints

```
1 <= s.length <= 10^5
1 <= repeatLimit <= s.length

s contains only lowercase English letters.
```

---

### Function Signature

Python:

```python
def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
```

Return the lexicographically largest string satisfying the repeat limit condition.
"""

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        hm={}
        for c in s:
            hm[c]=hm.get(c,0)+1
        r=""
        sortedhm = dict(sorted(hm.items(),reverse=True,key=lambda item:(item[0],item[1])))
        while sortedhm:
           first_key = next(iter(sortedhm))
           if not r or r[-1]!=first_key:
              count=0
              leg=sortedhm[first_key]
              while count<repeatLimit and count<leg:
                 r+=first_key
                 count+=1
                 sortedhm[first_key]-=1
                 if sortedhm[first_key]==0:
                     del(sortedhm[first_key])
           else:
               second_key=list(sortedhm)[1]    #lexogragphically maximum   z>y>x
               r+=second_key
               sortedhm[second_key]-=1
               if sortedhm[second_key]==0:
                     del(sortedhm[second_key])
               
           if len(sortedhm)==1 :
               if r:
                   if r[-1]==list(sortedhm)[0]:
                       break
        return r
if __name__=="__main__":
    s="cczazcc"
    repeatLimit=3
    j=Solution()
    print(j.repeatLimitedString(s,repeatLimit))
