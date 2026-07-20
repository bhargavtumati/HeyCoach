/*### Problem Statement

Given a matrix `mat` and an integer `k`, return a matrix where each cell contains the **sum of all elements within a k-radius block** around that cell.

For each cell `(i, j)`, calculate the sum of elements inside the rectangle:

```
row: i-k to i+k
col: j-k to j+k
```

Cells outside the matrix boundaries are ignored.

### Example

**Input:**

```text
mat =
[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

k = 1
```

**Output:**

```text
[
 [12,21,16],
 [27,45,33],
 [24,39,28]
]
```

### Explanation

For cell `(1,1)`:

Block with `k = 1`:

```
1 2 3
4 5 6
7 8 9
```

Sum:

```
1+2+3+4+5+6+7+8+9 = 45
```

So the center value becomes `45`.

### Approach

* For every cell:

  * Find the valid row and column boundaries using `max()` and `min()`.
  * Traverse the block and calculate the sum.
  * Store the result.

### Complexity

Let:

* `m` = number of rows
* `n` = number of columns

For each cell, we scan up to `(2k+1) × (2k+1)` elements.

**Time Complexity:**
`O(m × n × k²)`

**Space Complexity:**
`O(m × n)` for the result matrix.

### Optimization

Using a **2D prefix sum matrix**, the block sum can be calculated in `O(1)` per cell.

Optimized complexity:

* **Time:** `O(m × n)`
* **Space:** `O(m × n)`
 */


class matrixBlockSum  {
    public int[][] Solution (int[][] mat, int k) {
        int[][] result=new int[mat.length][mat[0].length];
       for(int i=0;i<mat.length;i++){
        for(int j=0;j<mat[0].length;j++){
            int rs=Integer.max(0,i-k);
            int re=Integer.min(mat.length-1,i+k);
            int cs=Integer.max(0,j-k);
            int ce=Integer.min(mat[0].length-1,j+k);
            int sum=0;
for(int l=rs;l<=re;l++){
    for(int m=cs;m<=ce;m++){
       sum+=mat[l][m];
    }
}
result[i][j]=sum;
System.out.print(result[i][j]+" ");
        }
        System.out.println();
       }
       return result;
    }
    public static void main(String args[]){
        int[][] mat={{1,2,3},{4,5,6},{7,8,9}};
        int k=1;
        matrixBlockSum m = new matrixBlockSum();
       m.Solution(mat, k);
    }
}