"""
Let’s Swap
Description: Ajay and Vijay are playing an intense game, they are provided an array a with n positive integers which has the following rules:

 If a1=0, the game ends and the person whose turn it is loses. (a1 is the element at 1th position)
 In a move a player can choose i such that 2<=i<=n. The player decreases the value of a1 by 1 and swaps ai (ith position) by a1(1th position).
 Ajay always plays first.
Print the winner of the game if they both play the game logically.

Example:

Let’s say that n=2 and a = [1,1] now Ajay goes first and he chooses i=2 (only choice), now a1=1 gets reduced to 0 and after that it is swapped with a2 = 1 so the array we end up with is a = [1,0]

Now it is the turn of Vijay, so he then chooses i=2 (only choice) , now a1=1 gets reduced to zero and after that it is swapped with a2=0 and the array is a= [0,0]. It’s Ajay’s turn now and a1 = 0, thus the winner of the game is “Vijay”.

Sample Input:

N = 2, a = [2, 1]

Sample Output:

Ajay

Constraints:

2<=n<=10^4

1<=ai<=10^8"""

def solve(ar, n):
  #Write your code here
    mi = min(ar[1:])
    
    if ar[0] == mi:
        print("Vijay")
    else:
        print("Ajay")



n = 2 
    #int(input())
ar = [2,1] 
    #list(map(int, input().split()))

solve(ar, n)