/*### Problem Statement: Regular Expression Matching

Given an input string `s` and a pattern `p`, implement regular expression matching with support for:

* `.` → Matches **any single character**.
* `*` → Matches **zero or more occurrences** of the character immediately before it.

The matching should cover the **entire string**, not just a substring.

Return:

* `true` if the string matches the pattern.
* `false` otherwise.

---

### Example 1:

**Input:**

```java
s = "aa"
p = "a"
```

**Output:**

```text
false
```

**Explanation:**

Pattern `"a"` matches only one `a`, but string contains two `a` characters.

---

### Example 2:

**Input:**

```java
s = "aa"
p = "a*"
```

**Output:**

```text
true
```

**Explanation:**

`a*` means zero or more `a` characters.

So:

```
a* → aa
```

The pattern matches the entire string.

---

### Example 3:

**Input:**

```java
s = "ab"
p = ".*"
```

**Output:**

```text
true
```

**Explanation:**

`.` matches any character.

`.*` means any number of any characters.

So:

```
.* → ab
```

---

### Example 4:

**Input:**

```java
s = "a"
p = "b*"
```

**Output:**

```text
false
```

**Explanation:**

`b*` can match:

```
""
"b"
"bb"
"bbb"
...
```

It cannot match `"a"`.

---

## Approach Used: Dynamic Programming + Recursion

The state:

```java
dp[i][j]
```

represents:

> Whether `s[i...]` matches `p[j...]`

---

### Cases:

### 1. Pattern has `*`

Example:

```
a*
```

Two choices:

#### Ignore `*`

```
a* → ""
```

Move pattern forward.

#### Use `*`

```
a* → a, aa, aaa...
```

Stay on the same pattern position and move string forward.

---

### 2. Current characters match

Condition:

```java
s.charAt(si) == p.charAt(pi)
```

or

```java
p.charAt(pi) == '.'
```

Move both pointers:

```
si + 1
pi + 1
```

---

### Example:

Input:

```java
s = "a*"
p = "b*"
```

Check:

```
a* vs b*
```

First characters:

```
a != b
```

`b*` can match zero b's, but remaining string is `"a*"`, so result:

```
false
```

---

### Complexity:

Let:

* `m = length of s`
* `n = length of p`

Time Complexity:

```
O(m × n)
```

Each state is calculated once.

Space Complexity:

```
O(m × n)
```

For memoization table.

---

This is the classic **LeetCode 10 - Regular Expression Matching** problem.
 */

import java.util.*;

class RegularExMat {
    int sl, pl; // Lengths of string s and pattern p

    // Recursive function to check if there is a match between s and p
    public boolean isMatch(int si, int pi, String s, String p, int[][] dp) {
        // If both strings have been exhausted, return true
        if (si >= sl && pi >= pl)
            return true;

        // If pattern is exhausted but string is not, return false
        if (si < sl && pi >= pl)
            return false;

        // If string is exhausted but pattern still has elements
        if (si >= sl && pi < pl) {
            // If remaining pattern consists of only '*' characters, return true
            pi++;
            while (pi < pl) {
                if (p.charAt(pi) != '*') return false;
                pi += 2;
            }
            if (p.charAt(pl - 1) != '*') return false;
            return true;
        }

        // If the result for current state (si, pi) is already computed, return it
        if (dp[si][pi] != -1)
            return dp[si][pi] == 1;

        // If the next character in pattern is '*', handle it
        if (pi < pl - 1 && p.charAt(pi + 1) == '*') {
            // Case 1: Don't use the '*' character
            boolean notUse = isMatch(si, pi + 2, s, p, dp);
            // Case 2: Use the '*' character
            boolean use = (s.charAt(si) == p.charAt(pi) || p.charAt(pi) == '.') && isMatch(si + 1, pi, s, p, dp);
            dp[si][pi] = (notUse || use) ? 1 : 0;
            return notUse || use;
        }
        // If the next character in pattern is '.' or matches the current character in string
        else if (p.charAt(pi) == '.' || s.charAt(si) == p.charAt(pi)) {
            boolean result = isMatch(si + 1, pi + 1, s, p, dp);
            dp[si][pi] = result ? 1 : 0;
            return result;
        }

        dp[si][pi] = 0;
        return false;
    }

    public boolean isMatch(String s, String p) {
        sl = s.length();
        pl = p.length();
        int[][] dp = new int[sl + 1][pl + 1]; // Memoization table
        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }
        return isMatch(0, 0, s, p, dp); // Start the recursive function
    }

    public static void main (String Args[]){
RegularExMat rm = new RegularExMat();
String s="a*";
String p="b*";
System.out.println(rm.isMatch(s,p));
    }
}