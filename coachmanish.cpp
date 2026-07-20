/*
Coach Manish
Manish is the coach of a high school football team. He has come up with a training regime of difficulty 'd' but he is afraid that it might result in his team getting exhausted quickly and prone to fatigue.
So he has decided to break the training in 'n' number of days where every day has a certain amount of difficulty and the difficulty of each day adds up to 'd' the original difficulty.
But he also wants to make sure that his training results in a greater output so he cannot spread the difficulty of training without planning. The result can be determined by calculating the GCD of the difficulty of all the days. Return the greatest result that can be achieved from the training.

Input Format:
You are given two space-separated integers d and n, denoting the total difficulty and number of days it is divided into.

Output Format:
You have to return a single integer denoting the maximum result that can be achieved from the training.

Sample Input:
9 2

Sample Output:
3

Explanation:
We can break the difficulty in 3 and 6 whose GCD results in 3 which is the greatest output possible.

Constraints:
1 <= d <= 10^5

1<= n <= d
*/



#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int solve(int d, int n) {
        // Initialize the answer to 1. This will store the maximum GCD possible.
        int ans = 1;
        
        // Loop through all possible divisors of 'd'.
        for (int i = 1; i * i <= d; i++) {
            // If 'i' is a divisor of 'd'
            if (d % i == 0) {
                // Check if dividing 'd' by 'i' results in a quotient that is greater than or equal to 'n'

        // This checks if we can split 'd' into 'n' parts each of which is at least 'd/i'
                if (n <= d / i) {
                    // If true, update the answer to be the maximum of the current answer and 'i'
                    ans = max(ans, i);
                }
                // Check if 'i' is greater than or equal to 'n'
                // This checks if we can split 'd' into 'n' parts each of which is at least 'i'
                if (n <= i) {
                    // If true, update
                   ans=max(ans,n);
                }
            }
        }
        return ans;
    }
};
    int main(){
    Solution s;
    int n=2;
    int d=9;
    cout<<s.solve(d,n);

}



