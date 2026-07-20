"""### Problem Statement

You are given two groups:

* `students[i]` represents the answers of the `i`th student.
* `mentors[j]` represents the answers of the `j`th mentor.

Each student must be assigned to exactly one mentor.

The **compatibility score** between a student and mentor is the number of positions where their answers are the same.

Return the **maximum total compatibility score** possible by assigning students to mentors.

### Example

**Input:**

```text
students =
[
 [1,1,0],
 [1,0,1],
 [0,0,1]
]

mentors =
[
 [1,0,0],
 [0,0,1],
 [1,1,0]
]
```

**Output:**

```text
8
```

### Explanation:

Compatibility scores:

```
          Mentor 0  Mentor 1  Mentor 2
Student 0     1        1        3
Student 1     2        2        2
Student 2     2        3        1
```

Best assignment:

```
Student 0 → Mentor 2 = 3
Student 1 → Mentor 0 = 2
Student 2 → Mentor 1 = 3
```

Total:

```
3 + 2 + 3 = 8
```

### Approach

1. Create a compatibility score matrix:

   * `score[i][j]` stores the matching answers between student `i` and mentor `j`.

2. Generate all possible mentor assignments using permutations.

3. Calculate the total score for each assignment.

4. Return the maximum score.

### Complexity

Let `m` be the number of students/mentors.

* Creating score matrix:

  * `O(m² × n)` where `n` is the number of questions.

* Trying all assignments:

  * `O(m! × m)`

**Total Time Complexity:**
`O(m! × m)`

**Space Complexity:**
`O(m²)` for the score matrix.

### Key Idea

This is a **maximum assignment problem**. The solution checks every possible matching of students and mentors and selects the one with the highest compatibility score. For larger inputs, Dynamic Programming with bitmasking can optimize it.
"""


from itertools import permutations
from typing import List


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)
        
        score = [[0]* m for _ in range(m)]
        for i in range(m): 
            for j in range(m): 
                score[i][j] = sum(x == y for x, y in zip(students[i], mentors[j]))
        
        ans = 0 
        for perm in permutations(range(m)): 
            ans = max(ans, sum(score[i][j] for i, j in zip(perm, range(m))))
        return ans 
if __name__=="__main__":
    students = [[1,1,0],[1,0,1],[0,0,1]]
    mentors = [[1,0,0],[0,0,1],[1,1,0]]
    v=Solution()
    print(v.maxCompatibilitySum(students,mentors))
