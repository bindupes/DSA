# to find all the non repeating characters in the stirng 

from collections import Counter

class Solution:
    def nonRepeatingCharacters(self, s):
        char_count = Counter(s)
        result = ""

        i=0
        while i < len(s):
            if char_count[char]==1:
                result+=s[i]
            i+=1

        return result if result else '$'
    
solution = Solution()
print(solution.nonRepeatingCharacters("geeksforgeeks"))