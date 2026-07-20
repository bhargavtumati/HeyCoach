"""
LIS
Longest Increasing Subsequence (LIS)
Given an array arr[] of size N, find the length of the Longest Increasing Subsequence (LIS) in the array. The LIS is defined as the longest subsequence where each element is strictly greater than the preceding one.

Input Format:

The first line contains an integer N, the size of the array.
The second line contains Nspace-separated integers representing the elements of the arrayarr[].
Output Format:

Output a single integer, the length of the longest increasing subsequence in the given array.
Constraints:

1 <= N <= 2500
-10^5 <= arr[i] <= 10^5, where arr[i] denotes the i-th element of the array arr[].
Sample Inputs and Outputs:

Input:

5
3 10 2 1 20
Output:

3
Explanation: The longest increasing subsequence is {3, 10, 20}, which has a length of 3.

Input:

2
3 2
Output:

1
Explanation: The longest increasing subsequences are {3}and{2}, both with a length of 1.

Input:

6
50 3 10 7 40 80
Output:

4
Explanation: The longest increasing subsequence is {3, 7, 40, 80}, which has a length of 4."""

class Solution:
    def lis(self, arr, n): 
         dp=[1]*n
         for i in range(1,n):
           for j in range(i):
             if arr[i]>arr[j]:   # when arr[i] > arr[j] increment by dp[i] by max of (dp[i],d[j]+1)
               dp[i]=max(dp[i],dp[j]+1)
  
         return max(dp) if n>0 else 0
    
if __name__=="__main__":
   s=Solution()
   arr=[3,10,2,1,20]
   n=5
   print(s.lis(arr,n))

