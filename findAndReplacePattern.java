/*### Problem Statement

Given a list of words and a pattern string, find all words that match the given pattern.

A word matches the pattern if there is a **one-to-one mapping** between characters in the pattern and characters in the word.

* Each pattern character should map to only one word character.
* Each word character should map to only one pattern character.

### Example

**Input:**

```text
words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
```

**Output:**

```text
["mee","aqq"]
```

### Explanation

Pattern:

```
a b b
```

Word:

```
m e e
```

Mapping:

```
a → m
b → e
```

Valid because the same pattern character `b` maps to the same character `e`.

But:

```
ccc
```

Mapping:

```
a → c
b → c
```

Invalid because two different pattern characters cannot map to the same word character.

### Approach

* Maintain two mappings:

  1. Pattern character → Word character
  2. Word character → Pattern character
* If any mapping conflicts occur, the word does not match.

### Complexity

For `n` words and word length `m`:

* **Time Complexity:** `O(n × m)`
* **Space Complexity:** `O(1)` (fixed 26 character arrays)
 */


import java.util.*;

class findAndReplacePattern {
   public List<String> Solution (List<String> li, String pattern) {
   List<String> result = new ArrayList<>();

   for(String word:li){
       if(matches(word,pattern)){
           result.add(word);
       }
   }
   return result;
   }
   private boolean matches(String word, String pattern){
       char[] patternToWord = new char[26];
       char[] wordToPattern = new char[26];

       for(int index =0;index<word.length();index++){
           char wordChar = word.charAt(index);
           char patternChar = pattern.charAt(index);

           if(patternToWord[patternChar - 'a']==0){
               patternToWord[patternChar-'a']=wordChar;
           }
           if(wordToPattern[wordChar-'a']==0){
               wordToPattern[wordChar-'a']=patternChar;
           }
           if(patternToWord[patternChar - 'a']!=wordChar || wordToPattern[wordChar - 'a'] != patternChar){
               return false;
           }
           

       }
       return true;
   }
   public static void main(String[] args){
      String[] hm = {"abc","deq","mee","aqq","dkd","ccc"};
      List<String> li = new ArrayList<>();
      li.addAll(Arrays.asList(hm));
      String word = "abb";
      findAndReplacePattern f = new findAndReplacePattern();
      System.out.println(f.Solution(li,word));


   }
}