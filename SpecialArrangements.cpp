/*Special Arrangements
You're a daring jewel thief infiltrating the vault of the century, protected by a complex combination lock. Each dial holds a glittering gem, their values encoded in integers (represented by the nums array).
To crack the lock, you need to arrange the gems in a specific order: for each adjacent pair, either the first gem's value must divide evenly into the second's, or vice versa. But cracking such a combination requires more than just brute force!

You're given an array of nums containing the values of the vault's gems (n distinct positive integers between 1 and 10^9).
Your mission is to find the total number of possible "special" arrangements of these gems, where every pair satisfies the divisibility requirement (i.e., forms a harmonious sequence). Since the number of special arrangements can be huge, you need to return the answer modulo 10^9 + 7 to avoid numerical overflows.

Input/Output Format:
Input:
An array nums containing the gem values separated by spaces or commas.

Output:
Return a single integer representing the total number of special gem arrangements modulo 10^9 + 7.

Examples:
Input:
2 3 6 (Three gems in the vault)

Output:
2 (Only two arrangements work: [3 6 2] and [2 6 3])

Input:
1 4 3 (Another vault to plunder)

Output:
2 (Similar to the first example, only two special arrangements exist: [3 1 4] and [4 1 3])

Constraints:
2 <= n <= 14 (Number of gems in the vault)
1 <= nums[i] <= 10^9 (Individual gem value)*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
class SpecialArrangements {
  public:
      int specialArr(vector<int>& nums) {
        //Write your code here
  
  
          dp.resize(20, vector<int>((1 << nums.size()) + 5, -1));
          vector<int> chosenIndices;
          return solve(nums, -1, chosenIndices);
      }
      vector<vector<int>> dp;
      int solve(vector<int>& nums, int previdx, vector<int>& chosenIndices) {
          if (chosenIndices.size() == nums.size())
              return 1;
         
          int mask = 0;
          for (int index : chosenIndices)
              mask |= (1 << index);
         
          if (dp[previdx + 1][mask] != -1)
              return dp[previdx + 1][mask];
     
          int tot = 0;
          for (int j = 0; j < nums.size(); j++) {
              if (find(chosenIndices.begin(), chosenIndices.end(), j) != chosenIndices.end())
              continue;
              if (previdx == -1 || nums[previdx] % nums[j] == 0 || nums[j] % nums[previdx] == 0) {
                  chosenIndices.push_back(j);
                  tot += solve(nums, j, chosenIndices);
                  tot %= 1000000007;
                  chosenIndices.pop_back();
              }
          }
          return  dp[previdx + 1][mask] = tot;
      }
  };
  int main(){
    vector<int> gems = {2, 3, 6};
    SpecialArrangements sp;
    cout<<sp.specialArr(gems);
  }

