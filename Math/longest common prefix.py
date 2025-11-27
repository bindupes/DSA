'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
'''

class Solution(object):
 def longestCommonPrefix(self,str):
   if not strs:
     return ""
   prefix = strs[0]
   for s in strs[1:]:
     while not s.startswith(prefix):
        prefix =prefix[:-1]
        if not prefix:
           return ""
   return prefix 



(OR)


class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        first=strs[0]
        for i in range(len(first)):
            char=first[i]
            for s in strs[1:]:
                if i>len(s) or s[i]!=char:
                    return first[:i]   # this will usually execute
        return first  # this only executes if the full string matches , like "flower" 
