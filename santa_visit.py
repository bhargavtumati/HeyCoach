"""
Santa's Visit
Description:

Since Aman was exceptionally good last year, on New Year's Eve, he was visited by Santa Claus
, who brought an enormous bag of gifts with him! The bag contains n sweet candies from the 
beloved bakery, each labeled from 1 to n corresponding to its tastiness. Notably, no two candies
 share the same tastiness. The selection of candies has a profound impact on Aman's joy. 
 One might assume that he should choose the most delicious ones — but no, the holiday magic 
 turns things around. It is the xor-sum of the tastinesses that matters, rather than the ordinary 
 sum! The xor-sum of a sequence of integers a1,a2,..,am​ is defined as the bitwise XOR of all its 
 elements: a1 XOR a2 XOR a3 XOR​…..XOR am, where XOR denotes the bitwise XOR operation. Santa Claus 
 asked Aman that he has more houses to visit, so Aman can take no more k candies from the bag. 
 Assist Aman in determining the largest xor-sum (which leads to maximum happiness!) he can achieve.

Input Format:

The first and only line contains two integers 'n' and 'k' where n denotes the sequence 
of numbers from 1 to n and k represents the number of candies that aman can take.

Output Format:

Return a single integer denoting the largest xor-sum that aman can achieve.

Sample Input:

4 3

Sample Output:

7

Explanation:

We have the sequence as 1 2 3 4 and can take upto 3 elements from it. In order to maximize the taste
 we can take 1, 2 and 3 whose XOR sum would be equal to 7 which turns out to be the maximum.

Constraints:

1<=k<=n<=10^18
"""

def santaxor(n,k):
    sumi=0
    i=1
    while (i<=(n+1-k)):
       x=0
       for j in range(i,i+k):
          
          x^=j
       print(x)
       if x>sumi:
          sumi=x
       i+=1
    return sumi
n=4
k=3
print(santaxor(n,k))