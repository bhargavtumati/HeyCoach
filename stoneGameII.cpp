/*### Problem Statement: Stone Game II

Alice and Bob are playing a game with a row of stone piles.

* The piles are represented by an integer array `piles`.
* Alice starts the game.
* Players take turns removing stones from the beginning of the remaining piles.
* Let `M` be a variable that starts with `1`.

On each turn, a player can take **X piles**, where:

```
1 <= X <= 2 * M
```

After taking `X` piles:

```
M = max(M, X)
```

The player who collects the maximum number of stones wins.

Return the **maximum number of stones Alice can collect** assuming both players play optimally.

---

### Example 1

**Input:**

```text
piles = [2,7,9,4,4]
```

**Output:**

```text
10
```

**Explanation:**

Possible optimal moves:

```
Alice takes: [2]
Bob takes: [7]
Alice takes: [9,4,4]
```

Alice collects:

```
2 + 4 + 4 = 10
```

Bob collects:

```
7 + 9 = 16
```

Alice cannot get more than 10 stones if Bob also plays optimally.

---

### Example 2

**Input:**

```text
piles = [1,2,3,4,5,100]
```

**Output:**

```text
104
```

**Explanation:**

Alice can choose moves optimally to take the maximum possible stones.

---

### Constraints

```text
1 <= piles.length <= 100

1 <= piles[i] <= 10^4
```

---

### Function Signature

C++:

```cpp
int Solution(vector<int>& piles)
```

Return the maximum number of stones Alice can collect.

---

## Approach Used in Your Code

Your solution uses:

### Dynamic Programming + Minimax

State:

```cpp
help(i, M)
```

means:

* `i` → current starting index of piles
* `M` → current maximum allowed move value

It returns:

```
Alice stones - Bob stones
```

from this state assuming both play optimally.

---

### Transition

For every possible move:

```cpp
for(int j=0; j<2*M; j++)
```

Alice can take:

```
j+1 piles
```

The stones taken:

```cpp
tot += piles[i+j]
```

The opponent's best difference:

```cpp
help(i+j+1, max(M,j+1), piles)
```

So:

```cpp
ans = max(
    ans,
    current stones - opponent difference
);
```

---

### Why `(sum + diff) / 2`?

Let:

```
Alice stones = A
Bob stones = B
```

Your DP returns:

```
diff = A - B
```

Total stones:

```
sum = A + B
```

Adding:

```
sum + diff

= (A+B) + (A-B)

= 2A
```

Therefore:

```
Alice stones = (sum + diff) / 2
```

---

### Example:

```
piles = [2,7,9,4,4]

Total = 26

DP difference:
Alice - Bob = -6

Alice stones:

(26 + (-6)) / 2

= 20/2

= 10
```

---

### Complexity

Number of states:

```
i * M
```

Maximum:

```
100 * 200
```

For each state, we try up to `2M` moves.

### Time Complexity:

```
O(N^3)
```

### Space Complexity:

```
O(N^2)
```

for the DP table.
*/


#include <bits/stdc++.h>
using namespace std;

class stoneGameII  {
public:
    int dp[101][201];
    int help(int i,int M,vector<int>&piles){// gets difference of no of stones alice and bob playing optimally(best case) 
        if(i>=piles.size())// return 0 if null
        return 0;
        if(dp[i][M]!=-1)
        return dp[i][M];
        int tot=0;
        int ans=INT_MIN;
        for(int j=0;j<2*M;j++){
            if(i+j<piles.size())
            tot+=piles[i+j];
            ans=max(ans,tot-help(i+j+1,max(M,j+1),piles));//max of ans,tot picked-opponents total picked,
        }
        
        return dp[i][M]=ans;
    }
    int Solution(vector<int>& piles) {
        int sum=0;
        memset(dp,-1,sizeof dp); //memset() copies the value static_cast<unsigned char>(val) into each of the first num characters of the object pointed to by obj.
        for(auto a:piles)
        sum+=a;   //caluculating sum
        int diff=help(0,1,piles); //0 is start , 1 is max piles can be taken, piles.
        cout<<diff<<endl;//alice get 10 and bob gets 16 so diff =-6 
        return (sum+diff)/2;// 26-6/2==10 i.e no of stones alice gets

    }
};
int  main(){
    vector<int> ch={2,7,9,4,4};
    stoneGameII j;
    cout<<j.Solution(ch);

}