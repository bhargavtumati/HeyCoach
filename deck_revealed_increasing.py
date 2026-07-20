"""Your code solves:

* LeetCode 950: Reveal Cards In Increasing Order

## Problem Statement

You are given an integer array `deck` where every integer is unique.

You can order the deck in any way you want. Initially, all cards start face down in one deck.

You repeatedly perform the following steps until all cards are revealed:

1. Take the top card of the deck, reveal it, and remove it from the deck.
2. If there are still cards in the deck, take the next top card and move it to the bottom of the deck.
3. Repeat the process until no cards remain.

Return an ordering of the deck that would reveal the cards in **increasing order**.

---

### Example 1

**Input**

```text
deck = [17,13,11,2,3,5,7]
```

**Output**

```text
[2,13,3,11,5,17,7]
```

**Explanation**

If the deck is arranged as:

```text
[2,13,3,11,5,17,7]
```

The reveal process is:

| Deck Before Reveal | Revealed | Deck After Moving Next Card |
| ------------------ | -------- | --------------------------- |
| [2,13,3,11,5,17,7] | 2        | [3,11,5,17,7,13]            |
| [3,11,5,17,7,13]   | 3        | [5,17,7,13,11]              |
| [5,17,7,13,11]     | 5        | [7,13,11,17]                |
| [7,13,11,17]       | 7        | [11,17,13]                  |
| [11,17,13]         | 11       | [13,17]                     |
| [13,17]            | 13       | [17]                        |
| [17]               | 17       | []                          |

The revealed sequence is:

```text
2, 3, 5, 7, 11, 13, 17
```

which is in increasing order.

---

### Example 2

**Input**

```text
deck = [1,1000]
```

**Output**

```text
[1,1000]
```

---

### Constraints

```text
1 <= deck.length <= 1000
1 <= deck[i] <= 10^6
All the values of deck are unique.
```

### Function Signature

```python
def deckRevealedIncreasing(deck: List[int]) -> List[int]:
```

Return an ordering of the deck such that revealing cards using the given process results in the cards appearing in increasing order.

"""
from typing import List

class Solution:

    def next_index(self, index: int, size: int) -> int:
        return (index + 1) % size

    def deck_revealed_increasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)

        result = [-1] * len(deck)

        index = 0
        skip = False

        while deck:
            if result[index] == -1:
                if skip:
                    skip = False
                else:
                    result[index] = deck.pop()
                    skip = True

            index = self.next_index(index, len(result))

        return result


if __name__ == "__main__":
    deck = [17, 13, 11, 2, 3, 5, 7]

    s = Solution()
    print(s.deck_revealed_increasing(deck))