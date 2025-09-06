#You are given two strings of equal lengths, s1 and s2. The task is to check if s2 is a reverse version of the string s1.
#Note: The characters in the strings are in lowercase.
#Examples :
#Input: s1 = "abcd", s2 = "cdab"
#Output: true
#Explanation: After 2 right rotations, s1 will become equal to s2.

class Solution:
    def reverse(self,s1,s2):
        if len(s1)==len(s2):
            for i in range(len(s1)):
                if s1[i]==s2[len(s2)-i-1]:
                    return True
                else:
                    return False
        return False
        
solution=Solution()
print(solution.reverse('abdc','cda'))