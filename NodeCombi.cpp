"""### Problem Statement: Merge Two Sorted Linked Lists

You are given the heads of two **sorted singly linked lists** `l1` and `l2`.

Your task is to merge the two linked lists into a **single sorted linked list** by rearranging the existing nodes.

Return the head of the merged sorted linked list.

---

### Example:

**Input:**

First linked list:

```
l1 = 0 → 2 → 4 → 6 → 8
```

Second linked list:

```
l2 = 1 → 3 → 5 → 7 → 9
```

---

### Output:

```
0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9
```

---

### Explanation:

Compare the first nodes of both lists:

```
l1: 0
l2: 1
```

`0` is smaller, so it becomes the first node.

Then compare:

```
l1: 2
l2: 1
```

`1` is smaller, so it comes next.

Continue this process until all nodes are merged.

---

### Example 2:

**Input:**

```
l1 = []
l2 = [1,3,5]
```

**Output:**

```
1 → 3 → 5
```

---

### Constraints:

```
0 <= number of nodes <= 50
-100 <= Node.val <= 100
```

The linked lists are sorted in non-decreasing order.

---

### Algorithm:

1. If one list is empty, return the other list.
2. Compare the values of current nodes of both lists.
3. Attach the smaller node to the result list.
4. Move that list pointer forward.
5. Continue until both lists are merged.

---

### Complexity:

Let:

* `m` = number of nodes in `l1`
* `n` = number of nodes in `l2`

Time Complexity:

```
O(m + n)
```

Space Complexity:

```
O(1)
```

because no extra linked list is created; existing nodes are reused.

---

This is the classic **LeetCode 21 - Merge Two Sorted Lists** problem.
"""


#include <iostream>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};
void printList(ListNode* head) {
    while (head) {
        std::cout << head->val << " ";
        head = head->next;
    }
    std::cout << std::endl;
}
class NodeCombi {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1 == NULL) return l2;
        if(l2 == NULL) return l1;
        if(l1->val > l2->val) 
        std::swap(l1 , l2);
        ListNode *res = l1;
        
        while(l1 != NULL && l2 != NULL ){
            ListNode *temp = NULL;
            while(l1!=NULL && l1->val<=l2->val){
                temp = l1;
                l1 = l1->next;
            }
            temp->next=l2;
            std::swap(l1,l2);
        }
        
        return res;
    }
};

int main(){
  ListNode* n1 = new ListNode(0);//nullptr
    //n1->next = new ListNode(2);
    //n1->next->next = new ListNode(4);
    //n1->next->next->next = new ListNode(6);
    //n1->next->next->next->next = new ListNode(8);

    ListNode* n2 = new ListNode(1);
 n2->next = new ListNode(3);
    n2->next->next = new ListNode(5);
    n2->next->next->next = new ListNode(7);
    n2->next->next->next->next = new ListNode(9);
    NodeCombi nc;
   printList(nc.mergeTwoLists(n1,n2));


    
    
}
