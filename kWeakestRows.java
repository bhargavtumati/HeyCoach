/*### Problem Statement

Given a binary matrix `mat` where each row represents a group of soldiers:

* `1` represents a soldier.
* `0` represents a civilian.

Rows are sorted in non-increasing order (all soldiers appear before civilians).

Find the indices of the **k weakest rows** in the matrix.

A row is weaker if:

1. It has fewer soldiers.
2. If two rows have the same number of soldiers, the row with the smaller index is weaker.

Return the indices of the `k` weakest rows.

### Example

**Input:**

```text
mat = [
 [1,0],
 [1,0],
 [1,0],
 [1,1]
]

k = 4
```

**Soldier count:**

```text
Row 0 → 1 soldier
Row 1 → 1 soldier
Row 2 → 1 soldier
Row 3 → 2 soldiers
```

Sorted by strength:

```text
Row 0, Row 1, Row 2, Row 3
```

**Output:**

```text
[0,1,2,3]
```

### Approach

* Count the number of soldiers (`1`s) in each row.
* Store the count along with the row index.
* Sort rows based on:

  1. Number of soldiers.
  2. Row index.
* Return the first `k` row indices.

### Complexity

Let:

* `m` = number of rows
* `n` = number of columns

**Your approach:**

* Counting soldiers: `O(m × n)`
* Sorting: `O(m log m)`

**Time Complexity:** `O(m × n + m log m)`
**Space Complexity:** `O(m)`

**Optimization:** Since rows are sorted, binary search can find the soldier count in each row in `O(log n)`, reducing counting time to `O(m log n)`.
 */


import java.util.*;
class kWeakestRows {
    public int[] Solution(int[][] mat, int k) {
        int matl[]=new int[k],count=0;
        ArrayList<Integer> al=new ArrayList<>();
        ArrayList<Integer> al2=new ArrayList<>();
        for (int i=0;i<mat.length;i++){
            count=0;
            for(int j=0;j<mat[0].length;j++){
                if(mat[i][j]==1)
                    count++; 
            }
            al.add(count);
            
        }
        al2.addAll(al);
        int h=0;
        Collections.sort(al2);
       for(int c:al2){
        for(int i=0;i<al.size();i++){
            if(c==al.get(i)&&h<k){
                
            matl[h++]=i;
            break;
            }
        }
       }
        return matl;
    }
    public static void main(String args[]){
kWeakestRows as=new kWeakestRows();
int[][] fh = {{1, 0}, {1, 0}, {1, 0}, {1, 1}}; 

int[] ch=as.Solution(fh, 4);
 
for(int c:ch){
System.out.print(c+" ");
}
    }
}