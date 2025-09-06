#Given a string s consisting of lowercase Latin Letters. 
# Return the first non-repeating character in s. 
# If there is no non-repeating character, return '$'.
from collections import Counter
class Solution:
    def countingchar(self,s):
        char_count = Counter(s)

        for char in s:
            if char_count[char]==1:
                return char
        return '$'
solution=Solution()
print(solution.countingchar('geeksforgeeks'))