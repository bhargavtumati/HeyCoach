/*### Problem Statement

Given a string containing digits from `2` to `9`, return all possible **letter combinations** that the number could represent based on the telephone keypad mapping.

Each digit maps to a set of letters, and the output should contain all possible combinations of those letters.

### Example

**Input:**

```text
digits = "23"
```

**Mapping:**

```text
2 → abc
3 → def
```

**Output:**

```text
["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

### Explanation:

For digit `2`, possible letters are:

```text
a, b, c
```

For digit `3`, possible letters are:

```text
d, e, f
```

Combining each letter gives all possible results.

### Approach

* Store the phone keypad mapping.
* Start with an empty combination.
* For each digit:

  * Add every possible letter of that digit to existing combinations.
  * Build new combinations iteratively.

### Complexity

Let:

* `n` = number of digits
* `k` = maximum letters for a digit (4)

**Time Complexity:** `O(4ⁿ × n)`
**Space Complexity:** `O(4ⁿ × n)` (to store all combinations)

### Key Idea

Each digit creates multiple choices, so the problem is solved by generating the **Cartesian product** of all possible letters.
*/


#include <iostream>
#include <vector>
using namespace std;

class LetComb {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        
        vector<string> mapping = {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        vector<string> result;
        result.push_back(""); // Start with an empty string in the result
        
        for (char digit : digits) {
            vector<string> temp;
            for (string combination : result) {
                for (char letter : mapping[digit - '0']) {
                    temp.push_back(combination + letter);
                }
            }
            result.swap(temp); // Update the result with the new combinations

        }
        
        return result;
    }
};

int main() {
    LetComb lc;
    vector<string> combinations = lc.letterCombinations("23");
    cout << "Letter combinations for \"23\":\n";
    for (const string& combo : combinations) {
        cout << combo << " ";
    }
    cout << endl;
    return 0;
}