"""
1019. Next Greater Node In Linked List
Solved
Medium
Topics
Companies
Hint
You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

 

Example 1:


Input: head = [2,1,5]
Output: [5,5,0]
Example 2:


Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 104
1 <= Node.val <= 109

Hint:
We can use a stack that stores nodes in monotone decreasing order of value.
When we see a node_j with a larger value, every node_i in the stack has next_larger(node_i) = node_j .
"""


# First, we define the ListNode class as given
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        stack=[]
        result=[0]*len(nums)
        for i in range(len(nums)):
              # While stack is not empty and current element is greater than top of the stack
              while stack and nums[i] > nums[stack[-1]]:
                  # Pop from stack and set the result for popped index
                  index = stack.pop()
                  result[index] = nums[i]
              # Push the current index onto the stack
              stack.append(i)
        return result
    
# Now, let's create a linked list [2, 1, 5] as an example
node1 = ListNode(2)
node2 = ListNode(1)
node3 = ListNode(5)

node1.next = node2
node2.next = node3

# We create an instance of the Solution class
solution = Solution()

# And call the nextLargerNodes method with the head of our list
result = solution.nextLargerNodes(node1)

# Finally, we print the result
print(result)  # This should output [5, 5, 0]

