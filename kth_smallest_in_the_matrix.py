"""
Kth Smallest in the Matrix
Kunal has an matrix of size nm. The cell in the ith row and jth column contain the value equals to ij. Help him to find the Kth smallest in the matrix.

Example:
Suppose n=3 , m=3 and k=5 then if we arrange all elements in the matrix in the sorted order then 
they are 1 2 2 3 3 4 6 6 9 and the 5th smallest here is 3 so our answer is 3.
Input
The input contains three integers n , m and k (1≤n,m≤5e5 , 1≤k≤n*m).
Output:
Print one integer, kth number in ascending order in the Matrix.
Sample Input 1
3 4 4
Sample Output 1
3

Sample Input 2
5 6 16
Sample Output 2
9
"""

def getkthsmallest(n,m,k):
    li=[]
    for i in range(1,n+1):
        for j in range(1,m+1):
            li.append(i*j)
    li.sort()
    
    return li[k-1]
n=3
m=4
k=4
print(getkthsmallest(n,m,k))