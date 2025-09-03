#Given two strings s1 and s2 consisting of lowercase characters.
#The task is to check whether two given strings are an anagram of each other or not. 
# An anagram of a string is another string that contains the same characters, only the order of characters can be different. 
# For example, "act" and "tac" are an anagram of each other. Strings s1 and s2 can only contain lowercase alphabets.


class Solution:
    def areAnagrams(self, s1,s2):
        if len(s1)!=len(s2):
            return False
        return sorted(s1) == sorted(s2)

solution  =Solution()
print(solution.areAnagrams('geeks','kseeg'))