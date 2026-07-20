"""
Group Anangrams
Given an array of strings strs, group the anagrams together. You can print the answer in sorted order. Also, output the list of anagrams in sorted order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input Format:
first line contains a single integer n (size of the array).
second line contains n strings.
Output Format:
Print the group of anagrams with a single space between them

Each group in new line
Constraints:
1 <= n <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
Example:
Input:
6
eat tea tan ate nat bat

Output:
ate eat tea
bat
nat tan

Explanation:
As ate comes before bat so the group of anagrams of ate should come before group of anagrams of bat. same for others.

class solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs){
      //Write your code here 

   }
};    """

class Solution:
    def anagram(self,cs:str,ps:str)-> bool:
        for c in cs:
            if c not in ps:
                return False
        for d in ps:
            if d not in cs:
                return False
        return True
            
    def groupAnagrams(self, strs):
      #Write your code here
       while len(strs)>0:
         for c in strs:
               print(c+" ",end='')
               for f in strs:
                   if c!=f:
                     if self.anagram(c,f):
                        print(f+" " ,end='')
                        strs.remove(f)
               print()
               strs.remove(c)
               
if __name__=="__main__":
    strs=["eat", "tea", "tan", "ate", "nat", "bat"]
    f=Solution()
    f.groupAnagrams(strs)
      