#Given two strings, one is a text string txt and the other is a pattern string pat. The task is to print the indexes of all the occurrences of the pattern string in the text string. Use 0-based indexing while returning the indices. 
#Note: Return an empty list in case of no occurrences of pattern.

#Examples :

#Input: txt = "abcab", pat = "ab"
#Output: [0, 3]
#Explanation: The string "ab" occurs twice in txt, one starts at index 0 and the other at index 3. 
#Input: txt = "abesdu", pat = "edu"
#Output: []
#Explanation: There's no substring "edu" present in txt.

class Solution:
    def find_pattern(self,text,pat):
        result=[]
        i=0
        while i < len(text):
            if text[i]==pat[0]:
                if text[i:i+len(pat)]==pat:
                    result.append(i)
            i+=1
        return result 
    
solution = Solution()
print(solution.find_pattern('abcab','ab'))


