"""### Problem Statement

Given a string `s` containing only `'('` and `')'`, find the **length of the longest valid (well-formed) parentheses substring**.

A valid parentheses substring is a substring where every opening bracket has a matching closing bracket in the correct order.

### Example

**Input:**

```text
s = ")()())"
```

**Output:**

```text
4
```

### Explanation:

Valid substrings are:

```text
()
()
```

The longest valid substring is:

```text
()()
```

Length:

```text
4
```

### Approach

* Use a **stack** to store indices of unmatched parentheses.
* Initialize stack with `-1` as a base index.
* For each character:

  * If `'('`, store its index.
  * If `')'`, remove the matching `'('` index.
  * If stack becomes empty, store the current index as a new base.
  * Otherwise, calculate the valid substring length using:

```text
current_index - stack_top
```

* Keep track of the maximum length.

### Complexity

* **Time Complexity:** `O(n)`
  (Each character is processed once)

* **Space Complexity:** `O(n)`
  (Stack stores indices)

### Key Idea

The stack stores positions where a valid parentheses sequence can start. The difference between the current index and the last unmatched position gives the length of the current valid substring.
"""


class Solution:
    def longestValidParentheses(self,s: str) -> int:
        max_length = 0
        stack = [-1]

        for i, char in enumerate(s):
            if char == '(':
                 stack.append(i)
            else:
                 stack.pop()
                 if not stack:
                     stack.append(i)
                 else:
                     max_length = max(max_length, i - stack[-1])

        return max_length
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    
    # Test cases
    test_cases = [
        "(()",          # 2
        ")()())",       # 4
        "",             # 0
        "()(())",       # 6
        "(()))())(",    # 4
    ]
    
    # Test the longestValidParentheses method with the test cases
    for test in test_cases:
        result = solution.longestValidParentheses(test)
        print(f"The longest valid parentheses in '{test}' is {result} characters long.")
