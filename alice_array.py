"""
Alice and his sister are playing with two arrays a which consists n elements 
and b consisting of m elements. The array a is given to Alice and b to his 
sister. As Alice is really naughty she wants the minimum value of his array 
a should be at least as much as the maximum value of his sister's array b. 
Now You have to help Alice in achieving his condition. You can perform multiple 
operations on the array. In single operation, you are allowed to increase 
or decrease any element of any of the arrays by 1. Note that you are allowed 
to apply the operation on any index of the array multiple times. You need to 
find the minimum number of operations required to satisfy Alice's condition.

constraints:
1<=len(a),len(b)<=10^6
"""
class Solution:
    def minimum_operations(self, a, b):
      #Write your code here
        n = len(a)   
        m = len(b)

        st = set()   # added a , b array to set

        for i in range(n):
            st.add(a[i])

        for i in range(m):
            st.add(b[i])

        a.sort()
        b.sort()

        pa = [0] * n   #created an array of size n
        pb = [0] * m

        pa[0] = a[0]   #assign value in pa,pb  array
        pb[0] = b[0]

        for i in range(1, n):    #cummulative sum
            pa[i] = pa[i - 1] + a[i]

        for i in range(1, m):
            pb[i] = pb[i - 1] + b[i]

        ans = float('inf')

        for c in st:   #no of moves 
            ubb = self.binary_search(b, c)   
            sb = self.pre(ubb, m - 1, pb)   

            lba = self.binary_search(a, c)  
            sa = self.pre(0, lba - 1, pa)   

            rb = sb - (c * (m - ubb))
            ra = (c * lba) - sa

            ans = min(ans, rb + ra)

        return ans

    def binary_search(self, arr, target):     #get address of target
        low, high = 0, len(arr)
        while low < high:
            mid = low + (high - low) // 2
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low

    def pre(self, l, r, p):       #
        if l > r:
            return 0
        if l == 0:
            return p[r]
        return p[r] - p[l - 1]
if __name__=="__main__":
    a=[-1,1]
    b=[0,1]
    d=Solution()
    print(d.minimum_operations(a,b))                