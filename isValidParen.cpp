/**### Problem Statement

Given a string `s` containing characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine whether the brackets are **valid**.

A string is valid if:

1. Every opening bracket has a corresponding closing bracket.
2. Opening brackets are closed in the correct order.
3. Each closing bracket matches the same type of opening bracket.

Return `true` if the string is valid, otherwise return `false`.

### Example

**Input:**

```text
s = "()[]{}"
```

**Output:**

```text
true
```

**Explanation:**

```
( ) → matched
[ ] → matched
{ } → matched
```

---

**Input:**

```text
s = "(){}}{"
```

**Output:**

```text
false
```

**Explanation:**

```
Extra closing bracket } exists and order is invalid.
```

### Approach

* Use a **stack** to store opening brackets.
* When an opening bracket is found, push it into the stack.
* When a closing bracket is found:

  * Check whether the top of the stack contains the matching opening bracket.
  * If not, the string is invalid.
  * Otherwise, remove the opening bracket.
* At the end, the stack should be empty.

### Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

### Key Idea

The stack follows **LIFO (Last In First Out)**, which matches the rule that the most recent opening bracket must be closed first.
*/


#include <iostream>
#include <stack>
using namespace std;

class isValidParen {
public:
    bool isValid(string s) {
       stack<char> st;
       bool val=false;
       for(int i=0;i<s.length();i++){
        if(s.at(i)=='('||s.at(i)=='['||s.at(i)=='{'){
st.push(s.at(i));
val=false;
        }
        else if(st.size()>=1){
         if(s.at(i)==')'&&st.top()=='('){
st.pop();
if(i==s.length()-1)
val=true;
        }
        
        else if(s.at(i)==']'&&st.top()=='['){
st.pop();
if(i==s.length()-1)
val=true;
        }
        
        else if(s.at(i)=='}'&&st.top()=='{'){
st.pop();
if(i==s.length()-1)
val=true;
        }
        
        else{
         val= false;
         break;}
       }
       else{
        val = false;
       break;
       }
       
    }
    return val;
    }
};

int main()
{
    string s="(){}}{";
    isValidParen ch;
    cout << ch.isValid(s); 
    
}